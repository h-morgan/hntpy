from hntpy.account import Account
from hntpy.hotspot import Hotspot
from loguru import logger
import sys

logger.remove()
logger.add(sys.stderr, level="DEBUG")
