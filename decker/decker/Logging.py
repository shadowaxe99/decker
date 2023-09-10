import logging

class Logging:
    def __init__(self):
        logging.basicConfig(filename='app.log', level=logging.INFO)

    def log_event(self, event):
        logging.info(event)

    def log_error(self, error):
        logging.error(error)