#!/bin/python3
from logging import *
from os import system as sy

sy('bash bash.sh')
# python program

from logging import *

# step1
logger = getLogger('Robin')
logger.setLevel(DEBUG)

# step2
consoleHandler = StreamHandler()

formatter = Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                      datefmt='%d/%m/%Y %I:%M:%S %p')

# step3
consoleHandler.setFormatter(formatter)

# step4
logger.addHandler(consoleHandler)

logger.critical('Hello')
