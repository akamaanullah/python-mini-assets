from transformers import pipeline

# Load sentiment-analysis model
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result

text = "I love learning about AI!"
print(analyze_sentiment(text))
