import logging
import time


# logging.basicConfig(filename=f"{time.time()}.log", filemode="a")
# the least 10 (debug msg), highest 50 (fatal error msg)
# displays messages from the given level and up

# backwards compatibility
fmt = "%(asctime)s :: %(levelname)-8s :: %(message)s"
logging.basicConfig(format=fmt)
logging.basicConfig(level=10)
logging.debug("Debug message")
logging.info("Mike")
logging.warning("Oxlong")
logging.error("Mike")
logging.fatal("Hunt")

try:
    x = int(input("x: "))
    logging.info(x)
    y = int(input("y: "))
    logging.info(x)
    z = x / y
    logging.info("z")
except ZeroDivisionError:
    logging.error("You can't divide with 0")

except Exception as e:
    logging.error(e)
    logging.warning("WARNING THE APP IS STIL RUNNING")
