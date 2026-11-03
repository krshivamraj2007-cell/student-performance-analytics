# Student Performance Analytics

[![Pipeline Tests](https://github.com/krshivamraj2007-cell/student-performance-analytics/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/krshivamraj2007-cell/student-performance-analytics/actions/workflows/tests.yml)

A data analytics project that processes student academic records, analyzes marks and attendance, identifies performance and potential academic risk levels, and presents insights through an interactive Streamlit dashboard.

This project demonstrates an end-to-end data analytics workflow using Python, Pandas, PostgreSQL, SQL, and Streamlit.

## Features

- **Synthetic Data Generation:** Generate student records for demonstration and testing.
- **Data Cleaning:** Clean and preprocess records using Pandas.
- **Data Transformation:** Transform student data and categorize academic performance.
- **PostgreSQL Integration:** Store and manage structured academic records.
- **SQL Analytics:** Analyze marks, attendance, academic performance, and departmental results.
- **Interactive Dashboard:** Explore academic data through a Streamlit dashboard.
- **Filtering and Search:** Filter results and search for student records using the available dashboard controls.
- **Performance Analysis:** Explore performance categories and student rankings.
- **Attendance Analysis:** Examine attendance statistics and identify potential academic risks.
- **KPI Metrics:** View key academic indicators and summary statistics.
- **Automated Testing:** Test pipeline functionality using pytest.
- **Continuous Integration:** Automatically run tests through GitHub Actions.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data pipeline and processing |
| Pandas | Data cleaning and transformation |
| PostgreSQL | Relational database |
| SQL | Analytical queries and reporting |
| Streamlit | Interactive dashboard |
| pytest | Automated testing |
| Git and GitHub | Version control and repository hosting |
| GitHub Actions | Continuous integration |

## Project Architecture

```text
Synthetic Student Data
        |
        v
Data Cleaning and Preprocessing
        |
        v
Data Transformation and Validation
        |
        v
PostgreSQL Database
        |
        v
SQL Analytics
        |
        v
Streamlit Dashboard
        |
        v
KPIs, Charts, and Insights
```

## Project Structure

```text
student-performance-analytics/
├── dashboard/
│   └── app.py
├── data/
│   └── Student CSV files
├── sql/
│   ├── 01_basic_analysis.sql
│   ├── 02_performance_analysis.sql
│   └── 03_advanced_analysis.sql
├── src/
│   ├── analyze_data.py
│   ├── clean_data.py
│   ├── dashboard_data.py
│   ├── db_connection.py
│   ├── generate_data.py
│   ├── load_attendance.py
│   ├── load_marks.py
│   ├── load_students.py
│   ├── subject_map.py
│   ├── transform_data.py
│   └── validate_data.py
├── tests/
│   └── test_pipeline.py
├── .env.example
├── .gitignore
├── requirements.txt
├── run_pipeline.py
└── README.md
```

*Note: This structure highlights the main project files. Additional files may exist in individual directories.*

## Prerequisites

Install the following before running the project:

- Python 3
- PostgreSQL
- Git
- pip

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/krshivamraj2007-cell/student-performance-analytics.git
cd student-performance-analytics
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create your local environment file:

```bash
cp .env.example .env
```

Open `.env` in VS Code and configure the database connection using the variable names defined in `.env.example`.

For a local PostgreSQL database, the configuration may resemble:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=student_performance
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
```

Replace the example values with your actual PostgreSQL credentials.

**Important:** These variable names are examples. Use the exact names expected by your project's database connection code.

The application may also use `NEON_DATABASE_URL` when configured. Ensure it points to the intended database and that the required tables exist.

Never commit your `.env` file, database passwords, or private connection strings to GitHub.

### 5. Prepare the Database

Ensure PostgreSQL is running and the `student_performance` database exists.

The pipeline and dashboard depend on the required database tables and their data. Follow the database initialization and loading steps implemented in the project.

## Run the Data Pipeline

From the project root, execute:

```bash
python3 run_pipeline.py
```

The pipeline runs the configured data generation, cleaning, transformation, validation, and database-loading steps.

Make sure your database configuration is correct before running the pipeline.

## Run the Streamlit Dashboard

Start the dashboard:

```bash
streamlit run dashboard/app.py
```

Open the local address displayed in the terminal to explore the dashboard.

The dashboard requires the configured PostgreSQL database and the tables and data used by its queries.

## Run Automated Tests

Execute the test suite:

```bash
python3 -m pytest
```

To generate a test coverage report, install `pytest-cov` if necessary:

```bash
python3 -m pip install pytest-cov
```

Then run:

```bash
python3 -m pytest --cov=src --cov-report=term-missing
```

The project uses GitHub Actions to run automated tests through its configured CI workflow.

**Latest verified local result:** 10 tests passed during the reported test run. Results may change if the code or environment changes.

## SQL Analytics

The project includes SQL scripts for exploring student academic data.

| SQL File | Purpose |
|---|---|
| `01_basic_analysis.sql` | Basic academic statistics and summaries |
| `02_performance_analysis.sql` | Student performance analysis |
| `03_advanced_analysis.sql` | Advanced analytical queries |

These queries support analysis of student marks, attendance, performance categories, and other academic indicators.

## Dataset

The project uses synthetic student records for demonstration and testing.

The records can be processed through the data pipeline, stored in PostgreSQL, and analyzed through SQL queries and the dashboard.

**Disclaimer:** Synthetic records are for demonstration purposes and should not be interpreted as actual student results.

## Future Improvements

Potential future enhancements include:

- Deploying the dashboard to a cloud platform.
- Adding downloadable analytical reports.
- Improving data validation and error handling.
- Introducing role-based access control.
- Exploring predictive analytics to identify students who may need academic support.

These are possible extensions and are not claimed as existing features.

## Learning Outcomes

This project demonstrates practical experience with:

- Building Python data pipelines.
- Cleaning and transforming data using Pandas.
- Integrating applications with PostgreSQL.
- Writing SQL queries for analytical reporting.
- Developing interactive dashboards with Streamlit.
- Writing automated tests using pytest.
- Configuring continuous integration with GitHub Actions.
- Managing source code using Git and GitHub.

## Author

Developed as a data analytics portfolio project using Python, Pandas, PostgreSQL, SQL, and Streamlit.
