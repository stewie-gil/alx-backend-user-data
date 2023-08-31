#!/usr/bin/env python3
""" the filter_datum method"""


import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """matches and replaces fields with redaction"""
    pattern = r'({})=([^;]+)'.format('|'.join(fields))
    replacement = r'\1={}'.format(redaction)
    return re.sub(pattern, replacement, message)
