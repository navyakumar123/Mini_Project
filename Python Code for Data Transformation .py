from sqlalchemy import create_engine
import pandas as pd

# Database connection details
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'Notrust$1'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'
DATABASE_NAME = 'postgres'

# Establish database connection
engine = create_engine(f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')

# Load data from PostgreSQL
customers_df = pd.read_sql("SELECT * FROM Customers", engine)
orders_df = pd.read_sql("SELECT * FROM Orders", engine)
restaurants_df = pd.read_sql("SELECT * FROM Restaurants", engine)

# Clean column names
customers_df.columns = customers_df.columns.str.strip()
orders_df.columns = orders_df.columns.str.strip()
restaurants_df.columns = restaurants_df.columns.str.strip()

# Check if required columns exist in the DataFrames
required_customer_cols = {'customer_id'}
required_order_cols = {'customer_id', 'order_amount', 'restaurant_id'}
required_restaurant_cols = {'restaurant_id'}

if required_customer_cols.issubset(customers_df.columns) and \
   required_order_cols.issubset(orders_df.columns) and \
   required_restaurant_cols.issubset(restaurants_df.columns):

    # Calculate total spending per customer
    total_spending = orders_df.groupby('customer_id')['order_amount'].sum()

    # Filter customers with total order amount greater than $500
    high_spending_customers = total_spending[total_spending > 500].index
    high_spending_df = customers_df[customers_df['customer_id'].isin(high_spending_customers)]

    # Join data to get detailed order history
    customer_orders_df = pd.merge(orders_df, customers_df, on='customer_id', how='inner')
    customer_orders_restaurants_df = pd.merge(customer_orders_df, restaurants_df, on='restaurant_id', how='inner')

    # Check if 'name' exists in customer_orders_restaurants_df
    if 'name' in customer_orders_restaurants_df.columns:
        group_by_columns = ['restaurant_id', 'name']
    else:
        print("Warning: 'name' column is missing. Grouping by 'restaurant_id' only.")
        group_by_columns = ['restaurant_id']

    # Aggregation for restaurants
    restaurant_summary = customer_orders_restaurants_df.groupby(group_by_columns).agg(
        total_orders=('order_amount', 'count'),
        total_revenue=('order_amount', 'sum'),
        avg_order_value=('order_amount', 'mean')
    ).reset_index()

    # Find the top 10 customers based on total spending
    top_10_customers = total_spending.sort_values(ascending=False).head(10)

    # Save transformed data
    customer_orders_restaurants_df.to_sql('Customer_Order_Summary', engine, if_exists='replace', index=False)
    customer_orders_restaurants_df.to_csv('customer_order_summary.csv', index=False)

    # Display restaurant summary and top 10 customers
    print("Restaurant Summary:")
    print(restaurant_summary.head())
    print("\nTop 10 Customers by Total Spending:")
    print(top_10_customers)

    # Statistical Insights
    if 'order_amount' in customer_orders_restaurants_df.columns:
        avg_order_value = customer_orders_restaurants_df['order_amount'].mean()

        if 'cuisine_type' in customer_orders_restaurants_df.columns:
            cuisine_distribution = customer_orders_restaurants_df.groupby('cuisine_type')['order_amount'].count().sort_values(ascending=False)
        else:
            print("Warning: 'cuisine_type' column is missing.")
            cuisine_distribution = pd.Series()

        top_restaurants = restaurant_summary.sort_values(by='total_revenue', ascending=False).head(10)
        avg_top_restaurant_rating = top_restaurants['avg_order_value'].mean()

        if 'location' in customer_orders_restaurants_df.columns:
            city_revenue = customer_orders_restaurants_df.groupby('location')['order_amount'].sum()
            highest_revenue_city = city_revenue.idxmax()
        else:
            print("Warning: 'location' column is missing.")
            highest_revenue_city = None

        insights = {
            'Average Order Value': avg_order_value,
            'Top 10 Restaurants by Revenue': top_restaurants[['restaurant_id', 'total_revenue']],
            'Cuisine Distribution': cuisine_distribution,
            'Average Rating of Top Restaurants': avg_top_restaurant_rating,
            'Highest Revenue City': highest_revenue_city
        }

        # Save insights to CSV
        insights_df = pd.DataFrame({k: [v] for k, v in insights.items() if isinstance(v, (int, float, str))})
        insights_df.to_csv('zomato_insights_report.csv', index=False)

        print("\nStatistical Insights:")
        print(insights)

else:
    print("Error: One or more required columns are missing in the DataFrames.")
