#!/usr/bin/env python3
""" the filter_datum method"""


import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """matches and replaces fields with redaction"""
    pattern = "|".join(map(re.escape, fields))
    return re.sub(f'({pattern})=[^\\{separator}]*',
                  f'\\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """the init method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format logging records"""
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'ip')


def get_logger() -> logging.Logger:
    """Adds loggs to the stderr using streamhandler
    and formats with RedactingFormatter"""
    logger = logging.getlogger('user_data')
    logger.setlevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
    logger.propagate = False
    formatter = RedactingFormatter(PII_FIELDS)
    logger.setFormatter(formatter)
    return logger
