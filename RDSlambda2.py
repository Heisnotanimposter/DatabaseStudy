import os
import json
import mysql.connector
import tensorflow as tf
from tensorflow.keras.models import load_model

def lambda_handler(event, context):
    # Load the pre-trained Gemini LLM model
    model_path = os.environ['MODEL_PATH']
    model = load_model(model_path)  # Ensure the model is compatible with TensorFlow's load_model

    # Database configuration
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

    # Query to fetch data for model fine-tuning
    query = "SELECT * FROM training_data LIMIT 1000;"  # Adjusted for more data

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    result = cursor.fetchall()

    # Convert result to a suitable format for TensorFlow processing
    # This example assumes you are fetching numeric data; adjust preprocessing as needed
    data = tf.convert_to_tensor([list(row) for row in result], dtype=tf.float32)

    # Use the data to fine-tune the model
    # This is a simplified example; you might want to split data into features and labels, etc.
    model.fit(data, data, epochs=5)  # Self-training example for demonstration

    # Save the fine-tuned model back to a file or other storage
    model.save(model_path)

    # Clean up
    cursor.close()
    connection.close()

    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps("Model fine-tuned successfully")
    }