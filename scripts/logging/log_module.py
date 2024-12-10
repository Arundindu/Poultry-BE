import logging
import logging.handlers
import os
import sys
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

from scripts.constants import app_configuration

if not os.path.exists(app_configuration.LOG_BASE_PATH):
    os.makedirs(app_configuration.LOG_BASE_PATH)

logging.trace = logging.DEBUG - 5
logging.addLevelName(logging.DEBUG - 5, 'TRACE')


class GLensLogger(logging.getLoggerClass()):
    def __init__(self, name):
        super().__init__(name)

    def trace(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.trace):
            self._log(logging.trace, msg, args, **kwargs)


def get_logger():
    """sets logger mechanism"""
    # logging.setLoggerClass(GLensLogger)
    _logger = logging.getLogger("GLens")
    _logger.setLevel(app_configuration.LOG_LEVEL)

    if app_configuration.LOG_LEVEL == 'DEBUG' or app_configuration.LOG_LEVEL == 'TRACE':
        _formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - '
                                       '%(lineno)d - %(message)s')
    else:
        _formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if 'file' in app_configuration.LOG_HANDLERS:
        _file_handler = logging.FileHandler(app_configuration.FILE_NAME)
        _file_handler.setFormatter(_formatter)
        _logger.addHandler(_file_handler)

    if 'rotating' in app_configuration.LOG_HANDLERS:
        _rotating_file_handler = RotatingFileHandler(filename=app_configuration.FILE_NAME,
                                                     maxBytes=int(app_configuration.FILE_BACKUP_SIZE),
                                                     backupCount=int(app_configuration.FILE_BACKUP_COUNT))
        _rotating_file_handler.setFormatter(_formatter)
        _logger.addHandler(_rotating_file_handler)

    if 'console' in app_configuration.LOG_HANDLERS:
        _console_handler = StreamHandler(sys.stdout)
        _console_handler.setFormatter(_formatter)
        _logger.addHandler(_console_handler)

    return _logger


logger = get_logger()
