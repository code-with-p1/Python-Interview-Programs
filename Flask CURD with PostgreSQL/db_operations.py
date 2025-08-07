import psycopg2
from psycopg2 import Error

# Function to establish connection with the PostgreSQL database
def connect():
    try:
        timeout = 30
        # Connect to an existing database
        connection = psycopg2.connect(
            user="postgres",
            password="1234",
            host="172.23.0.3",
            port="5432",
            database="postgres",
            application_name='local',
            options=f"-c statement_timeout={timeout}s",
        )
        return connection, connection.cursor()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None, None

# Function to create a table
def create_table(cursor):
    try:
        create_table_query = '''CREATE TABLE IF NOT EXISTS users
            (id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL); '''
        cursor.execute(create_table_query)
        cursor.connection.commit()
        print("Table created successfully in PostgreSQL ")
    except (Exception, Error) as error:
        print("Error while creating PostgreSQL table", error)

# Function to insert data into the table
def create_user(cursor, name, email):
    try:
        insert_query = '''INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id'''
        cursor.execute(insert_query, (name, email))
        user_id = cursor.fetchone()[0]
        cursor.connection.commit()
        print(f"User with ID {user_id} inserted successfully.")
    except (Exception, Error) as error:
        print("Error while inserting data into PostgreSQL", error)

# Function to read data from the table
def read_users(cursor):
    try:
        select_query = '''SELECT * FROM users ORDER BY ID ASC'''
        cursor.execute(select_query)
        users = cursor.fetchall()
        return users
    except (Exception, Error) as error:
        print("Error while reading data from PostgreSQL", error)

# Function to update data in the table
def update_user(cursor, user_id, new_name, new_email):
    try:
        update_query = '''UPDATE users SET name = %s, email = %s WHERE id = %s'''
        cursor.execute(update_query, (new_name, new_email, user_id))
        cursor.connection.commit()
        print("User updated successfully.")
    except (Exception, Error) as error:
        print("Error while updating data in PostgreSQL", error)

# Function to delete data from the table
def delete_user(cursor, user_id):
    try:
        delete_query = '''DELETE FROM users WHERE id = %s'''
        cursor.execute(delete_query, (user_id,))
        cursor.connection.commit()
        print("User deleted successfully.")
    except (Exception, Error) as error:
        print("Error while deleting data from PostgreSQL", error)

# Uncomment the functions you want to test
if __name__ == "__main__":
    # This command is used to get hostname as IPAddress to make connection with container postgresql db
    # sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' d7fa7dfaba95

    # Create connection and cursor object 
    connection, cursor = connect()
    print()

    # Create Table Query
    create_table(cursor)
    print()

    # Create User Query
    create_user(cursor, "John Doe", "john@example.com")
    print()

    # Get User Datails Query
    read_users(cursor)
    print()

    # Update User Data Query
    update_user(cursor, 1, "Jane Doe", "jane@example.com")
    print()

    # Delete User
    delete_user(cursor, 1)
    print()

    # Closing Connection & Cursor
    cursor.close()
    connection.close()