from abc import ABC, abstractmethod

# ABSTRACTION + ENCAPSULATION
class TextProcessor(ABC):
    def __init__(self, text):
        self._text = self._clean_text(text)

    def _clean_text(self, text):
        return text.strip()

    @abstractmethod
    def process(self):
        pass
