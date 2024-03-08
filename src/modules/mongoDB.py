from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class MongoDB:
    def __init__(self, uri=os.getenv("MONGODB_URI", "mongodb://localhost:27017"), db_name=os.getenv("MONGODB_DB_NAME", "mydatabase")):
        self.client = None
        self.db_name = db_name
        self.uri = uri
        self.connect()

    def connect(self):
        """Connect to the MongoDB server."""
        try:
            self.client = MongoClient(self.uri)
            self.client.admin.command('ping')  # Ping the server to test connection
            print("Connected to MongoDB")
        except ConnectionFailure:
            print("Failed to connect to MongoDB")
            self.client = None

    def get_database(self):
        """Get the database object."""
        if self.client:
            return self.client[self.db_name]
        else:
            print("Not connected to MongoDB")
            return None

    def save_data(self, collection_name, data):
        """Save data to a specified collection."""
        if self.client:
            db = self.get_database()
            collection = db[collection_name]
            result = collection.insert_one(data)
            print(f"Data inserted with record id {result.inserted_id}")
        else:
            print("Not connected to MongoDB")

    def query_data(self, collection_name, query):
        """Query data from a specified collection."""
        if self.client:
            db = self.get_database()
            collection = db[collection_name]
            documents = collection.find(query)
            return list(documents)
        else:
            print("Not connected to MongoDB")
            return []

# Example usage
if __name__ == "__main__":
    mongo_db = MongoDB()  # Environment variables are now used by default
    
    # Example to save data
    mongo_db.save_data("test_collection", {"name": "John", "age": 30})

    # Example to query data
    results = mongo_db.query_data("test_collection", {"name": "John"})
    for doc in results:
        print(doc)
