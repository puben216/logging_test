import logging
import sys

log_file = sys.argv[1]

#logging.basicConfig(filename=log_file, level=logging.INFO)
logging.basicConfig(filename=log_file, level=logging.DEBUG)

logging.debug('debug kiteru')
logging.info('info kiteru')
logging.debug('debug kiteru')
logging.error('error kiteru')
logging.warning('warning kiteru')

print('end')	
