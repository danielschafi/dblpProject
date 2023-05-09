import psycopg2

# connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="dblp",
    user="postgres",
    password="1234"
)

# create a cursor object
cursor = conn.cursor()

# execute the SQL query to close all open connections
cursor.execute("""
    SELECT pg_terminate_backend(pg_stat_activity.pid)
    FROM pg_stat_activity
    WHERE pg_stat_activity.datname = 'dblp'
      AND pid <> pg_backend_pid();
""")

# commit the changes and close the cursor and connection
conn.commit()


# drop the dblp database
cursor.execute("DROP DATABASE IF EXISTS dblp")

# commit the changes
conn.commit()

# create a cursor object
cursor = conn.cursor()

# execute the SQL code from file
with open("createDBLP.sql", "r") as f:
    cursor.execute(f.read())

# commit the changes and close the cursor and connection to the dblp database
conn.commit()
cursor.close()
conn.close()