import logging

def setup_logging():
    logger = logging.getLogger('autobox')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('autobox.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
