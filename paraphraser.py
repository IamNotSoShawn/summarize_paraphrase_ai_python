import re
import random
from text_processor import TextProcessor

# INHERITANCE + POLYMORPHISM
class Paraphraser(TextProcessor):
    def __init__(self, text):
        super().__init__(text)

    def _split_sentences(self):
        return re.split(r'(?<=[.!?]) +', self._text)

    def _paraphrase_sentence(self, sentence):
        words = sentence.split()
        if len(words) <= 1:
            return sentence
        middle = words[1:-1]
        random.shuffle(middle)
        return ' '.join([words[0]] + middle + [words[-1]])

    def process(self):
        sentences = self._split_sentences()
        return ' '.join([self._paraphrase_sentence(s) for s in sentences])
