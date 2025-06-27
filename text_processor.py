from abc import ABC, abstractmethod

# ✅ ABSTRACTION: This abstract class defines the common interface `process()`
# and hides the logic of how text will be processed. Subclasses must implement it.
class TextProcessor(ABC):

    def __init__(self, text):
        # ✅ ENCAPSULATION: The `_text` attribute is "protected" (not public)
        # This hides the data from direct external access.
        self._text = self._clean_text(text)

    def _clean_text(self, text):
        """
        ✅ ENCAPSULATION: This is a protected helper method to clean input text.
        Only internal use; keeps text sanitization isolated.
        """
        return text.strip()

    @abstractmethod
    def process(self):
        """
        ✅ ABSTRACTION: This abstract method forces subclasses to define their
        own `process()` implementation — but hides what that actually looks like.
        """
        pass
