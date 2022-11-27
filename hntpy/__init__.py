from hntpy.resources.account import Account
from hntpy.resources.hotspot import Hotspot
from loguru import logger
import sys

logger.remove()
logger.add(sys.stderr, level="INFO")
