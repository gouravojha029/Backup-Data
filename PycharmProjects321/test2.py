import logging

logging.basicConfig(filename="test2.log",level=logging.DEBUG,format='%(asctime)s %(message)s') # here tag of logg
# will not be seen.
logging.info("this is my log with timestamp")