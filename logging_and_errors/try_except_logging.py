import logging

# Log to console and file
logging.basicConfig(level=logging.INFO, filename='error.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.exception("Exception occurred while dividing numbers")
