from logging.handlers import RotatingFileHandler
# i don't intend on using this unless i'm hosting it somehwere 24/7 but why would i
def setup_logging():
    handler = RotatingFileHandler("discord.log", maxBytes=5_000_000, backupCount=3)
    logging.basicConfig(level=logging.INFO, handlers=[handler])
