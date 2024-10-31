from typing import Optional

from . import IComponent, abstractmethod


class ILogger(IComponent):
    """
    logger
    """

    @abstractmethod
    def info(
            self,
            msg: Optional[str] = None,
            attrs: Optional[dict] = None,
            error: Optional[Exception] = None,
    ) -> None:
        """
        log info
        """

    @abstractmethod
    def warning(
            self,
            msg: Optional[str] = None,
            attrs: Optional[dict] = None,
            error: Optional[Exception] = None,
    ) -> None:
        """
        log warning
        """

    @abstractmethod
    def error(
            self,
            msg: Optional[str] = None,
            attrs: Optional[dict] = None,
            error: Optional[Exception] = None,
    ) -> None:
        """
        log error
        """


class ILoggerSite(IComponent):
    """
    logger site
    """

    @abstractmethod
    def get_logger(self, topic: str) -> ILogger:
        """
        get logger by topic
        """
