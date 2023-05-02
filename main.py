#Main file
import argparse
import chatgpt
import wikimedia
import datechecker
from wikimedia import Wikipedia
#in command line, take in initial prompt
def getPrompt():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='output file')
    args = parser.parse_args()
    if args.output:
        with open(args.output, 'w') as f:
            user_input = input('Enter a prompt to chatgpt: ')
            f.write(user_input)
    else:
        user_input = input('Enter a prompt for chatgpt: ')
        print('You entered:', user_input)
    return user_input



#main code (maybe put in a main function?)
#prompt user to enter question (for now let's do this with command line)
user_input = getPrompt()
#make call to chatgpt using chatgpt.py and get response
response = chatgpt.getGptText(user_input)
'^^'
print(response)
topictext = chatgpt.getGptText("give a list of up to 3 main wikipedia topics in this text. Only respond with those three or less topics, separated by commas. Only include topics if they are unique and central to the text: " + response)
print(topictext)
topictext.replace("\n", "")
topics = topictext.split(", ")
print(topics)
prompttopic = chatgpt.getGptText("give a list of up to 3 main wikipedia topics in this text. Only respond with those three or less topics, separated by commas. Only include topics if they are unique and central to the text: " + user_input)
print(prompttopic)
prompttopic.replace("\n", "")
ptop = prompttopic.split(", ")
print(ptop)
#Identify relevant topics returned as a list of strings
#topics = processtext.identify_topics(response)
#make calls to wikimedia.py to get relevant text
#Iterate through topics, make wikipedia call and save text to list
wikipedia_pages = [] #will be list of strings, each string is a topic with text to compare to
for topic in topics:
    textArray = Wikimedia(topic).getTextSegs()
    wikipedia_pages.append(textArray)
    #make calls to wikipedia function
for pto in ptop:
    wikitext = wikimedia.search_wikipedia(topic)
    wikipedia_pages.append(wikitext)

#chatgpt workaround
substitutedtext = response 
print(wikipedia_pages)
for page in wikipedia_pages:
    print(page)
    if page != []:
        substitutedtext = chatgpt.getGptText("Compare these two texts and list ALL the parts in the first text where there is a date that is different than in the second text. The second text is always correct, only the first text can be incorrect. Respond with the first text substituted with the dates from the second text. Only say the substituted text: " + "\"" + substitutedtext + "\" , \"" + page[0]['content'])  

print(substitutedtext)



'''
#go through text from chatgpt and go through text from topic pages and identify parts of the text that match
#"was born on" "happened on" etc
# Given 2 chunks of text, how to figure out if there's matching text?
#key: 45 value: ("john was born on feb 5th", "john was born on march 4th")
#key: index in chatgpt text string where the first character in the chatgpt fact starts 
#value: maybe a pair: (chatgpt fact, Wikipedia fact) Basically, the line of text from chatgpt, the line of similar text in wikipedia pages
def is_similar(sentence1, sentence2):
    # Tokenize the sentences
    tokens1 = nltk.word_tokenize(sentence1)
    tokens2 = nltk.word_tokenize(sentence2)

    # Get the POS tags for each sentence
    pos_tags1 = nltk.pos_tag(tokens1)
    pos_tags2 = nltk.pos_tag(tokens2)

    # Extract the nouns from each sentence
    nouns1 = [word for (word, pos) in pos_tags1 if pos.startswith('N')]
    nouns2 = [word for (word, pos) in pos_tags2 if pos.startswith('N')]

    # Check if any of the nouns in the first sentence are also in the second sentence
    for noun1 in nouns1:
        for noun2 in nouns2:
            # Use WordNet to check if the nouns are synonyms
            synsets1 = wordnet.synsets(noun1)
            synsets2 = wordnet.synsets(noun2)
            for synset1 in synsets1:
                for synset2 in synsets2:
                    if synset1.wup_similarity(synset2) is not None and synset1.wup_similarity(synset2) > 0.8:
                        return True

    return False

# Watch out for text that contains periods (like Mr.)
def find_similar_sentences(response, wikipedia_pages):
    response_sentences = [s.strip() for s in response.split('.') if s.strip()]
    wikipedia_sentences = []
    for wikipedia_page in wikipedia_pages:
        wikipedia_sentences += [s.strip() for s in wikipedia_page.split('.') if s.strip()]

    facts_to_check = {}
    for i, response_sentence in enumerate(response_sentences):
        for j, wikipedia_sentence in enumerate(wikipedia_sentences):
            if any(char.isdigit() for char in response_sentence) and any(char.isdigit() for char in wikipedia_sentence):
                if is_similar(response_sentence, wikipedia_sentence):
                    index = response.index(response_sentence)
                    facts_to_check[index] = (response_sentence, wikipedia_sentence)
    return facts_to_check

facts_to_check = find_similar_sentences(response, wikipedia_pages)
print(facts_to_check)
'''