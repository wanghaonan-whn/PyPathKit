from abc import ABC, abstractmethod
from pathlib import Path

from pathkit.base.path import PathEntry


class BaseReader(ABC):
    """Base class for file readers."""

    def __init__(self, path: str | Path | PathEntry) -> None:
        self.path = path.path if isinstance(path, PathEntry) else Path(path)

    @abstractmethod
    def read(self) -> str:
        raise NotImplementedError
