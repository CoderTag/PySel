import logging
import inspect


def get_logger():
    # inspect.stack() - display which test case invoked logger
    # logger = logging.getLogger(__name__)
    logger = inspect.stack()[1][3]
    logger.setLevel(logging.INFO)

    # Setting log format
    log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    # file where logger will print
    filehandler = logging.FileHandler('log.log')

    # console handler for logging
    handler = logging.StreamHandler()

    # pass the log format to both handler
    filehandler.setFormatter(log_format)
    handler.setFormatter(log_format)

    # add log file handler to logger
    logger.addHandler(filehandler)
    handler.setLevel(logging.INFO)

    return logger
