
import logging
logging.basicConfig(filename="test.log",level = logging.INFO)
logging.info("this is my very first code for logging")
logging.warning("this will try to load a warning message")
l= [1,2,3,4,5,6,7,7]
for i in l:
    if i==2:
        logging.info(l)
        logging.warning("this is  a warning for a user that have found out 2 in list")
        logging.error("this is a error message from system")

logging.shutdown()
         logging.info("this will not be stored ")
# there are different level of logging
#1 debug(10)
#2 info(20)
#3 warning(30)
#4 error(40)
#5 critical(50)

