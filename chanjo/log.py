# -*- coding: utf-8 -*-
import logging

from . import __title__

logger = logging.getLogger(__title__)
logger.setLevel(logging.DEBUG)

LEVELS = {0: logging.ERROR, 1: logging.WARN, 2: logging.INFO,
          3: logging.DEBUG}


def make_handler(stream, level=logging.INFO):
    """Setup a logging handler connected to the logger.

    Args:
        stream (file): file-like object with ``write`` + ``flush`` methods
        level (level, optional): lower logger level to accept

    Returns:
        handler: configured logging ``StreamHandler`` instance
    """
    # create stream/file handler
    handler = logging.StreamHandler(stream)
    handler.setLevel(level)

    # set formatter
    template = "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s"
    formatter = logging.Formatter(template)
    handler.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(handler)

    return handler
