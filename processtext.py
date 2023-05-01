import gensim
from gensim import corpora
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk import pos_tag
from string import punctuation

def identify_topics(text, num_topics=5):
    # preprocess text by removing stopwords and punctuation
    # you can use any text preprocessing techniques you like
    # for example, you can use the NLTK library for stopwords removal
    # and the string library for punctuation removal
    text = text.lower()
    # remove punctuation
    text = ''.join([c for c in text if c not in punctuation])
    # remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in text.split() if word not in stop_words]
    words = [word for word, pos in pos_tag(words) if pos not in ['JJ', 'JJR', 'JJS']]
    # create a dictionary from the list of words
    dictionary = corpora.Dictionary([words])
    
    # create a bag-of-words representation of the text
    corpus = [dictionary.doc2bow(words)]
    
    # train a topic model using LDA
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)
    
    # get the top topics for the text
    top_topics = lda_model.show_topics(num_topics=num_topics, num_words=3)
    
    #unique topics
    unique_topics = []
    for topic in top_topics:
        # get the topic words and score
        words = topic[1].split("+")
        score = topic[0]
        
        # create a list of topic words
        topic_words = []
        for word in words:
            # get the word without the probability score
            word = word.split("*")[1].strip().replace('"', '')
            topic_words.append(word)
        
        # check if the topic has already been added to the unique_topics list
        if set(topic_words) not in [set(t) for t in unique_topics]:
            unique_topics.append(topic_words)
    
    return unique_topics

#test

words = "hi my name is lisa. I like dogs and pineapples. Today I bought a pineapple at a store. It was delicious. Unfortunately, I am allergic to pineapples. My dog had to take me to the hospital. It was a bad day."
print(identify_topics(words))
more_words = "John Bobb the third was born on December 450th in the second year of the galactic empire. In archaic terms, he was born on December 13th, 3600. He grew up in Monrovia District 2. His mother was a poet and his father was a galactic shaper. He had a hard childhood because he lived through the 67 famines that happened that year. This childhood shaped his political decisions later in life. In November of year three (In common terms, November 3666), he graduated from intensification training, and got an administrative position in the government. In November 3766, he was elected as president of his local district. At that point in time, he began to commit controversial acts, such as unbanning apple trees and promoting snake worship. He also disturbed the peace. He signed many laws into action, such as the law requiring inspection for headaches to check for district 8ix fever. His most famous act while in office was when he signed a law favoring trickle down economics. The money never tricked down. Ultimately, John Bobb the third lived a lengthy and eventful life. He died on December 31st, 3701. He left behind 81 children, three dogs, and a legacy that will shape his district for generations. He was truly an important figure in the galactic empire"
print(identify_topics(more_words))
prompt = "write an explanation about the life of John Bobb the third"
print(identify_topics(prompt))