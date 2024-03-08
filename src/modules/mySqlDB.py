import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

class MySQLDB:
    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        """Connect to the MySQL database."""
        try:
            connection = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST", "localhost"),
                port=int(os.getenv("MYSQL_PORT", "3306")),
                user=os.getenv("MYSQL_USER", "root"),
                password=os.getenv("MYSQL_PASSWORD", ""),
                database=os.getenv("MYSQL_DB", "test")
            )
            if connection.is_connected():
                db_info = connection.get_server_info()
                print(f"Connected to MySQL Server version {db_info}")
                return connection
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            return None

    def execute_query(self, query, params=None):
        """Execute a query (insert, update, delete)."""
        if self.connection:
            cursor = self.connection.cursor()
            try:
                cursor.execute(query, params)
                self.connection.commit()
                print("Query executed successfully")
            except Error as e:
                print(f"Failed to execute query: {e}")
            finally:
                cursor.close()

    def fetch_data(self, query, params=None):
        """Fetch data from the database."""
        if self.connection:
            cursor = self.connection.cursor(dictionary=True)
            try:
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result
            except Error as e:
                print(f"Failed to fetch data: {e}")
                return []
            finally:
                cursor.close()