import re
from text_processor import TextProcessor

# ✅ INHERITANCE: Summarizer inherits from TextProcessor and uses its methods and attributes.
class Summarizer(TextProcessor):

    def __init__(self, text):
        # ✅ INHERITANCE: Reuses constructor logic from the parent class.
        super().__init__(text)

    def _split_sentences(self):
        return re.split(r'(?<=[.!?]) +', self._text)

    def _score_sentences(self, sentences):
        """
        Simple scoring: longest sentences assumed most important.
        """
        return sorted(sentences, key=len, reverse=True)[:2]

    # ✅ POLYMORPHISM: This class implements the `process()` method in its own way.
    # Same method name as in Paraphraser, but different behavior.
    def process(self):
        sentences = self._split_sentences()
        summary = self._score_sentences(sentences)
        return ' '.join(summary)
