import os
import json
import mysql.connector

def lambda_handler(event, context):
    # Configuration for database connection
    config = {
        'user': os.environ['DB_USER'],
        'password': os.environ['DB_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'database': os.environ['DB_NAME'],
        'raise_on_warnings': True
    }

    # Connect to the database
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Query to execute
    query = "SELECT * FROM your_table_name LIMIT 10;"

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    result = cursor.fetchall()

    # Clean up
    cursor.close()
    connection.close()

    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }