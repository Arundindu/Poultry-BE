from scripts.constants import app_configuration
from scripts.logging.log_module import logger as log
from scripts.utils.mongoUtility import MongoDBUtility

mongo_obj = MongoDBUtility(uri=app_configuration.MONGO_HOST)


class TabManagement:

    def __int__(self):
        print("Initalising")
        # self.mongo_obj = Mongo_DBUtility(app_configuration.MONGO_DATABASE, app_configuration.MONGO_COLLECTION)

    def add_tab(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while adding tab data'}
        try:
            mongo_query = {'tab_name': 'setting_tab'}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_COLLECTION)
            if data:
                mongo_data = data[0]['tab_data']
                for each_data in request_data['tabs']:
                    mongo_data.append(each_data)
                update_operation = {"$set": {"tab_data": mongo_data}}
                mongo_obj.update_one_record(mongo_query, update_operation, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.MONGO_TAB_COLLECTION)
                json_object['status'] = 'success'
                json_object['message'] = 'Tab Details Saved Successfully'
            else:
                data = {'tab_data': [], 'tab_name': 'setting_tab'}
                for each_data in request_data['tabs']:
                    data['tab_data'].append(each_data)
                mongo_obj.insert_record(data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.MONGO_TAB_COLLECTION)
                json_object['status'] = 'success'
                json_object['message'] = 'Tab Details Saved Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def fetch_settings_tab_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data', 'tabData': []}
        try:
            mongo_query = {'tab_name': 'setting_tab'}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_COLLECTION)
            if data:
                mongo_data = data[0]['tab_data']
                for each_data in mongo_data:
                    json_object['tabData'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Tab Details fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def fetch_settings_tab_header_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data', 'tabData': []}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            if data:
                mongo_data = data[0][request_data['tabName']]
                for each_data in mongo_data:
                    json_object['tabData'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Tab Details fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def save_bird_price_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data', 'tabData': []}
        try:
            mongo_query = {"$and": [{"userName": request_data["userName"]}, {"date": request_data["data"]["date"]}]}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.BIRD_PRICE_COLLECTION)
            if data:
                mongo_data = data[0]
                mongo_data["price"] = request_data["data"]["price"]
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.BIRD_PRICE_COLLECTION)
            else:
                mongo_data = {"userName": request_data["userName"],
                              "date": request_data["data"]["date"],
                              "price": request_data["data"]["price"]}
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.BIRD_PRICE_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Tab Details Saved Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object