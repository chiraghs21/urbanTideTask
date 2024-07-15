import pandas as pd
from sqlalchemy import Table, Column, Integer, String, Float, MetaData, text
from app.db import engine, metadata

def detect_outliers(df):
    """
    Detect outliers in the dataframe using the Interquartile Range (IQR) method.
    
    Parameters:
    df (DataFrame): The dataframe to check for outliers.

    Returns:
    bool: True if outliers are detected, False otherwise.
    """
    Q1 = df['value'].quantile(0.25)
    Q3 = df['value'].quantile(0.75)
    IQR = Q3 - Q1
    filter = (df['value'] >= (Q1 - 1.5 * IQR)) & (df['value'] <= (Q3 + 1.5 * IQR))
    return not all(filter)

def create_table(df, table_name):
    """
    Create a table in the database based on the dataframe schema.
    
    Parameters:
    df (DataFrame): The dataframe whose schema will be used to create the table.
    table_name (str): The name of the table to be created.
    """
    columns = [Column('timestamp', String), Column('value', Float), Column('category', String)]
    table = Table(table_name, metadata, *columns, extend_existing=True)
    metadata.create_all(engine)

def insert_data(df, table_name):
    """
    Insert data from the dataframe into the specified table in the database.
    
    Parameters:
    df (DataFrame): The dataframe containing the data to be inserted.
    table_name (str): The name of the table where data will be inserted.
    """
    df.to_sql(table_name, engine, if_exists='append', index=False)

def delete_all_rows_from_table(table_name):
    """
    Delete all rows from the specified table in the database.
    
    Parameters:
    table_name (str): The name of the table from which all rows will be deleted.

    Returns:
    tuple: A message indicating the result of the operation and the HTTP status code.
    """
    try:
        delete_query = text(f'DELETE FROM {table_name}')

        with engine.connect() as connection:
            trans = connection.begin()
            connection.execute(delete_query)
            trans.commit()

        return {"message": f"All rows deleted from '{table_name}'"}, 200

    except Exception as e:
        return {"error": str(e)}, 500
