import psycopg2

def get_sql_query(file_directory):
    with open(file_directory, 'r') as file:
        return file.read()
    

def connect_to_postgres():
    conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='postgres',
    host='localhost', 
    port='5432')
    return conn