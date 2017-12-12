import logging
from datetime import datetime

class Logging():

    def __init__(self, name):

        self.logger = self.set_logger(name)
        logging.basicConfig(
            filename=self.get_log_name(),
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"
        )


    def get_log_name(self):

        date = str(datetime.now().date())
        file_name = "log/%s.log" % date
        return file_name

    
    def info(self, log):
        self.logger.info(log)


    def error(self, log):
        self.logger.error(log)


    def set_logger(self, name):
        logger = logging.getLogger(name)
        return logger
