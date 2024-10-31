from logging import Logger, getLogger
from traceback import format_exc
from typing import Optional

from fivc.core.interfaces import IComponentSite, loggers
from fivc.core.interfaces.utils import implements


@implements(loggers.ILogger)
class LoggerImpl:
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
class LoggerSiteImpl:

    def __init__(self, component_site: IComponentSite, **kwargs):
        print('create logger site component of default')

    def get_logger(self, topic: str):
        return LoggerImpl(getLogger(topic))
