import re
import random
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
from text_processor import TextProcessor

class Paraphraser(TextProcessor):
    def __init__(self, text):
        super().__init__(text)

    def _get_synonym(self, word):
        """
        Find a synonym for the word using WordNet. Return the original word if no synonym found.
        """
        synonyms = wordnet.synsets(word)
        if synonyms:
            # Get all possible lemmas for the first synonym
            lemmas = synonyms[0].lemmas()
            # Choose one synonym that is different from the original word
            for lemma in lemmas:
                synonym = lemma.name().replace('_', ' ')
                if synonym.lower() != word.lower():
                    return synonym
        return word

    def _paraphrase_sentence(self, sentence):
        """
        Replace some words with their synonyms.
        """
        tokens = word_tokenize(sentence)
        paraphrased = []

        for word in tokens:
            # Only try replacing if it's a normal word (not punctuation or number)
            if word.isalpha() and len(word) > 3:
                if random.random() < 0.4:  # 40% chance to replace
                    word = self._get_synonym(word)
            paraphrased.append(word)

        return ' '.join(paraphrased)

    def process(self):
        sentences = sent_tokenize(self._text)
        return ' '.join([self._paraphrase_sentence(s) for s in sentences])
