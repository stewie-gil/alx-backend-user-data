#!/usr/bin/env python3
""" the filter_datum method"""


import re


def filter_datum(fields, redaction, message, separator):
    """matches and replaces fields with redaction"""
    pattern = r'({})=([^;]+)'.format('|'.join(fields))
    replacement = r'\1={}'.format(redaction)
    return re.sub(pattern, replacement, message)
