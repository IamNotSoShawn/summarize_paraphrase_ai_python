from text_tool import TextTool

if __name__ == "__main__":
    print("Do you want to summarize or paraphrase the text?")
    user_choice = input("Enter 'summarize' or 'paraphrase': ").strip().lower()

    if user_choice not in ['summarize', 'paraphrase']:
        print("Invalid choice. Please restart and enter 'summarize' or 'paraphrase'.")
    else:
        print("\nEnter the text you want to process:")
        user_text = input("> ")

        tool = TextTool(user_text, user_choice)
        result = tool.run()

        print(f"\n{user_choice.capitalize()}d Text:")
        print(result)
import nltk



