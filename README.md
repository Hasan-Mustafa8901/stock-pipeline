# Stock Market ETL & Analytics Dashboard

An end-to-end data engineering and analytics project that extracts stock market data using public APIs, processes it with PySpark, stores it in MySQL, and serves dynamic, interactive visualizations through a Flask web application.


## Project Overview

**Objective:** Build a real-time stock market analytics pipeline that demonstrates skills across the full data stack: ETL, data engineering, backend development, and data visualization.

## Tech Stack

- **Python 3**
- **yfinance API** – for extracting stock market data
- **PySpark** – for data cleaning, transformation & feature engineering
- **MySQL** – for structured storage of processed data
- **Flask** – for serving a dynamic web application
- **Plotly.js** – for interactive data visualizations
- **HTML/CSS/JavaScript** – for front-end development
- **Git** – for version control

## Project Architecture

yfinance API → PySpark (ETL Pipeline) → MySQL Database → Flask Web App → Interactive Dashboard

## 🔧 Features

- Automated data extraction from yfinance
- Modular ETL pipeline using PySpark (cleaning, transformation, feature engineering)
- Processed data stored in MySQL relational database
- Flask backend to serve data dynamically
- Real-time filtering by:
  - Stock Ticker
  - Date Range
- Summary Statistics:
  - Average Closing Price for a stock
  - Average Opening Price for a stock
  - Average Daily Return
- Interactive Plotly Charts for visual analysis
- Responsive Dark/Light Mode toggle
- Modular, scalable, and production-friendly code structure

## Project Structure

<pre>
stock-pipeline/
│
├── ETL/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│
├── app/
│ ├── app.py
│ ├── templates/
│ └── home.html
│
├── static/ # (Optional for future custom styles)
├── requirements.txt
├── .gitignore
└── README.md
</pre>

## How to Run

### Clone the Repository

```bash
git clone https://github.com/Hasan-Mustafa8901/stock-pipeline.git
cd stock-pipeline
```
### Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Setup MySQL Database

Create database: `stockDB`

Create table schema as per your processed data.

Update database credentials inside `app/app.py`.

### Run ETL Pipeline
Run ETL scripts inside `ETL/` to extract, transform and load data into MySQL.

### Run Flask Web App

```bash
cd app
python app.py
```
## Future Enhancements

- Deploying a Machine Learning model to predict the stock market

- Add more advanced financial metrics

- Deploy web app on cloud (Render, PythonAnywhere, etc.)

- Dockerize the entire pipeline

- Pagination for large datasets

- Multi-ticker comparison

- Enhanced UI/UX with modern design

## Learning Outcomes
- Hands-on with full end-to-end ETL

- Working with real-world stock market data

- Data engineering using PySpark

- MySQL integration & relational modeling

- Backend API development with Flask

- Frontend visualization using Plotly.js

- Building scalable and modular pipelines

![Screenshot 2025-06-17 013139](https://github.com/user-attachments/assets/5ce8fbab-61fd-4db3-90a2-32fc876dbbb5)
![Screenshot 2025-06-17 013203](https://github.com/user-attachments/assets/75306f65-a825-472b-9df6-ffba05f83b8b)





