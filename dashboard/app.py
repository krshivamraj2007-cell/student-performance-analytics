# import streamlit as st

# st.set_page_config(
#     page_title="Student Performance Analytics",
#     page_icon="📊",
#     layout="wide"
# )

# st.title("📊 Student Performance Analytics")
# st.write("Dashboard is working!")


#

# st.title("📊 Student Performance Analytics")

# df = get_student_performance()

# st.success("Database connected successfully!")

# st.write("Student Performance Data")

# st.dataframe(df)


# st.subheader("📌 Key Performance Indicators")

# total_students = len(df)
# average_marks = df["average_marks"].mean()
# average_attendance = df["attendance"].mean()
# high_performers = (df["average_marks"] >= 75).sum()

# col1, col2, col3, col4 = st.columns(4)

# col1.metric("Total Students", total_students)
# col2.metric("Average Marks", f"{average_marks:.2f}")
# col3.metric("Average Attendance", f"{average_attendance:.2f}%")
# col4.metric("High Performers", high_performers)

import pandas as pd
#
# DEPARTMENT SECTION
#

import streamlit as st
import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.dashboard_data import (
    get_student_performance,
    get_subject_performance
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Student Performance Analytics")


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = get_student_performance()

st.sidebar.header("Filters")

departments = ["All"] + sorted(df["department_name"].unique().tolist())

selected_department = st.sidebar.selectbox(
    "Department",
    departments
)

if selected_department != "All":
    df = df[df["department_name"] == selected_department]

semesters = ["All"] + sorted(df["semester"].unique().tolist())

selected_semester = st.sidebar.selectbox(
    "Semester",
    semesters
)

if selected_semester != "All":
    df = df[df["semester"] == selected_semester]
student_search = st.sidebar.text_input(
    "Search Student",
    placeholder="Enter name or student ID"
)

if student_search:
    search = student_search.strip().lower()

    df = df[
        df["name"].str.lower().str.contains(search, na=False)
        | df["student_id"].str.lower().str.contains(search, na=False)
    ]
performance_categories = [
    "All",
    "Excellent",
    "Good",
    "Average",
    "Below Average",
    "Poor"
]

selected_category = st.sidebar.selectbox(
    "Performance Category",
    performance_categories
)

if selected_category != "All":

    if selected_category == "Excellent":
        df = df[df["average_marks"] >= 90]

    elif selected_category == "Good":
        df = df[
            (df["average_marks"] >= 75) &
            (df["average_marks"] < 90)
        ]

    elif selected_category == "Average":
        df = df[
            (df["average_marks"] >= 60) &
            (df["average_marks"] < 75)
        ]

    elif selected_category == "Below Average":
        df = df[
            (df["average_marks"] >= 40) &
            (df["average_marks"] < 60)
        ]

    elif selected_category == "Poor":
        df = df[df["average_marks"] < 40]

attendance_status = st.sidebar.selectbox(
    "Attendance Status",
    [
        "All",
        "Good (≥ 75%)",
        "At Risk (< 75%)"
    ]
)

if attendance_status == "Good (≥ 75%)":
    df = df[df["attendance"] >= 75]

elif attendance_status == "At Risk (< 75%)":
    df = df[df["attendance"] < 75]

risk_filter = st.sidebar.selectbox(
    "Risk Level",
    [
        "All",
        "Low Risk",
        "Medium Risk",
        "High Risk"
    ]
)

if risk_filter != "All":
    df = df[df["risk_level"] == risk_filter]

st.success("Database connected successfully!")


# --------------------------------------------------
# KEY PERFORMANCE INDICATORS
# --------------------------------------------------

st.subheader("📌 Key Performance Indicators")

total_students = len(df)

average_marks = df["average_marks"].mean()

average_attendance = df["attendance"].mean()

high_performers = (df["average_marks"] >= 75).sum()

st.subheader("🧠 Dashboard Insights")

if not df.empty:
    st.info(
        f"📌 The average academic performance of the selected students "
        f"is **{average_marks:.2f} marks**."
    )
    st.info(
    f"📚 The average attendance of the selected students "
    f"is **{average_attendance:.2f}%**."
)
    at_risk_count = len(
    df[
        (df["attendance"] < 75) &
        (df["average_marks"] < 60)
    ]
)

    st.warning(
    f"⚠️ There are **{at_risk_count} students** "
    f"at academic and attendance risk."
)
    top_student = df.loc[
    df["average_marks"].idxmax()
]

    st.success(
    f"🏆 **{top_student['name']}** is the top performer "
    f"with an average of **{top_student['average_marks']:.2f} marks**."
)
    
else:
    st.warning("No students match the selected filters.")


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Students",
    total_students
)

