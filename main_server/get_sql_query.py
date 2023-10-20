def get_sql_query(file_directory):
    with open(file_directory, 'r') as file:
        return file.read()