import re
import random
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
from text_processor import TextProcessor

# ✅ INHERITANCE: Paraphraser also inherits from TextProcessor
class Paraphraser(TextProcessor):

    def __init__(self, text):
        super().__init__(text)

    def _get_synonym(self, word):
        """
        ✅ ENCAPSULATION: Internal method to get a synonym for a word.
        Users never see or call this method directly.
        """
        synonyms = wordnet.synsets(word)
        if synonyms:
            for lemma in synonyms[0].lemmas():
                synonym = lemma.name().replace('_', ' ')
                if synonym.lower() != word.lower():
                    return synonym
        return word

    def _paraphrase_sentence(self, sentence):
        tokens = word_tokenize(sentence)
        paraphrased = []
        for word in tokens:
            if word.isalpha() and len(word) > 3:
                if random.random() < 0.4:
                    word = self._get_synonym(word)
            paraphrased.append(word)
        return ' '.join(paraphrased)

    # ✅ POLYMORPHISM: Like in Summarizer, this `process()` method behaves differently.
    # This one paraphrases instead of summarizing.
    def process(self):
        sentences = sent_tokenize(self._text)
        return ' '.join([self._paraphrase_sentence(s) for s in sentences])
