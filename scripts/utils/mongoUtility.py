from pymongo import MongoClient

from scripts.constants import app_configuration
from scripts.logging.log_module import logger as log


class MongoDBUtility:
    def __init__(self, uri):
        try:
            self.uri = uri
            self.client = MongoClient(self.uri, connect=False)
        except Exception as e:
            log.exception(str(e))
            raise

    # def __init__(self, database_name, collection_name):
    #     """
    #     Initialize the MongoDB utility.
    #     """
    #     try:
    #         # Connect to MongoDB
    #         self.client = MongoClient(app_configuration.MONGO_HOST)
    #         self.db = self.client[database_name]
    #         self.collection = self.db[collection_name]
    #         log.info(f"Connected to database: {database_name}, collection: {collection_name}")
    #     except Exception as e:
    #         print(f"Failed to connect to MongoDB: {e}")
    #         raise

    def insert_record(self, record,database,collection):
        """
        Insert a single record into the collection.
        """
        try:
            database_name = database
            collection_name = collection
            db = self.client[database_name]
            collection = db[collection_name]
            result = collection.insert_one(record)
            return True
        except Exception as e:
            print(f"Failed to insert record: {e}")
            return False

    def fetch_records(self, database,collection,query=None):
        """
        Fetch records from the collection based on a query.
        If no query is provided, fetch all records.
        """
        records = []
        try:
            query = query or {}  # Default to fetching all records
            database_name = database
            collection_name = collection
            db = self.client[database_name]
            collection = db[collection_name]
            records = collection.find(query)

        except Exception as e:
            print(f"Failed to fetch records: {e}")
        return list(records)

    def update_records(self, query, update_values,database,collection):
        """
        Update records in the collection based on a query.
        """
        try:
            database_name = database
            collection_name = collection
            db = self.client[database_name]
            collection = db[collection_name]
            result = collection.update_many(query, {"$set": update_values})
            print(f"{result.matched_count} record(s) matched. {result.modified_count} record(s) updated.")
        except Exception as e:
            print(f"Failed to update records: {e}")

    def update_one_record(self, filter_query, updated_values,database,collection):
        """
               Update one record in the collection based on a query.
        """
        try:
            database_name = database
            collection_name = collection
            db = self.client[database_name]
            collection = db[collection_name]
            result = collection.update_one(filter_query, updated_values)
        except Exception as e:
            log.info("")

    def delete_records(self, query,database,collection):
        """
        Delete records from the collection based on a query.
        """
        try:
            database_name = database
            collection_name = collection
            db = self.client[database_name]
            collection = db[collection_name]
            result = collection.delete_many(query)
            print(f"{result.deleted_count} record(s) deleted.")
        except Exception as e:
            print(f"Failed to delete records: {e}")

    def close_connection(self):
        """
        Close the MongoDB connection.
        """
        self.client.close()
        print("MongoDB connection closed.")
