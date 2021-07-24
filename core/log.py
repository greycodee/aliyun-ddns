import logging
import logging.config
import os
from logging.handlers import TimedRotatingFileHandler


class Log(object):
    leave = None
    logger = None

    def __init__(self, leave=logging.WARNING):
        self.leave = leave
        logger_name = "dynamic_dns_log"
        logger = logging.getLogger(logger_name)
        logger.setLevel(self.leave)

        # create file handler
        log_path = "./logs/dynamic-dns-history.log"
        if not os.path.exists("./logs"):
            os.mkdir("./logs")
        fh = TimedRotatingFileHandler(log_path, when='D', interval=1, backupCount=7)
        fh.setLevel(self.leave)

        # create formatter
        fmt = '%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s'
        date_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(fmt, date_fmt)

        # add handler and formatter to logger
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        self.logger = logger

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

