/*
1. Database Setup 
Tools Required: PostgreSQL, pgAdmin, or another SQL management tool. 
---------------------------------------------------------------------

SQL Scripts for Table creation and Load
-----------------------------------------
Tables to Create:
 
Customers: 
Customer_ID: Unique identifier. 
Name: Customer's name. 
Age: Customer's age. 
Gender: Customer's gender. 
Location: Customer's location (city). 
************************************************************************
Orders: 
Order_ID: Unique identifier for each order. 
Customer_ID: Foreign key referencing Customers. 
Restaurant_ID: Foreign key referencing Restaurants. 
Order_Date: Date and time of the order. 
Order_Amount: Total amount for the order. 
**************************************************************************
Restaurants: 
Restaurant_ID: Unique identifier for each restaurant. 
Name: Restaurant's name. 
Cuisine_Type: Cuisine offered by the restaurant (e.g., Indian, Chinese). 
Location: Restaurant's location (city). 
Rating: Average rating for the restaurant. 
*/


-- Creating the 'Customers' table 
CREATE TABLE Customers ( 
    Customer_ID SERIAL PRIMARY KEY, 
    Name VARCHAR(100), 
    Age INT, 
    Gender VARCHAR(10), 
    Location VARCHAR(100) 
); 
 
-- Creating the 'Restaurants' table 
CREATE TABLE Restaurants ( 
    Restaurant_ID SERIAL PRIMARY KEY, 
    Name VARCHAR(100), 
    Cuisine_Type VARCHAR(50), 
    Location VARCHAR(100), 
    Rating DECIMAL(3, 2) 
); 
 
-- Creating the 'Orders' table 
CREATE TABLE Orders ( 
    Order_ID SERIAL PRIMARY KEY, 
    Customer_ID INT REFERENCES Customers(Customer_ID), 
    Restaurant_ID INT REFERENCES Restaurants(Restaurant_ID), 
    Order_Date TIMESTAMP, 
    Order_Amount DECIMAL(10, 2) 
); 
  

/*
-------------------------------------------------------------------------------------
Data Ingestion: 
Load sample datasets into these tables using the SQL COPY command or any other method. 
--------------------------------------------------------------------------------------
 */

-- Loading data for Customers table 
COPY Customers (Customer_ID,Name, Age, Gender, Location) 
FROM 'C:\Mini Project\CSV Files\customers.csv' DELIMITER ',' CSV HEADER; 
 
-- Loading data for Restaurants table 
COPY Restaurants (Restaurant_ID,Name, Cuisine_Type, Location, Rating) 
FROM 'C:\Mini Project\CSV Files\restaurants.csv' DELIMITER ',' CSV HEADER; 
 
-- Loading data for Orders table 
COPY Orders (Order_ID,Customer_ID, Restaurant_ID, Order_Date, Order_Amount) 
FROM 'C:\Mini Project\CSV Files\orders.csv' DELIMITER ',' CSV HEADER; 
