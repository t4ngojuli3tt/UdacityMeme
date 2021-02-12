from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVImporter import CSVImporter
from .DOCXImporter import DOCXImporter
from .TXTImporter import TXTImporter
from .PDFImporter import PDFImporter


class Ingestor(IngestorInterface):
    """Concrete subclasses of IngestorInterface to ovveride parse method
    to provide one interface for exiting importers.
    """
    importers = [DOCXImporter, CSVImporter, TXTImporter, PDFImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Override of parse method that checks if there is importer
        that could ingest a file and call it if found.
        """

        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
