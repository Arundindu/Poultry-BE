from datetime import datetime

from scripts.constants import app_configuration
from scripts.logging.log_module import logger as log
from scripts.utils.mongoUtility import MongoDBUtility

mongo_obj = MongoDBUtility(uri=app_configuration.MONGO_HOST)


class UserManagement:

    def __int__(self):
        print("Initalising")
        # self.mongo_obj = Mongo_DBUtility(app_configuration.MONGO_DATABASE, app_configuration.MONGO_COLLECTION)

    def add_user(self, request_data):
        # columns = ["username", "email", "phone_number", "user_type", "created_at", "updated_at",
        #            "status", "last_login",'failed_attempts"]
        json_object = {'status': 'failed', 'message': 'Error Occurred while saving data'}
        try:
            mongo_query = {'userName': request_data['userName']}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_COLLECTION)
            if data:
                json_object["message"] = "UserName Already exists. Kindly try with different userName"
                json_object['status'] = 'info'
            else:
                created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                request_data['created_at'] = created_at
                request_data['user_status'] = 'Active'
                request_data['failed_attempts'] = 0
                status = mongo_obj.insert_record(request_data, database=app_configuration.MONGO_DATABASE,
                                                 collection=app_configuration.MONGO_COLLECTION)
                if status:
                    json_object['message'] = 'Successfully created an account'
                    json_object['status'] = 'success'
        except Exception as e:
            log.error(f"Error occurred while adding user due to {e}. Kindly try after sometime")

        return json_object

    def login_user(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while validating data'}
        try:
            user_name = request_data['userName']
            password = request_data['password']
            mongo_query = {'userName': user_name, "password": password, 'user_status': 'Active',
                           "failed_attempts": {"$lte": 3}}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_COLLECTION)
            if data:
                mongo_data = data[0]
                update_operation = {"$set": {"failed_attempts": 0}}
                mongo_data['failed_attempts'] = 0
                mongo_obj.update_one_record({'userName': user_name}, update_operation,
                                            database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.MONGO_COLLECTION)
                json_object['status'] = 'success'
                json_object['message'] = 'User logged in successfully'
                return json_object
            user_inactive_query = {'userName': user_name, "password": password, 'user_status': 'InActive'}
            inactive_user_data = mongo_obj.fetch_records(query=user_inactive_query,
                                                         database=app_configuration.MONGO_DATABASE,
                                                         collection=app_configuration.MONGO_COLLECTION)
            if inactive_user_data:
                json_object['status'] = 'InActive'
                json_object['message'] = 'Kindly activate the user'
                return json_object

            user_data = {'userName': user_name}
            mongo_user_data = mongo_obj.fetch_records(query=user_data, database=app_configuration.MONGO_DATABASE,
                                                      collection=app_configuration.MONGO_COLLECTION)
            if mongo_user_data:
                mongo_user_data = mongo_user_data[0]
                if mongo_user_data['failed_attempts'] > 3:
                    json_object['status'] = 'failed'
                    json_object['message'] = 'User account locked. Kindly ask admin to unblock user'
                elif password != mongo_user_data['password']:
                    mongo_user_data["failed_attempts"] = mongo_user_data['failed_attempts'] + 1
                    update_operation = {"$set": {"failed_attempts": mongo_user_data['failed_attempts'] + 1}}
                    mongo_obj.update_one_record({'userName': user_name}, update_operation,
                                                database=app_configuration.MONGO_DATABASE,
                                                collection=app_configuration.MONGO_COLLECTION)
                    json_object['status'] = 'failed'
                    json_object['message'] = 'Incorrect User Name or Password'
                    return json_object
            else:
                json_object['status'] = 'failed'
                json_object['message'] = 'No User found with the mentioned User Name'
                return json_object
        except Exception as e:
            log.error(f"Error occurred while logging to the portal due to {e}. Kindly try after sometime")
        return json_object

    def activate_user(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while activating user data'}
        try:
            user_name = request_data['userName']
            update_operation = {"$set": {"user_status": "Active"}}
            mongo_obj.update_one_record({'userName': user_name}, update_operation,
                                        database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.MONGO_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'User Activated successfully'
        except Exception as e:
            log.error(f"Error occurred while logging to the portal due to {e}. Kindly try after sometime")
        return json_object

    def de_activate_user(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while De-Activating user'}
        try:
            user_name = request_data['userName']
            update_operation = {"$set": {"user_status": "InActive"}}
            mongo_obj.update_one_record({'userName': user_name}, update_operation,
                                        database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.MONGO_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'User De-Activated successfully'
        except Exception as e:
            log.error(f"Error occurred while De-Activating the user due to {e}. Kindly try after sometime")
        return json_object

    def delete_user(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while deleting user data'}
        try:
            user_name = request_data['userName']
            mongo_operation = {'userName': user_name}
            mongo_obj.delete_records(mongo_operation, database=app_configuration.MONGO_DATABASE,
                                     collection=app_configuration.MONGO_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'User Deleted successfully'
        except Exception as e:
            log.error(f"Error occurred while deleting the user due to {e}. Kindly try after sometime")
        return json_object
