from datetime import datetime
import json
import time
from scripts.constants import app_configuration, app_constants
from scripts.logging.log_module import logger as log
from scripts.utils.mongoUtility import MongoDBUtility
from pywebpush import webpush, WebPushException

mongo_obj = MongoDBUtility(uri=app_configuration.MONGO_HOST)


class UserManagement:

    def __int__(self):
        print("Initialising")
        # self.mongo_obj = Mongo_DBUtility(app_configuration.MONGO_DATABASE, app_configuration.MONGO_COLLECTION)

    def add_user(self, request_data):
        # columns = ["username", "email", "phone_number", "user_type", "created_at", "updated_at",
        #            "status", "last_login","failed_attempts"]
        json_object = {'status': 'failed', 'message': 'Error Occurred while saving data'}
        try:
            mongo_query = {'userName': request_data['userName']}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_COLLECTION)
            if data:
                json_object["message"] = "UserName Already exists. Kindly try with different userName"
                json_object['status'] = 'info'
            else:
                createdAt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                request_data['createdAt'] = createdAt
                request_data['userStatus'] = 'Active'
                request_data['failedAttempts'] = 0
                status = mongo_obj.insert_record(request_data, database=app_configuration.MONGO_DATABASE,
                                                 collection=app_configuration.MONGO_COLLECTION)
                if status:
                    json_object['message'] = 'Successfully created an account'
                    json_object['status'] = 'success'
        except Exception as e:
            log.error(f"Error occurred while adding user due to {e}. Kindly try after sometime")

        return json_object

    def login_user(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while validating data','data':{}}
        try:
            user_name = request_data['userName']
            password = request_data['password']
            mongo_query = {'userName': user_name, "password": password, 'userStatus': 'Active',
                           "failedAttempts": {"$lte": 3}}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_COLLECTION)
            if data:
                mongo_data = data[0]
                update_operation = {"$set": {"failedAttempts": 0}}
                mongo_data['failedAttempts'] = 0
                mongo_obj.update_one_record({'userName': user_name}, update_operation,
                                            database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.MONGO_COLLECTION)
                json_object['status'] = 'success'
                json_object['message'] = 'User logged in successfully'
                json_object['data']['userName'] = mongo_data['userName']
                json_object['data']['userType'] = mongo_data['userType']
                json_object['data']['eMail'] = mongo_data['eMail']
                return json_object
            user_inactive_query = {'userName': user_name, "password": password, 'userStatus': 'InActive'}
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
                if mongo_user_data['failedAttempts'] > 3:
                    json_object['status'] = 'failed'
                    json_object['message'] = 'User account locked. Kindly ask admin to unblock user'
                elif password != mongo_user_data['password']:
                    mongo_user_data["failedAttempts"] = mongo_user_data['failedAttempts'] + 1
                    update_operation = {"$set": {"failedAttempts": mongo_user_data['failedAttempts'] + 1}}
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
            update_operation = {"$set": {"userStatus": "Active"}}
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
            update_operation = {"$set": {"userStatus": "InActive"}}
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

    def disease_list(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching diseases data','data':[]}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.DISEASES_COLLECTION)
            if data:
                for each_data in data:
                    del each_data['_id']
                    json_object['data'].append(each_data)
                json_object['status'] = 'success'
                json_object['message'] = 'Disease list fetched successfully'
            else:
                json_object['status']='failed'
                json_object['message']='Unable to fetch diseases list'

        except Exception as e:
            log.error(f"Error occurred while fetching diseases list due to {e}. Kindly try after sometime")
        return json_object


    def market_trends(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching diseases data','data':{'date':[],'seriesData':[]}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.BIRD_PRICE_COLLECTION)
            if data:
                for each_data in data:
                    json_object['data']['date'].append(each_data['date'])
                    json_object['data']['seriesData'].append(each_data['birdsPrice'])
                json_object['status'] = 'success'
                json_object['message'] = 'Disease list fetched successfully'
            else:
                json_object['status']='failed'
                json_object['message']='Unable to fetch diseases list'

        except Exception as e:
            log.error(f"Error occurred while fetching diseases list due to {e}. Kindly try after sometime")
        return json_object


    def customer_wise_sales_trends(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching diseases data','data':{'date':[],'seriesData':[]}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.BIRD_PRICE_COLLECTION)
            if data:
                for each_data in data:
                    json_object['data']['date'].append(each_data['date'])
                    json_object['data']['seriesData'].append(each_data['birdsPrice'])
                json_object['status'] = 'success'
                json_object['message'] = 'Birds price fetched successfully'
            else:
                json_object['status']='failed'
                json_object['message']='Unable to fetch diseases list'

        except Exception as e:
            log.error(f"Error occurred while fetching diseases list due to {e}. Kindly try after sometime")
        return json_object


    def chick_trends(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching diseases data','data':{'date':[],'seriesData':[]}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.CHICK_PRICE_COLLECTION)
            if data:
                for each_data in data:
                    json_object['data']['date'].append(each_data['date'])
                    json_object['data']['seriesData'].append(each_data['chickPrice'])
                json_object['status'] = 'success'
                json_object['message'] = 'Chick Prices fetched successfully'
            else:
                json_object['status']='failed'
                json_object['message']='Unable to fetch diseases list'

        except Exception as e:
            log.error(f"Error occurred while fetching diseases list due to {e}. Kindly try after sometime")
        return json_object

    def unblock_user(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while saving data'}
        try:
            mongo_query = {'userName': request_data['data']['userName']}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_COLLECTION)
            if data :
                update_operation = {"$set": {"failedAttempts": 0}}
                mongo_obj.update_one_record({'userName':request_data['data']['userName']}, update_operation,
                                            database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.MONGO_COLLECTION)
            json_object['status']= 'success'
            json_object['message']= 'User unblocked successfully'
        except Exception as e:
            log.error(f"Error occurred while adding user due to {e}. Kindly try after sometime")

        return json_object

    def get_user_role_data(self):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching data','data':{}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.USER_ACCESS_COLLECTION)
            json_object['data']=data[0]['accessData']
            json_object['status']= 'success'
            json_object['message']= 'User unblocked successfully'
        except Exception as e:
            log.error(f"Error occurred while adding user due to {e}. Kindly try after sometime")
        return json_object

    def set_user_role_data(self,request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching data'}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.USER_ACCESS_COLLECTION)
            if data :
                update_operation = {"$set": {f"accessData.{request_data['key']}": request_data[request_data['key']]}}
                mongo_obj.update_one_record({"_id":data[0]["_id"]},update_operation,
                                            database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.USER_ACCESS_COLLECTION)
            json_object['status']= 'success'
            json_object['message']= 'Data updated successfully'
        except Exception as e:
            log.error(f"Error occurred while adding user due to {e}. Kindly try after sometime")
        return json_object

    def store_subscription(self,request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching data'}
        try:
            mongo_query = {'userName': request_data['userName']}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.SUBSCRIPTIONS)
            if data:
                update_operation = {
                    "$push": {
                        "subscription": request_data["subscription"]
                        }
                }
                mongo_obj.update_one_record({'userName':request_data['userName']}, update_operation,
                                            database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.SUBSCRIPTIONS)
                json_object['message'] = 'Successfully subscribed'
                json_object['status'] = 'success'
            else:
                subscription = {
                    'userName': request_data['userName'],
                    'subscription':[request_data['subscription']]
                }
                status = mongo_obj.insert_record(subscription, database=app_configuration.MONGO_DATABASE,
                                                 collection=app_configuration.SUBSCRIPTIONS)
                if status:
                    json_object['message'] = 'Successfully subscribed'
                    json_object['status'] = 'success'
        except Exception as e:
            log.error(f"Error occurred while adding subscription due to {e}. Kindly try after sometime")

        return json_object

    def push_notify(self,request_data):
        try:
            data = mongo_obj.fetch_records(query={},database=app_configuration.MONGO_DATABASE,collection=app_configuration.SUBSCRIPTIONS)
            if not data:
                return
            payload = json.dumps({
                "title": request_data['notificationData']['title'],
                "body": request_data['notificationData']['message']
            })
            for each_data in data:
                for subscription_info in each_data['subscription']:
                    self.send_push_with_retry(subscription_info, payload)
        except Exception as e:
            log.error(f"Background push error: {e}")

    def send_push_with_retry(self, subscription_info, payload, retries=4):
        for attempt in range(retries):
            try:
                webpush(
                    subscription_info=subscription_info,
                    data=payload,
                    vapid_private_key=app_constants.VAPID_PRIVATE_KEY,
                    vapid_claims=app_constants.VAPID_CLAIMS
                )
                return True

            except WebPushException as exc:
                status = exc.response.status_code
                log.error(f"WebPush error ({status}) on attempt {attempt + 1}: {exc}")
                # Handle expired subscription
                if status in [404, 410]:
                    self.remove_subscription(subscription_info)
                    return False
                # Handle rate limits or temporary failure
                if status in [429, 503]:
                    time.sleep(1)
                    continue
                else:
                    return False
            except Exception as e:
                log.error(f"Unexpected push error: {e}")
                time.sleep(1)
                continue
        return False

    def remove_subscription(self, subscription_info):
        try:
            mongo_obj.update_records(
                query={"subscription": {"$elemMatch": {"endpoint": subscription_info["endpoint"]}}},
                update_values={"$pull": {"subscription": {"endpoint": subscription_info["endpoint"]}}},
                database=app_configuration.MONGO_DATABASE,
                collection=app_configuration.SUBSCRIPTIONS
            )
            log.info(f"Removed expired subscription: {subscription_info['endpoint']}")
        except Exception as e:
            log.error(f"Error removing expired subscription: {e}")