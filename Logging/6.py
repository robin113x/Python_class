#!/bin/python3
from logging import *
from os import system as sy

sy('bash bash.sh')

import logging

logger=logging.getLogger('Robin')
logger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
fileHandler = logging.FileHandler('abc.log',mode='a')


log_format = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s'
        ,datefmt='%d/%m/%Y :: %I:%M:%S %p')

consoleHandler.setFormatter(log_format)
fileHandler.setFormatter(log_format)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

logger.info('Starting')

try:
    a=int(input('Enter a no : '))
    b=int(input('Enter a no : '))
    print(a/b)
except Exception as msg:
    print('Error', msg)
    logger.exception(msg)
finally:
    print('Thank u')

logger.info('Closed')



