import re
from text_processor import TextProcessor

# INHERITANCE + POLYMORPHISM
class Summarizer(TextProcessor):
    def __init__(self, text):
        super().__init__(text)

    def _split_sentences(self):
        return re.split(r'(?<=[.!?]) +', self._text)

    def _score_sentences(self, sentences):
        sorted_sentences = sorted(sentences, key=len, reverse=True)
        return sorted_sentences[:2]

    def process(self):
        sentences = self._split_sentences()
        summary = self._score_sentences(sentences)
        return ' '.join(summary)
