from logging.handlers import TimedRotatingFileHandler
from configs.global_adapter import *


def configure_logging(app):
    for handler in list(app.logger.handlers):
        app.logger.removeHandler(handler)

    handler = TimedRotatingFileHandler(
        LOG_FILENAME,
        when='midnight',
        interval=1,
        backupCount=0,
        encoding='utf-8'
    )
    handler.setFormatter(LOG_FILE_FORMAT)
    handler.setLevel(LOG_LEVEL)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(LOG_FILE_FORMAT)
    console_handler.setLevel(LOG_LEVEL)

    app.logger.addHandler(handler)
    app.logger.addHandler(console_handler)
    app.logger.setLevel(LOG_LEVEL)

    return app
