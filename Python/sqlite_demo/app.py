# Connect SQLite Database
import sqlite3
import pandas as pd

# Step 1: Connect to SQLite file
database = 'database.sqlite'
conn = sqlite3.connect(database)
print("Opened database successfully")

# Step 2: Read list of all tables
tables = pd.read_sql("""
SELECT name FROM sqlite_master
WHERE type='table';
""", conn)

print("Tables in Database:")
print(tables)

#Step 3: Read a table (example table name: students)
df = pd.read_sql("SELECT * FROM students", conn)
print(df)
