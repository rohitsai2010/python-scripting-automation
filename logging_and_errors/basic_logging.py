import logging

# Set up basic logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Debugging info")
logging.info("General info")
logging.warning("Warning occurred")
logging.error("An error happened")
logging.critical("Critical issue")
