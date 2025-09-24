import os
import logging


log_level = logging.INFO
if os.environ.get("DEBUG"):
    log_level = logging.DEBUG
print('DEBUG MODE', log_level)

def init_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s | %(asctime)s | %(name)-10s | %(funcName)s() | L%(lineno)-2d | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('app.log', mode='a'),
            # logging.FileHandler('app.log', mode='w')
        ]
    )

    logger = logging.getLogger(__name__)
    logger.warning("Logger setup conpleted successfully!")