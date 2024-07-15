from flask import request, jsonify
from app import app
from app.constants import TABLE_NAME
from app.utils import detect_outliers, create_table, insert_data
from app.db import engine, metadata
from sqlalchemy import text
import pandas as pd

# Reflect the existing database schema to the metadata
metadata.reflect(bind=engine)

@app.route('/')
def test():
    return "<p>Hello! These are APIs to upload csv files and insert them to SQL.</p>"

@app.route('/upload', methods=['POST'])
def upload_file():
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
    try:
        # Construct SQL query to delete all rows
        delete_query = text(f'DELETE FROM {TABLE_NAME}')

        # Execute the delete query
        with engine.connect() as connection:
            connection.execute(delete_query)

        return jsonify({"message": f"All rows deleted from '{TABLE_NAME}'"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

