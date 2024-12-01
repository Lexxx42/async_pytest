"""Logging module of a project."""

import sys

from loguru import logger

LOG_LEVEL = "DEBUG"
LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | "
    "<level>{level: <8}</level> | "
    "<yellow>Line {line: >4} ({file}):</yellow> "
    "<cyan>{message}</cyan>"
)
# removing default logger
logger.remove()
# adding own logger with new format
logger.add(sys.stderr, level=LOG_LEVEL, format=LOG_FORMAT, colorize=True, backtrace=True, diagnose=True)
