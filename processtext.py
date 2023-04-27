import gensim
from gensim import corpora

def identify_topics(text, num_topics=5):
    # preprocess text by removing stopwords and punctuation
    # you can use any text preprocessing techniques you like
    # for example, you can use the NLTK library for stopwords removal
    # and the string library for punctuation removal
    
    # tokenize text into a list of words
    words = text.split()
    
    # create a dictionary from the list of words
    dictionary = corpora.Dictionary([words])
    
    # create a bag-of-words representation of the text
    corpus = [dictionary.doc2bow(words)]
    
    # train a topic model using LDA
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)
    
    # get the top topics for the text
    top_topics = lda_model.show_topics(num_topics=num_topics, num_words=10)
    
    return top_topics


#test

words = "hi my name is lisa. I like dogs and pineapples. Today I bought a pineapple at a store. It was delicious. Unfortunately, I am allergic to pineapples. My dog had to take me to the hospital. It was a bad day."

print(identify_topics(words))