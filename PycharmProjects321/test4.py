import logging

logging.basicConfig(filename="test4.log",level=logging.INFO,format='%(levelname)s,%(asctime)s,%(name)s,%(message)')

try:
    logging.info("i am trying to read a file")
    with open("sudh.txt","r"):
        logging.info("succesfully it has read the file")
except exception as e:
    logging.error(e)