from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An abstract superclass for ingestors for various type of files."""
    allowed_extension = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """A class method to checks if extension can be parse by this ingestor class"""
        if path.split('.')[-1] in cls.allowed_extension:
            return True
        else:
            False

    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """An abstract parse method."""
        pass
