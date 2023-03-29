#!/usr/bin/env python

import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Set up the database connection
db_credentials = {}
with open('dbcredentials.env', 'r') as f:
    for line in f:
        key, value = line.strip().split('=')
        db_credentials[key] = value

db_uri = f"postgresql://{db_credentials['POSTGRES_USER']}:{db_credentials['POSTGRES_PASSWORD']}@my_pgdb:5432/{db_credentials['POSTGRES_DB']}"
engine = create_engine(db_uri)

# Read CSV files from the folder
csv_folder = './InstaCart-Online-Grocery-Basket-Analysis-Dataset'
for file in os.listdir(csv_folder):
    if file.endswith('.csv'):
        # Read the CSV file into a DataFrame
        file_path = os.path.join(csv_folder, file)
        df = pd.read_csv(file_path)

        # Generate the table name from the CSV file name
        table_name = os.path.splitext(file)[0]

        # Create the table and import data into PostgreSQL
        df.to_sql(table_name, engine, if_exists='replace', index=False, method='multi')
