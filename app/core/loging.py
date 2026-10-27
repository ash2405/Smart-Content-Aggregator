import sys
from pathlib import Path

from loguru import logger


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Log directory
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


# show log in console and file
def setup_logging() -> None:
    # Remove default logger configuration
    logger.remove()

    # Console logging
    logger.add(
        sys.stdout, # to show log in console
        level = 'INFO', # TRACE | DEBUG | INFO | SUCCESS | WARNING | ERROR | CRITICAL
        format = (
                "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | " # log time
                "<level>{level: <8}</level> | " # level
                "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | " # module name, line number and function
                "<level>{message}</level>" # logger.info("Server Started")
                ), # it decides how the log will show
        colorize = True
    )

    # File logging
    logger.add(
        LOG_DIR / "app.log",
        level="INFO",
        rotation="10 MB",
        retention="7 days",
        compression="zip",
        encoding="utf-8",
    )