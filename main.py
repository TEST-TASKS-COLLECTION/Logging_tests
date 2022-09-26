from loguru import logger
import sys

logger.debug("Nice debug buddy!!")
logger.info("Nice info buddy!!")

# remove the previously used default handler
logger.remove()
# logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add(sys.stderr, format="{level} {message}", filter="main.py", level="ERROR")
logger.info("Nice info buddy!!")
logger.add("file_{time}.log")


try:
    print(0/0)
except ZeroDivisionError as e:
    logger.error(e)
    # logger.exception(e) # for traceback use this
    
    
# catching errors
@logger.catch
def catch_me_if_you_can():
    return 0 / 0

logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
catch_me_if_you_can()