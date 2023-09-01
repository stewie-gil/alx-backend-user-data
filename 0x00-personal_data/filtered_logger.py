#!/usr/bin/env python3
""" the filter_datum method"""

import os
import re
import mysql.connector
from typing import List
import logging


def get_db() -> connection.MySQLConnection:
    """uses stored environment variables to
    connect to a msql db
    Return: a connector to the database"""

    personal_data_db_username = os.getenv('PERSONAL_DATA_DB_USERNAME')
    personal_data_db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    personal_data_db_host = os.getenv('PERSONAL_DATA_DB_HOST')
    personal_data_db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    

    connection = mysql.connector.connect(
        host=personal_data_db_host,
        user=personal_data_db_username,
        password=personal_data_db_password,
        database=personal_data_db_name
    )

    return connection


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
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
