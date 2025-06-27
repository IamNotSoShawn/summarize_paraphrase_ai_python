import re
from text_processor import TextProcessor

class Summarizer(TextProcessor):

    def __init__(self, text):
# INHERITANCE
        super().__init__(text)

    def _split_sentences(self):
        return re.split(r'(?<=[.!?]) +', self._text)

    def _score_sentences(self, sentences):
        """
        Simple scoring: longest sentences assumed most important.
        """
        return sorted(sentences, key=len, reverse=True)[:2]
# POLYMORPHISM
    def process(self):
        sentences = self._split_sentences()
        summary = self._score_sentences(sentences)
        return ' '.join(summary)
