# Student Performance Analytics

[![Pipeline Tests](https://github.com/krshivamraj2007-cell/student-performance-analytics/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/krshivamraj2007-cell/student-performance-analytics/actions/workflows/tests.yml)

A data analytics project that processes student academic records, analyzes marks and attendance, identifies performance and risk levels, and presents insights through an interactive Streamlit dashboard.

The project demonstrates an end-to-end data workflow using Python, Pandas, PostgreSQL, SQL, and Streamlit.

## Features

- **Data Generation:** Generate synthetic student records for demonstration and testing.
- **Data Cleaning:** Clean and preprocess data using Pandas.
- **Data Transformation:** Transform student records and categorize academic performance.
- **PostgreSQL Integration:** Store and query structured student data.
- **SQL Analytics:** Analyze academic performance, marks, attendance, and departmental results.
- **Interactive Dashboard:** Explore results through a Streamlit dashboard.
- **Filtering and Search:** Filter results by department and semester and search for students.
- **Performance Analysis:** Examine student performance categories and rankings.
- **Attendance Analysis:** Explore attendance statistics and potential academic risks.
- **KPI Metrics:** View key academic indicators and summary statistics.
- **Automated Testing:** Validate project functionality using pytest.
- **Continuous Integration:** Run automated tests through GitHub Actions.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and pipeline development |
| Pandas | Data cleaning, transformation, and analysis |
| PostgreSQL | Relational database |
| SQL | Academic analytics and reporting queries |
| Streamlit | Interactive dashboard |
| pytest | Automated testing |
| Git and GitHub | Version control and project hosting |
| GitHub Actions | Continuous integration |

## Project Architecture

```text
Synthetic Student Data
          |
          v
Data Cleaning and Preprocessing
          |
          v
Data Transformation
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
Charts, KPIs and Insights
```

## Project Structure

```text
student-performance-analytics/
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── Student CSV files
│
├── sql/
│   ├── 01_basic_analysis.sql
│   ├── 02_performance_analysis.sql
│   └── 03_advanced_analysis.sql
│
├── src/
│   ├── Data processing modules
│   └── Database and dashboard utilities
│
├── tests/
│   └── Automated tests
│
├── .env.example
├── .gitignore
├── requirements.txt
├── run_pipeline.py
└── README.md
```

*Note: Some filenames are represented by their purpose. Refer to the repository for the exact contents of each directory.*

## Prerequisites

Before running the project, install:

- Python 3
- PostgreSQL
- Git
- pip

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/krshivamraj2007-cell/student-performance-analytics.git
cd student-performance-analytics
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Configure the database

Create a PostgreSQL database named `student_performance`, unless your existing database uses a different name.

Copy the example environment file:

```bash
cp .env.example .env
```

Open `.env` and enter the database configuration expected by your project.

For a local PostgreSQL setup, the values may resemble:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=student_performance
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
```

**Important:** These variable names are examples. Keep the names consistent with your existing `.env.example` and database connection code. Do not commit `.env` or publish passwords and connection strings.

If your application prioritizes `NEON_DATABASE_URL`, ensure it is configured appropriately for the database you intend to use.

## Run the Data Pipeline

Execute the pipeline from the project root:

```bash
python3 run_pipeline.py
```

The pipeline runs the configured data processing and database-loading steps.

Ensure that PostgreSQL is running and the required database configuration is correct before executing it.

## Run the Dashboard

Start the Streamlit application:

```bash
streamlit run dashboard/app.py
```

Streamlit will provide a local address in the terminal. Open that address in your browser to explore the dashboard.

Depending on your configuration, the dashboard requires the PostgreSQL tables and data to be available.

## Run Automated Tests

Run the test suite:

```bash
python3 -m pytest
```

For a coverage report, if `pytest-cov` is installed:

```bash
python3 -m pytest --cov=src --cov-report=term-missing
```

GitHub Actions is configured to run automated tests when the relevant workflow triggers occur.

## Database Analytics

The project includes SQL scripts for analyzing student records.

| SQL file | Purpose |
|---|---|
| `01_basic_analysis.sql` | Basic academic statistics and summaries |
| `02_performance_analysis.sql` | Student performance analysis |
| `03_advanced_analysis.sql` | More advanced analytical queries |

These queries support exploration of student marks, attendance, and academic performance.

## Data

The project uses synthetic student records for demonstration and learning.

The data can be processed and loaded into PostgreSQL for analysis through SQL queries and the dashboard.

Synthetic data should not be interpreted as real student results.

## Future Improvements

Potential extensions include:

- Deploy the dashboard to a cloud platform.
- Add more advanced visualizations and downloadable reports.
- Improve data validation and error handling.
- Add role-based access control.
- Explore predictive analytics for identifying students who may need academic support.

## Learning Outcomes

This project provides practical experience with:

- Python-based data pipelines.
- Data cleaning and transformation using Pandas.
- Relational database integration with PostgreSQL.
- SQL queries for analytical reporting.
- Interactive dashboard development with Streamlit.
- Automated testing and continuous integration.
- Version control and project documentation using Git and GitHub.

## Author

Developed as a data analytics portfolio project using Python, Pandas, PostgreSQL, SQL, and Streamlit.