import logging

logging.basicConfig(filename="test1.log",level=logging.DEBUG,format='%(levelname)s,%(asctime)s,%(name)s,%(message)s')
logging.info("this is my log with timestamp")