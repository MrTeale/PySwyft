import logging
from .pyswyft import API
from .exceptions import PySwyftError


__title__ = 'pyswyft'
__version__ = '0.2.0'
__author__ = 'Lachlan Teale'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 Lachlan Teale'

# Version synonym
VERSION = __version__

# Set default logging handler to avoid "No handler found" warnings.
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

_all__ = (
    'API',
    'PySwyftError'
)