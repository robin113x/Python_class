#!/bin/python3
from os import system as sy
sy('bash bash.sh')
#python program

import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
print('python logging demo')
logging.debug("Debug message")
logging.info("info message")
logging.warning("warning message")
logging.critical("critical message")
logging.error("error message")





print("*"*20)
opt=input('do u want to see ur log [Y/N] : ')
if opt == 'y' or opt == 'Y':
    print()
    sy('cat -n log.txt')
else:
    print('thank you')


