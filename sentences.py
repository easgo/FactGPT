import nltk
nltk.download('punkt')
def split_into_sentences(text):
    # This line splits the text into sentences and returns as a list
    return nltk.sent_tokenize(text)