import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources (run this only once)
nltk.download('punkt')
nltk.download('stopwords')

# Function to summarize text
def text_summarizer(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return " ".join(filtered_text)

text = "Natural Language Processing is a field of artificial intelligence that enables machines to understand human language."
print(text_summarizer(text))
