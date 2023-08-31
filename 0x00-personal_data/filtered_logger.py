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


def get_logger() -> logging.Logger:
    """creating a logger object"""
    logger = logging.get_logger("user_data")
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)

    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s: %(message)s')
    stream_handler.setFormatter(Formatter)

    return logger


PII_FIELDS = ("ssn", "credit_card", "email", "address", "phone_number")


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
