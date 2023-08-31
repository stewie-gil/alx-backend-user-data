#!/usr/bin/env python3
""" the filter_datum method"""


import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """matches and replaces fields with redaction"""
    pattern = "|".join(map(re.escape, fields))
    return re.sub(f'({pattern})=[^\\{separator}]*',
                  f'\\1={redaction}', message)
