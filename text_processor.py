from abc import ABC, abstractmethod

# -------------------------------
# ABSTRACT BASE CLASS (Abstraction)
# -------------------------------
# This class hides the complex logic of how a text should be processed.
# It provides a common interface (process()) that all children must implement.
class TextProcessor(ABC):
    def __init__(self, text):
        # ENCAPSULATION: The _text variable is protected (not public)
        # Only accessible through class methods, not directly from outside
        self._text = self._clean_text(text)

    def _clean_text(self, text):
        """
        Helper method to clean the input text.
        This is a protected method – part of encapsulation.
        """
        return text.strip()

    @abstractmethod
    def process(self):
        """
        ABSTRACT METHOD (Abstraction):
        Forces subclasses to define their own version of process().
        """
        pass
