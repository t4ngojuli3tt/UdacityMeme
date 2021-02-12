from typing import List
import subprocess
import os

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .TXTImporter import TXTImporter


class PDFImporter(IngestorInterface):
    """Concrete subclasses of IngestorInterface to ovveride parse method for pdf files."""

    allowed_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Override of parse method for pdf files.
        This method use subprocess module to use pdftotext console app to convert pdf to txt.
        Hence in order for this to work pdftotext must be install.
        In order to parse txt file this method call TXTImporter.parse method.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = './_data/quotes.txt'
        subprocess.call(['pdftotext', path, tmp])
        quotes = TXTImporter.parse(tmp)
        os.remove(tmp)

        return quotes
