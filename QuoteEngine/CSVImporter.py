from typing import List
import pandas as pd


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVImporter(IngestorInterface):
    """Concrete subclasses of IngestorInterface to ovveride parse method for csv files."""

    allowed_extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Override of parse method for csv files. Use pandas module."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pd.read_csv(path)
        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'].strip('"'), row['author'])
            quotes.append(new_quote)

        return quotes
