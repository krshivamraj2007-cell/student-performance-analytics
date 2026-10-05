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

st.success("Database connected successfully!")


# --------------------------------------------------
# KEY PERFORMANCE INDICATORS
# --------------------------------------------------

st.subheader("📌 Key Performance Indicators")

total_students = len(df)

average_marks = df["average_marks"].mean()

average_attendance = df["attendance"].mean()

high_performers = (df["average_marks"] >= 75).sum()


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
# DEPARTMENT PERFORMANCE
# --------------------------------------------------

st.subheader("🏫 Department Performance")

department_performance = (
    df.groupby("department_name")["average_marks"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(department_performance)


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

st.subheader("👨‍🎓 Student Performance Data")

st.dataframe(
    df,
    use_container_width=True
)