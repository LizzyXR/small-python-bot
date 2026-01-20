from logging.handlers import RotatingFileHandler

def setup_logging():
    handler = RotatingFileHandler("discord.log", maxBytes=5_000_000, backupCount=3)
    logging.basicConfig(level=logging.INFO, handlers=[handler])