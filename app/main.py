from flask import request, jsonify
from app import app
from app.constants import TABLE_NAME
from app.utils import delete_all_rows_from_table, detect_outliers, create_table, insert_data
from app.db import engine, metadata
from sqlalchemy import text
import pandas as pd

# Reflect the existing database schema to the metadata
metadata.reflect(bind=engine)

@app.route('/')
def home():
    """
    Home endpoint to test if the API is running.
    """
    return "<p>Hello! These are APIs to upload csv files and insert them to SQL, and delete all rows from SQL. Please use Postman to use them.</p>"

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Endpoint to upload a CSV file.
    The file is processed, checked for outliers, and inserted into the database.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        df = pd.read_csv(file)
        
        if detect_outliers(df):
            return jsonify({"error": "Outliers detected"}), 400
        
        create_table(df, TABLE_NAME)
        insert_data(df, TABLE_NAME)
        
        return jsonify({"message": "File successfully processed"}), 200

@app.route('/delete_all_rows', methods=['DELETE'])
def delete_all_rows():
    """
    Endpoint to delete all rows from the specified table.
    """
    response, status_code = delete_all_rows_from_table(TABLE_NAME)
    return jsonify(response), status_code

