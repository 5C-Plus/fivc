from logging import getLogger, Logger
from traceback import format_exc
from typing import Optional

from fivc.interfaces import IComponentSite
from fivc.interfaces import loggers
from fivc.interfaces.utils import implements


@implements(loggers.ILogger)
class LoggerImpl(object):
    """
    default logger
    """

    def __init__(self, logger: Logger):
        self.logger = logger

    def info(
            self,
            msg: Optional[str] = None,
            attrs: Optional[dict] = None,
            exc: Optional[Exception] = None,
    ):
        self.logger.info(msg or format_exc())

    def warning(
            self,
            msg: Optional[str] = None,
            attrs: Optional[dict] = None,
            exc: Optional[Exception] = None,
    ):
        self.logger.warning(msg or format_exc())

    def error(
            self,
            msg: Optional[str] = None,
            attrs: Optional[dict] = None,
            exc: Optional[Exception] = None,
    ):
        self.logger.error(msg or format_exc())


@implements(loggers.ILoggerSite)
class LoggerSiteImpl(object):

    def __init__(self, component_site: IComponentSite, **kwargs):
        print('create logger site component of default')

    def get_logger(self, topic: str):
        return LoggerImpl(getLogger(topic))
