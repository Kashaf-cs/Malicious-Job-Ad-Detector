import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download required NLTK resources
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")


# Load stopwords
stop_words = set(stopwords.words("english"))

# Create lemmatizer
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove extra spaces
    text = " ".join(text.split())

    # Remove stopwords
    text = " ".join(
        word
        for word in text.split()
        if word not in stop_words
    )

    # Lemmatization
    text = " ".join(
        lemmatizer.lemmatize(word)
        for word in text.split()
    )

    return text

if __name__ == "__main__":

    sample_text = """
    URGENT HIRING!!! Work from home.
    Earn $5000 weekly. No experience required.
    """

    cleaned_text = preprocess_text(sample_text)

    print("Original Text:")
    print(sample_text)

    print("\nCleaned Text:")
    print(cleaned_text)