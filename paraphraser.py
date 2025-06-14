import re
import random
from text_processor import TextProcessor

# -------------------------------
# PARAPHRASER CLASS
# -------------------------------
# INHERITANCE: Inherits from TextProcessor to reuse initialization and text cleaning.
class Paraphraser(TextProcessor):

    def __init__(self, text):
        super().__init__(text)  # INHERITANCE

    def _split_sentences(self):
        return re.split(r'(?<=[.!?]) +', self._text)

    def _paraphrase_sentence(self, sentence):
        """
        Naively paraphrase by shuffling non-stopwords.
        """
        words = sentence.split()
        if len(words) <= 1:
            return sentence
        # Keep first and last words fixed (like humans often do)
        middle = words[1:-1]
        random.shuffle(middle)
        return ' '.join([words[0]] + middle + [words[-1]])

    # POLYMORPHISM: Same method name `process()` as in Summarizer,
    # but performs a completely different task.
    def process(self):
        sentences = self._split_sentences()
        return ' '.join([self._paraphrase_sentence(s) for s in sentences])
