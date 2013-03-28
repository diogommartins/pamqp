"""AMQP Specifications and Classes"""
__author__ = 'Gavin M. Roy'
__email__ = 'gavinmroy@gmail.com'
__since__ = '2011-09-23'
__version__ = '1.1.3'

import sys

# Keep a constant that indicates if Python 3 support is needed
PYTHON3 = True if sys.version_info > (3, 0, 0) else False

from pamqp.header import ProtocolHeader
from pamqp.header import ContentHeader

from pamqp import body
from pamqp import codec
from pamqp import frame
from pamqp import specification
