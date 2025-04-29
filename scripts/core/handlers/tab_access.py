from scripts.constants import app_configuration
from scripts.constants import app_constants
from scripts.logging.log_module import logger as log
from scripts.utils.mongoUtility import MongoDBUtility
from datetime import datetime

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
            user_list = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_COLLECTION)
            shed_list = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.SHEDS_COLLECTION)
            users = []
            sheds = []
            for each_data in user_list:
                users.append({'value':each_data['userName'],'label':each_data['userName']})
            for each_data in shed_list:
                sheds.append({'value':each_data['shedName'],'label':each_data['shedName']})
            if data:
                mongo_data = data[0][request_data['tabName']]
                for each_data in mongo_data:
                    json_object['tabData'].append(each_data)
            if(request_data['tabName'] == 'sales'):
                for each_data in mongo_data:
                    if each_data['key'] == 'userName':
                        each_data['options'].extend(users)
                    if each_data['key'] == 'shedName':
                        each_data['options'].extend(sheds)
            if(request_data['tabName'] == 'feedConsumption'):
                for each_data in mongo_data:
                    if each_data['key'] == 'shedName':
                        each_data['options'].extend(sheds)
            if(request_data['tabName'] == 'orderHens'):
                for each_data in mongo_data:
                    if each_data['key'] == 'userName':
                        each_data['options'].extend(users)
            if (request_data['tabName'] == 'mortality'):
                for each_data in mongo_data:
                    if each_data['key'] == 'shedName':
                        each_data['options'].extend(sheds)
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
                mongo_data = {"$set": {"birdsPrice":request_data["data"]["birdsPrice"]}}
                mongo_query = {"_id":data[0]["_id"]} 
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.BIRD_PRICE_COLLECTION)
            else:
                mongo_data = {"userName": request_data["userName"],
                              "date": request_data["data"]["date"],
                              "birdsPrice": request_data["data"]["birdsPrice"]}
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.BIRD_PRICE_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Tab Details Saved Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def save_hens_availability_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data', 'tabData': []}
        try:
            mongo_query = {"$and": [{"userName": request_data["userName"]}, {"date": request_data["data"]["date"]}]}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.HENS_AVAILABILITY_COLLECTION)
            if data:
                mongo_query = {"_id": data[0]["_id"]}
                mongo_data = {"$set":{"availableHens":request_data["data"]["availableHens"]}}
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.HENS_AVAILABILITY_COLLECTION)
            else:
                mongo_data = {"userName": request_data["userName"],
                              "date": request_data["data"]["date"],
                              "availableHens": request_data["data"]["availableHens"]}
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.HENS_AVAILABILITY_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Hens Availability Data Saved Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def sheds_availability_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data', 'tabData': []}
        try:
            mongo_query = {"$and": [{"userName": request_data["userName"]}, {"openingDate": request_data["data"]["openingDate"]}]}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.SHEDS_COLLECTION)
            if data:
                mongo_query = {"_id": data[0]["_id"]}
                mongo_data = {"$set":{"shedName":request_data["data"]["shedName"]}}
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.SHEDS_COLLECTION)
            else:
                mongo_data = {"userName": request_data["userName"],
                              "openingDate": request_data["data"]["openingDate"],
                              "shedName": request_data["data"]["shedName"]}
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.SHEDS_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Shed Data Saved Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def feed_consumption_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data', 'tabData': []}
        try:
            mongo_query = {
                "$and": [{"userName": request_data["userName"]}, {"batchNo": request_data["data"]["batchNo"]}]}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.FEED_CONSUMPTION_COLLECTION)
            if data:
                mongo_query = {"_id": data[0]["_id"]}
                mongo_data = {"$set": {"feedConsumed": request_data["data"]["feedConsumed"]}}
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.FEED_CONSUMPTION_COLLECTION)
            else:
                mongo_data = {"userName": request_data["userName"],
                              "batchNo": request_data["data"]["batchNo"],
                              "shedNo": request_data["data"]["shedNo"],
                              "feedType": request_data["data"]["feedType"],
                              "feedConsumed": request_data["data"]["feedConsumed"]}
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.FEED_CONSUMPTION_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Feed Consumption Data Saved Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def sheds_table_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching table data','tableData':{'headerContent':[],'bodyContent':[]}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.SHEDS_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['shedsTableContent']['headerContent'])
            json_object['tableData']['actions'] = (header[0]['shedsTableContent']['actions'])
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    del each_data['_id']
                    json_object['tableData']['bodyContent'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Tab Details fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def feed_consumption_table_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching table data','tableData':{'headerContent':[],'bodyContent':[],'actions':{}}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.FEED_CONSUMPTION_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['feedConsumptionTableContent']['headerContent'])
            json_object['tableData']['actions']=(header[0]['feedConsumptionTableContent']['actions'])
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    del each_data['_id']
                    json_object['tableData']['bodyContent'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Tab Details fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def user_setup_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while saving data'}
        try:
            mongo_query = {'userName': request_data['data']['userName']}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_COLLECTION)
            if data:
                json_object["message"] = "UserName Already exists. Kindly try with different userName"
                json_object['status'] = 'info'
            else:
                createdAt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                request_data['data']['createdAt'] = createdAt
                request_data['data']['userStatus'] = 'Active'
                request_data['data']['failedAttempts'] = 0
                request_data['data']['userType'] = request_data['data']['userType'].capitalize()
                status = mongo_obj.insert_record(request_data['data'], database=app_configuration.MONGO_DATABASE,
                                                 collection=app_configuration.MONGO_COLLECTION)
                if status:
                    json_object['message'] = 'User details added successfully'
                    json_object['status'] = 'success'
        except Exception as e:
            log.error(f"Error occurred while adding user due to {e}. Kindly try after sometime")

        return json_object

    def user_setup_table_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching table data','tableData':{'headerContent':[],'bodyContent':[],'actions':{}}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['userSetupTableContent']['headerContent'])
            json_object['tableData']['actions']=(header[0]['userSetupTableContent']['actions'])
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    del each_data['_id']
                    json_object['tableData']['bodyContent'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Table data fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def order_hens_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error occurred while adding order details'}
        try:
            mongo_query = {
                "$and": [{"userName": request_data["userName"]}]}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.ORDER_HENS_COLLECTION)
            if data:
                mongo_query = {"_id": data[0]["_id"]}
                mongo_data = {"$set": {"feedConsumed": request_data["data"]["feedConsumed"]}}
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.ORDER_HENS_COLLECTION)
            else:
                mongo_data = {"userName": request_data["userName"],
                              "batchNo": request_data["data"]["batchNo"],
                              "shedNo": request_data["data"]["shedNo"],
                              "feedType": request_data["data"]["feedType"],
                              "feedConsumed": request_data["data"]["feedConsumed"]}
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.ORDER_HENS_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Order details added successfully'
        except Exception as e:
            log.error("Error occurred while adding order details due to " + str(e))
        return json_object

    def sales_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data'}
        try:
            mongo_query = {
                "$and": [{"userName": request_data["userName"]}, {"userName": request_data["data"]["userName"]},{"date": request_data["data"]["date"]}]}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.SALES_COLLECTION)
            if data:
                mongo_query = {"_id": data[0]["_id"]}
                mongo_data = {"$set": {"userName": request_data["data"]["userName"]}}
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.SALES_COLLECTION)
            else:
                mongo_data = {"date": request_data["data"]["date"],
                              "noOfHens": request_data["data"]["noOfHens"],
                              "userName": request_data["data"]["userName"],
                              "batchNo": request_data["data"]["batchNo"],
                              "shedName": request_data["data"]["shedName"],
                              "noOfKgs": request_data["data"]["noOfKgs"],
                              "amount": request_data["data"]["amount"],
                              }
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.SALES_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Sales Data Saved Successfully'
        except Exception as e:
            log.error("Error occurred while adding sales data due to " + str(e))
        return json_object

    def sales_table_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching table data','tableData':{'headerContent':[],'bodyContent':[],'actions':{}}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.SALES_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['salesTableContent']['headerContent'])
            json_object['tableData']['actions']=(header[0]['salesTableContent']['actions'])
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    del each_data['_id']
                    json_object['tableData']['bodyContent'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Table data fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def order_hens_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data'}
        try:
            mongo_query = {
                "$and": [{"userName": request_data["userName"]}, {"userName": request_data["data"]["userName"]},{"date": request_data["data"]["date"]}]}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.SALES_COLLECTION)
            if data:
                mongo_query = {"_id": data[0]["_id"]}
                mongo_data = {"$set": {"userName": request_data["data"]["userName"]}}
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.ORDER_HENS_COLLECTION)
            else:
                mongo_data = {"date": request_data["data"]["date"],
                              "noOfHens": request_data["data"]["noOfHens"],
                              "userName": request_data["data"]["userName"]
                              }
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.ORDER_HENS_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Order details Saved Successfully'
        except Exception as e:
            log.error("Error occurred while adding orders data due to " + str(e))
        return json_object

    def order_hens_table_data(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching table data','tableData':{'headerContent':[],'bodyContent':[],'actions':{}}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.ORDER_HENS_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['orderHensTableContent']['headerContent'])
            json_object['tableData']['actions']=(header[0]['orderHensTableContent']['actions'])
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    del each_data['_id']
                    json_object['tableData']['bodyContent'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Table data fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def birds_price_table(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching table data','tableData':{'headerContent':[],'bodyContent':[],'actions':{}}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.BIRD_PRICE_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['birdsPriceTableContent']['headerContent'])
            json_object['tableData']['actions']=(header[0]['birdsPriceTableContent']['actions'])
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    del each_data['_id']
                    json_object['tableData']['bodyContent'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Table data fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def chick_price(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data'}
        try:
            mongo_query = {
                "$and": [{"userName": request_data["userName"]}, {"chickPrice": request_data["data"]["chickPrice"]},{"date": request_data["data"]["date"]}]}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.CHICK_PRICE_COLLECTION)
            if data:
                mongo_query = {"_id": data[0]["_id"]}
                mongo_data = {"$set": {"chickPrice": request_data["data"]["chickPrice"]}}
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.CHICK_PRICE_COLLECTION)
            else:
                mongo_data = {"date": request_data["data"]["date"],
                              "chickPrice": request_data["data"]["chickPrice"]
                              }
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.CHICK_PRICE_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Chick Price Saved Successfully'
        except Exception as e:
            log.error("Error occurred while adding chick price data due to " + str(e))
        return json_object

    def chick_price_table(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching table data','tableData':{'headerContent':[],'bodyContent':[],'actions':{}}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.CHICK_PRICE_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['chickPriceTableContent']['headerContent'])
            json_object['tableData']['actions']=(header[0]['chickPriceTableContent']['actions'])
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    del each_data['_id']
                    json_object['tableData']['bodyContent'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Table data fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def mortality(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data'}
        try:
            mongo_query = {
                "$and": [{"userName": request_data["userName"]}, {"batchNo": request_data["data"]["batchNo"]},{"date": request_data["data"]["date"]},{"shedName": request_data["data"]["shedName"]},{"mortality": request_data["data"]["mortality"]}]}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MORTALITY_COLLECTION)
            if data:
                mongo_query = {"_id": data[0]["_id"]}
                mongo_data = {"$set": {"mortality": request_data["data"]["mortality"]}}
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.MORTALITY_COLLECTION)
            else:
                mongo_data = {"date": request_data["data"]["date"],
                              "mortality": request_data["data"]["mortality"],
                              "batchNo": request_data["data"]["batchNo"],
                              "shedName": request_data["data"]["shedName"]
                              }
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.MORTALITY_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Mortality data saved successfully'
        except Exception as e:
            log.error("Error occurred while adding data due to " + str(e))
        return json_object

    def mortality_table(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching table data','tableData':{'headerContent':[],'bodyContent':[],'actions':{}}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MORTALITY_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['mortalityTableContent']['headerContent'])
            json_object['tableData']['actions']=(header[0]['mortalityTableContent']['actions'])
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    del each_data['_id']
                    json_object['tableData']['bodyContent'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Table data fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def diseases(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching tab data'}
        try:
            mongo_query = {
                "$and": [{"userName": request_data["userName"]}, {"diseaseName": request_data["data"]["diseaseName"]},{"diseaseDescription": request_data["data"]["diseaseDescription"]}]}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.DISEASES_COLLECTION)
            if data:
                mongo_query = {"_id": data[0]["_id"]}
                mongo_data = {"$set": {"diseaseName": request_data["data"]["diseaseName"]}}
                mongo_obj.update_one_record(mongo_query, mongo_data, database=app_configuration.MONGO_DATABASE,
                                            collection=app_configuration.DISEASES_COLLECTION)
            else:
                mongo_data = {"diseaseName": request_data["data"]["diseaseName"],
                              "diseaseDescription": request_data["data"]["diseaseDescription"],
                              "diseaseImage": request_data["data"]["diseaseImage"],
                              "medicineName": request_data["data"]["medicineName"],
                              "medicineImage": request_data["data"]["medicineImage"]
                              }
                mongo_obj.insert_record(mongo_data, database=app_configuration.MONGO_DATABASE,
                                        collection=app_configuration.DISEASES_COLLECTION)
            json_object['status'] = 'success'
            json_object['message'] = 'Diseases data saved successfully'
        except Exception as e:
            log.error("Error occurred while adding data due to " + str(e))
        return json_object

    def diseases_table(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while fetching table data','tableData':{'headerContent':[],'bodyContent':[],'actions':{}}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.DISEASES_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['diseasesTableContent']['headerContent'])
            json_object['tableData']['actions']=(header[0]['diseasesTableContent']['actions'])
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    del each_data['_id']
                    json_object['tableData']['bodyContent'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Table data fetched Successfully'
        except Exception as e:
            log.error("Error occurred while adding tab details due to " + str(e))
        return json_object

    def delete_settings_details(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error Occurred while deleting data'}
        try:
            mongo_operation = {app_constants.settingsKeyMapping[request_data['tabName']]: request_data['data'][app_constants.settingsKeyMapping[request_data['tabName']]]}
            mongo_obj.delete_records(mongo_operation, database=app_configuration.MONGO_DATABASE,
                                     collection=app_constants.settingsTabMapping[request_data['tabName']])
            json_object['status'] = 'success'
            json_object['message'] = 'Data deleted successfully'
        except Exception as e:
            log.error(f"Error occurred while deleting due to {e}. Kindly try after sometime")
        return json_object

    def blockedUsersTable(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error occurred while unblocking the user','tableData':{'headerContent':[],'bodyContent':[],'actions':{}}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['blockedUsersTableContent']['headerContent'])
            json_object['tableData']['actions']=(header[0]['blockedUsersTableContent']['actions'])
            filtered_data = []
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    # del each_data['_id'],each_data['password']
                    if(each_data['failedAttempts'] >=3):
                        filtered_data.append({
                            "userName": each_data.get("userName"),
                            "failedAttempts": each_data.get("failedAttempts")
                        })
            json_object['tableData']['bodyContent'] = filtered_data
            json_object['status'] = 'success'
            json_object['message'] = 'Table data fetched Successfully'
        except Exception as e:
            log.error("Error occurred while unblocking user due to " + str(e))
        return json_object

    def dashboardTableData(self, request_data):
        json_object = {'status': 'failed', 'message': 'Error occurred while fetching table data','tableData':{'headerContent':[],'bodyContent':[],'actions':{}}}
        try:
            mongo_query = {}
            data = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.SALES_COLLECTION)
            header = mongo_obj.fetch_records(query=mongo_query, database=app_configuration.MONGO_DATABASE,
                                           collection=app_configuration.MONGO_TAB_JSON_COLLECTION)
            json_object['tableData']['headerContent'].extend(header[0]['dashboardTableContent']['headerContent'])
            json_object['tableData']['actions']=(header[0]['dashboardTableContent']['actions'])
            if data:
                mongo_data = data
                for each_data in mongo_data:
                    del each_data['_id']
                    json_object['tableData']['bodyContent'].append(each_data)
            json_object['status'] = 'success'
            json_object['message'] = 'Table data fetched Successfully'
        except Exception as e:
            log.error("Error occurred while fetching table data due to " + str(e))
        return json_object
