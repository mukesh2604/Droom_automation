import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_dir = os.path.join(os.getcwd(), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, 'automation.log')

        # Create a logger object
        logger = logging.getLogger("automationLogger")
        logger.setLevel(logging.DEBUG)

        # Avoid adding handlers multiple times
        if not logger.handlers:
            # File handler
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.DEBUG)

            # Console handler
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            # Formatter
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # Add handlers
            logger.addHandler(fh)
            logger.addHandler(ch)

        return logger
