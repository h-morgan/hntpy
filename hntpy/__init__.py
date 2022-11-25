from hntpy.account import Account
from loguru import logger
import sys

logger.remove()
logger.add(sys.stderr, level="DEBUG")
