from loguru import logger
import sys

logger.debug("Nice debug buddy!!")
logger.info("Nice info buddy!!")

# remove the previously used default handler
logger.remove()
# logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add(sys.stderr, format="{level} {message}", filter="main.py", level="ERROR")
logger.info("Nice info buddy!!")
logger.add(f"file{__name__}.log", rotation="500 MB", serialize=True)




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

# catch_me_if_you_can()

logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>", backtrace=True)
def call_():
    logger.info("Inside of caller")
    catch_me_if_you_can()
    
    
# for binding
# so binding add these to the log information(message)
logger.add("bind.log", format="{extra[ip]} {extra[user]} {message}", serialize=True)
context_logger = logger.bind(ip="184.184.0.1", user="Mario")
context_logger.info("Pokemon was cool a decade ago, now it's just cash grab")

context_logger.bind(user="Lugi").info("Inline binding of extra attribute")
context_logger.info("{level} Use kwargs to add context during formatting: {user}", user="Peach",level=context_logger.level)