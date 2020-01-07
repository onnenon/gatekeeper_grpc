import logging
import sys

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
handler.setLevel(logging.INFO)

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)

SERVER_ADDRESS = "localhost:8990"
ROW_COUNT = 20
USE_BOARD = None
