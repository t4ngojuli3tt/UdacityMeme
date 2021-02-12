from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTImporter(IngestorInterface):
    """Concrete subclasses of IngestorInterface to ovveride parse method for txt files."""

    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Override of parse method for txt files."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open(path, "r") as file:
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0].strip('"'), parse[1])
                    quotes.append(new_quote)
        return quotes
