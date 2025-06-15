from summarizer import Summarizer
from paraphraser import Paraphraser

# ABSTRACTION
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
        return processor.process()
