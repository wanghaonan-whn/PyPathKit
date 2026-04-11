from abc import ABC, abstractmethod
from pathlib import Path


class BaseReader(ABC):
    """Base class for file readers."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    @abstractmethod
    def read(self) -> str:
        raise NotImplementedError
