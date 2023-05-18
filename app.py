#Main file
import argparse
import chatgpt
import wikimedia
from wikimedia import Wikipedia
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from goo import *
app = Flask(__name__, static_folder='public')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')
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


@app.route('/main', methods=['POST'])
def main():
    user_input = request.json['prompt']

    #make call to chatgpt using chatgpt.py and get response
    response = "########ChatGPT Output########\n" + chatgpt.getGptText(user_input) + "\n\n"
    print(response)
    queries = chatgpt.getGptText("reformat as a list of context independent searchable questions for verification of the validity of important facts stated. Keep the questions precise as possible to make it easier for google to pull up a result. Try not to give more than 5 questions. No nonidentificable pronouns. Here is the response: " + response)
    print(queries)
    queries = queries.split("\n")
    print(queries)
    output = ""
    arr = []
    for question in queries:
        print("###########" +question +  "##########")
        if len(question) > 1:
            snips = get_snips(question)
            print(type(snips))
            question = {"q": question , "snips": snips}
            arr.append(question)

    #identify sources  
    # 
    # arr = [{"q": question, "snips": ["string", "string", "string"]}, {"q": question, "snips": ["string", "string", "string"]]

#arr = [ obj1, obj2]
 # obj = {"q": question, "snips": {"src": url, "text": text, "other meta info mb similarity" : }}}] 
    return jsonify({"gpt_response": response , "arr" : arr})


if __name__ == '__main__':
    app.run()

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