col2.metric(
    "Average Marks",
    f"{average_marks:.2f}"
)

col3.metric(
    "Average Attendance",
    f"{average_attendance:.2f}%"
)

col4.metric(
    "High Performers",
    high_performers
)


# --------------------------------------------------


# DEPARTMENT FILTER

st.subheader("📊 Department Performance")

departments = ["All"] + sorted(df["department_name"].unique().tolist())

selected_department = st.selectbox(
    "Select Department",
    departments
)

if selected_department != "All":
    filtered_df = df[df["department_name"] == selected_department]
else:
    filtered_df = df

department_performance = (
    filtered_df.groupby("department_name")["average_marks"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(department_performance)

# --------------------------------------------------
# Student Performance Distribution
# --------------------------------------------------

st.subheader("🎯 Student Performance Distribution")

performance_distribution = (
    df.assign(
        performance_category=pd.cut(
            df["average_marks"],
            bins=[0, 40, 60, 75, 90, 100],
            labels=[
                "Poor",
                "Below Average",
                "Average",
                "Good",
                "Excellent"
            ],
            include_lowest=True
        )
    )
    ["performance_category"]
    .value_counts()
    .reindex(
        ["Excellent", "Good", "Average", "Below Average", "Poor"],
        fill_value=0
    )
)

st.bar_chart(performance_distribution)


# --------------------------------------------------
# At-Risk Students
# --------------------------------------------------

st.subheader("⚠️ At-Risk Students")

at_risk_students = df[
    (df["attendance"] < 75) &
    (df["average_marks"] < 60)
].copy()

st.metric(
    "Students At Risk",
    len(at_risk_students)
)

st.dataframe(
    at_risk_students[
        [
            "student_id",
            "name",
            "department_name",
            "average_marks",
            "attendance"
        ]
    ],
    use_container_width=True
)


# --------------------------------------------------
# Top 10 Students
# --------------------------------------------------

st.subheader("🏆 Top 10 Students")

top_students = (
    df[
        [
            "student_id",
            "name",
            "department_name",
            "average_marks",
            "attendance"
        ]
    ]
    .sort_values("average_marks", ascending=False)
    .head(10)
)

st.dataframe(
    top_students,
    use_container_width=True
)

# --------------------------------------------------
# Attendance Distribution
# --------------------------------------------------

st.subheader("📊 Attendance Distribution")

attendance_distribution = (
    pd.cut(
        df["attendance"],
        bins=[0, 75, 85, 90, 100],
        labels=[
            "Below 75%",
            "75% - 84%",
            "85% - 89%",
            "90% - 100%"
        ],
        include_lowest=True
    )
    .value_counts()
    .sort_index()
)

st.bar_chart(attendance_distribution)
# --------------------------------------------------
# SUBJECT PERFORMANCE
# --------------------------------------------------

st.subheader("📚 Subject Performance")

subject_performance = get_subject_performance()

st.bar_chart(
    subject_performance.set_index("subject_name")["average_marks"]
)


# --------------------------------------------------
# STUDENT PERFORMANCE DATA
# --------------------------------------------------
st.subheader("👤 Student Details")

if not df.empty:

    student_options = (
        df["student_id"] + " - " + df["name"]
    ).tolist()

    selected_student = st.selectbox(
        "Select Student",
        student_options
    )

    selected_student_id = selected_student.split(" - ")[0]

    student = df[
        df["student_id"] == selected_student_id
    ].iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Student ID",
        student["student_id"]
    )

    col2.metric(
        "Department",
        student["department_name"]
    )

    col3.metric(
        "Semester",
        student["semester"]
    )

    col4.metric(
        "Average Marks",
        f"{student['average_marks']:.2f}"
    )

    col5, col6 = st.columns(2)

    col5.metric(
        "Attendance",
        f"{student['attendance']:.2f}%"
    )

    col6.metric(
        "Name",
        student["name"]
    )
df["risk_level"] = "Low Risk"
st.subheader("🚦 Risk Level Distribution")

risk_distribution = (
    df["risk_level"]
    .value_counts()
    .reindex(
        ["Low Risk", "Medium Risk", "High Risk"],
        fill_value=0
    )
)

st.bar_chart(risk_distribution)

df.loc[
    (df["attendance"] < 75) |
    (df["average_marks"] < 60),
    "risk_level"
] = "Medium Risk"

df.loc[
    (df["attendance"] < 75) &
    (df["average_marks"] < 60),
    "risk_level"
] = "High Risk"
st.subheader("👨‍🎓 Student Performance Data")

st.dataframe(
    df,
    use_container_width=True
)

csv_data = df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv_data,
    file_name="student_performance_filtered.csv",
    mime="text/csv"
)