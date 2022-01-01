#!/bin/python3

from os import system as sy
sy('bash bash.sh')

import logging

logger = logging.getLogger('Student-Logger')
logger.setLevel(logging.ERROR)

filehandler=logging.FileHandler('Student.log',mode='a')
filehandler.setLevel(logging.ERROR)

