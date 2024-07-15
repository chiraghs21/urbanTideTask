import pandas as pd
from sqlalchemy import Table, Column, Integer, String, Float, MetaData
from app.db import engine, metadata

def detect_outliers(df):
    # Simple outlier detection using IQR
    Q1 = df['value'].quantile(0.25)
    Q3 = df['value'].quantile(0.75)
    IQR = Q3 - Q1
    filter = (df['value'] >= (Q1 - 1.5 * IQR)) & (df['value'] <= (Q3 + 1.5 * IQR))
    return not all(filter)

def create_table(df, table_name):
    # Infer schema and create table
    columns = [Column('timestamp', String), Column('value', Float), Column('category', String)]
    table = Table(table_name, metadata, *columns, extend_existing=True)
    metadata.create_all(engine)

def insert_data(df, table_name):
    df.to_sql(table_name, engine, if_exists='append', index=False)
