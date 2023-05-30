import nltk
nltk.download('punkt')
def split_into_sentences(text):
    # This line splits the text into sentences and returns as a list
    return nltk.sent_tokenize(text)

text = "Hi my name is Lisa. I am 10 years old. I was born in August."
print(split_into_sentences(text))