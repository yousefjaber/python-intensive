import logging
import colorlog

class ColorLog:
    
    def __init__(self) -> None:
        self.logger = logging.getLogger("ColorLogger")
        self.logger.setLevel(logging.DEBUG)
        
  
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)

       
        formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)s: %(message)s",
            log_colors={
                'DEBUG': 'blue',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'magenta',
            }
        )

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def debug(self, message: str) -> None:
        self.logger.debug(message)
        
    def info(self, message: str) -> None:
        self.logger.info(message)
        
    def warning(self, message: str) -> None:
        self.logger.warning(message)
        
    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)

if __name__ == "__main__":
    log = ColorLog()
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.critical("This is a critical message")
