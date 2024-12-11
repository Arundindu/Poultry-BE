import configparser
import os

__config = configparser.ConfigParser()
__config.read("conf/application.conf")

# LOG HANDLERS

LOG_BASE_PATH = __config.get('LOG', 'base_path')
LOG_LEVEL = __config.get('LOG', 'level')
FILE_BACKUP_COUNT = __config.get('LOG', 'file_backup_count')
FILE_BACKUP_SIZE = __config.get('LOG', 'file_size_mb')
FILE_NAME = LOG_BASE_PATH + __config.get('LOG', 'file_name')
LOG_HANDLERS = __config.get('LOG', 'handlers')

# Server Details
PORT = __config.get('SERVER', 'port')
HOST = __config.get('SERVER', 'host')

KEY = "MONGO"
MONGO_HOST = os.environ.get("MONGO_HOST", __config.get(KEY, "HOST"))
MONGO_DATABASE = __config.get(KEY, "DATABASE")
MONGO_COLLECTION = __config.get(KEY, "USER_COLLECTION_NAME")
MONGO_TAB_COLLECTION = __config.get(KEY, "TAB_COLLECTION_NAME")
MONGO_TAB_JSON_COLLECTION = __config.get(KEY, "TAB_JSON_COLLECTION_NAME")
BIRD_PRICE_COLLECTION = __config.get(KEY, "BIRD_PRICE_COLLECTION_NAME")