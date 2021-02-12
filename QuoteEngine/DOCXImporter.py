from typing import List
from docx import Document


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXImporter(IngestorInterface):
    """Concrete subclasses of IngestorInterface to ovveride parse method for docx files."""

    allowed_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Override of parse method for docx files. Use python-docx module."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        qoutes = []
        doc = Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0].strip('"'), parse[1])
                qoutes.append(new_quote)

        return qoutes
