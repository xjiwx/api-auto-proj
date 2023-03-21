import logging
from testFunctions.getpathinfo import get_path
import os
import time
import colorlog
from logging import handlers

LOGGING_WHEN = 'D'                                         # 日志文件切分维度
LOGGING_INTERVAL = 1                                       # 间隔少个 when 后，自动重建文件
LOGGING_BACKUP_COUNT = 15                                 # 日志保留个数，0 保留所有日志
LOGGING_LEVEL = logging.DEBUG                              # 日志等级
LOGGING_suffix = "%Y.%m.%d.log"                            # 旧日志文件名

log_path = os.path.join(get_path(), 'logs')  # log_path是存放日志的路径
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)

class Log:
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        # self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.log_colors_config = {
            'DEBUG': 'green',
            'INFO': 'white',
            'WARNING': 'blue',
            'ERROR': 'red',
            'CRITICAL': 'yellow',
        }

    def __console(self, level, message):
        # 创建一个FileHander，用于写入本地

        fh = handlers.TimedRotatingFileHandler(filename=self.logname,
                                                         when=LOGGING_WHEN, interval=LOGGING_INTERVAL,
                                                         backupCount=LOGGING_BACKUP_COUNT,encoding='utf-8')
        fh.suffix = LOGGING_suffix
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler，用于输入到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # formatter = colorlog.ColoredFormatter(
        #     '%(log_color)s%(asctime)s  %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
        #     log_colors=self.log_colors_config)
        formatter = colorlog.ColoredFormatter(
            '%(log_color)s %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
            log_colors=self.log_colors_config)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)

        # 避免日志重复
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        # 关闭打开文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def critical(self, message):
        self.__console('critical', message)

if __name__ == '__main__':
    log = Log()
    log.info('测试')
    log.debug('测试')
    log.warning('测试')
    log.error('测试')
    log.critical('测试')


