from transformers import pipeline


summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def summary_agent(user_message: str, max_length: int = 1000, min_length: int = 50) -> str:
    """
    Summarizes the user message using a pre-trained model.
    """
    # Truncate input to fit model limits
    user_message = user_message[:4000]
    summary = summarizer(user_message, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']



if __name__ == "__main__":
    test_message = (
        "The quick brown fox jumps over the lazy dog. "
        "This is a test message to demonstrate the summarization capabilities of the model. "
        "The model should be able to condense this information into a shorter form while retaining the key points."
    )
    print("Original Message:")
    print(test_message)
    print("\nSummarized Message:")
    print(summary_agent(test_message))




     
                         









                         