import logging
# this time i will get tag of logging also
logging.basicConfig(filename="test2.1.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s  %(message)s')
logging.info("this is my log with timestamp")