from summarizer import Summarizer
from paraphraser import Paraphraser

# ✅ ABSTRACTION: This class hides the logic for which processor is chosen.
# The user just gives a mode and text, and it handles the rest.
class TextTool:
    def __init__(self, text, mode):
        self.text = text
        self.mode = mode.lower()

    def run(self):
        if self.mode == 'summarize':
            processor = Summarizer(self.text)
        elif self.mode == 'paraphrase':
            processor = Paraphraser(self.text)
        else:
            raise ValueError("Invalid mode. Choose 'summarize' or 'paraphrase'.")

        # ✅ POLYMORPHISM IN ACTION: `processor.process()` works regardless of class.
        return processor.process()
