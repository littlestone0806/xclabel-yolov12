import logging
from logging.handlers import TimedRotatingFileHandler

def CreateLogger(filepath, is_show_console=False):
    LOGGER_WHEN = 'd'
    LOGFILE_BACKUPCOUNT = 7

    level = logging.INFO
    logger = logging.getLogger()
    logger.setLevel(level)
    # formatter = logging.Formatter('%(asctime)s %(name)s %(lineno)s Admin [%(levelname)s] %(message)s')
    formatter = logging.Formatter('[admin] %(asctime)s %(lineno)s [%(levelname)s] %(message)s')

    # 最基础
    # fileHandler = logging.FileHandler(filepath, encoding='utf-8')  # 指定utf-8格式编码，避免输出的日志文本乱码
    # fileHandler.setLevel(level)
    # fileHandler.setFormatter(formatter)
    # logger.addHandler(fileHandler)

    # 时间滚动切分
    # when:备份的时间单位，backupCount:备份保存的时间长度
    timedRotatingFileHandler = TimedRotatingFileHandler(filepath,
                                                        when=LOGGER_WHEN,
                                                        backupCount=LOGFILE_BACKUPCOUNT,
                                                        encoding='utf-8')

    timedRotatingFileHandler.setLevel(level)
    timedRotatingFileHandler.setFormatter(formatter)
    logger.addHandler(timedRotatingFileHandler)

    # 控制台打印
    if is_show_console:
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(level)
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)

    return logger

