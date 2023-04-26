# pip3 install loguru
# Logging

from loguru import logger

logger.add('debug_{time}.log', colorize=True)  # Connects a log file.
logger.add('error_{time}.log', level='ERROR')  # Another file for errors or higher.
print("\n")
logger.success('A succuss message.')
print("\n")
logger.info('A info message.')
print("\n")
logger.warning('A warning message.')
print("\n")
logger.error('A error message.')
print("\n")
logger.critical('A critical message.')
