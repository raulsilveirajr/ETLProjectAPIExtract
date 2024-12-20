import logging
from logging import basicConfig, getLogger

import logfire

# ----------------------------
# Logfire Configuration

logfire.configure()
basicConfig(handlers=[logfire.LogfireLoggingHandler()])
logger = getLogger(__name__)
logger.setLevel(logging.INFO)
logfire.instrument_requests()
logfire.instrument_sqlalchemy()

# ----------------------------
