import re
from text_processor import TextProcessor

# -------------------------------
# SUMMARIZER CLASS
# -------------------------------
# INHERITANCE: Summarizer inherits from TextProcessor.
# It reuses the text cleaning and text handling logic.
class Summarizer(TextProcessor):

    def __init__(self, text):
        super().__init__(text)  # INHERITANCE from parent constructor

    def _split_sentences(self):
        """
        Helper method to split text into sentences.
        """
        return re.split(r'(?<=[.!?]) +', self._text)

    def _score_sentences(self, sentences):
        """
        A naive scoring system: longest sentences are most 'important'.
        Returns top 2.
        """
        sorted_sentences = sorted(sentences, key=len, reverse=True)
        return sorted_sentences[:2]

    # POLYMORPHISM: This is a different implementation of `process()`
    # than the one in Paraphraser, but it uses the same interface.
    def process(self):
        sentences = self._split_sentences()
        summary = self._score_sentences(sentences)
        return ' '.join(summary)
