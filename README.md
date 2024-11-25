# Mini_Project
Data Quality Project
Data Transformation and Statistical Analysis Project 

Table of Contents 

Overview 

Objective 

Technologies Used 

Features 

Data Flow 

Project Setup 

Database Schema 

Data Transformation 

Statistical Analysis 

Outputs 

Future Enhancements 

 

Overview 

This project processes food delivery data to extract insights about customer behavior, restaurant performance, and other metrics. It uses data from three tables: Customers, Orders, and Restaurants, performing transformations and aggregations to provide detailed statistical insights and visual reports. 

 

Objective 

The project aims to: 

Extract data from a PostgreSQL database. 

Transform data to calculate metrics such as high-spending customers and restaurant performance. 

Generate statistical insights and export them for further analysis. 

 

Technologies Used 

Programming Language: Python 

Database: PostgreSQL 

Libraries: Pandas, SQLAlchemy, NumPy 

 

Features 

Data extraction from PostgreSQL using SQLAlchemy. 

Identification of high-spending customers. 

Aggregation of restaurant performance metrics, including total revenue, total orders, and average order value. 

Statistical insights such as average order value, cuisine distribution, top restaurants, and highest revenue city. 

Export of transformed data and insights to CSV and database. 

 

Data Flow 

Extract: Load data from PostgreSQL tables Customers, Orders, and Restaurants. 

Transform: Perform data cleaning, merging, and aggregation. 

Analyze: Compute metrics for customers and restaurants. 

Export: Save data and insights as CSV files. 

 

Project Setup 

Prerequisites 

Python 3.x installed. 

PostgreSQL database with the required tables (Customers, Orders, Restaurants). 

Install Python libraries: pip install pandas sqlalchemy psycopg2 
  

Steps to Run 

Update the database connection details in the script: DATABASE_USER = 'postgres' 
DATABASE_PASSWORD = 'Notrust$1' 
DATABASE_HOST = 'localhost' 
DATABASE_PORT = '5432' 
DATABASE_NAME = 'postgres' 
  

Run the script: python "Python Code for Data Transformation.py" 
  

 

Database Schema 

Customers Table 

Column 

Data Type 

customer_id 

INT 

customer_name 

VARCHAR 

email 

VARCHAR 

... 

... 

Orders Table 

Column 

Data Type 

order_id 

INT 

customer_id 

INT 

restaurant_id 

INT 

order_amount 

FLOAT 

... 

... 

Restaurants Table 

Column 

Data Type 

restaurant_id 

INT 

name 

VARCHAR 

cuisine_type 

VARCHAR 

location 

VARCHAR 

 

Data Transformation 

Data Cleaning: Strips extra spaces from column names. 

High-Spending Customers:  

Identifies customers with total spending above $500. 

Data Joining:  

Combines Customers, Orders, and Restaurants tables. 

Aggregation:  

Computes total orders, revenue, and average order value per restaurant. 

 

Statistical Analysis 

The project computes the following: 

Average Order Value: Average revenue per order. 

High-Spending Customers: List of customers spending more than $500. 

Cuisine Distribution: Count of orders per cuisine type. 

Top Restaurants: Top 10 restaurants by revenue. 

Highest Revenue City: City generating the most revenue. 

 

Outputs 

Transformed Data:  

Exported to customer_order_summary.csv and saved in PostgreSQL. 

Insights Report:  

Saved as zomato_insights_report.csv. 

Console Outputs:  

Displays summaries and insights. 

 

Future Enhancements 

Visualizations: Add graphs for insights. 

Real-Time Data Updates: Automate data processing and analysis. 

Interactive Dashboards: Use tools like Power BI or Tableau. 

 
