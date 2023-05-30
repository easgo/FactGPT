#Main file
import argparse
import chatgpt
import openai
import time
import wikimedia
import sentence_match
import sentences
import facts
from facts import correct_facts
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

wiki_text = ""

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
    response_raw = chatgpt.getGptText(user_input)
    response = "########ChatGPT Output########\n" + response_raw + "\n\n"
    print(response)
    #queries = chatgpt.getGptText("reformat as a list of context independent searchable questions for verification of the validity of important facts stated. Keep the questions precise as possible to make it easier for google to pull up a result. Try not to give more than 2 questions. No nonidentificable pronouns. Here is the response: " + response)
    #print(queries)
    #queries = queries.split("\n")
    #print(queries)
    output = ""
    arr = []
    #for question in queries:
    #    if len(question) > 1:
    res = google_search_wrapper(user_input, 1)
            #askchat = "which of these links seems like it would be the best link to look at when trying to answer this question: " + str(question) + " please only respond with the one link: "
            #for results in res:
            #    askchat += ", " + str(results['link'])
            #    link = results['link']
            
           # try:
            #    finallink = chatgpt.getGptText(askchat)
           # except openai.error.RateLimitError as e:
           #     time.sleep(60)
           #    finallink = chatgpt.getGptText(askchat) 
    for results in res:
        link = results['link']
    text = scrape_website(link)

    #print("###########" +user_input+  "##########")
    #print(link)
    #print(text)
    #text = wikimedia.clean_string(text)
    #cut off useless stuff:
    search_phrase = "From Wikipedia the free encyclopedia"
    index = text.find(search_phrase)
    if index != -1:
        text = text[index + len(search_phrase):].strip()
    
    end_p = "Selected works. edit"
    ind_two = text.find(end_p)
    if ind_two != -1:
        text = text[0:ind_two].strip()

    outp = []
    for result in res:
    #    print(result['snippet'] + "\n" + "Source link:" + result["link"])
        outp.append(result['snippet'] + "\n\n" + "Source Link: " + result["link"])

        #set snips : outp to see snips or snips:text to see full page text
        question = {"q": user_input, "snips": text}
        arr.append(question)
        
        

        '''
        print("###########" +question +  "##########")
        if len(question) > 1:
            snips = get_snips(question)
            print(type(snips))
            question = {"q": question , "snips": snips}
            arr.append(question)
            text = scrape_website(snips.)
        '''
    #machine learning to replace facts:

    chatgpt_text = response_raw
    split_sentences = sentences.split_into_sentences(chatgpt_text)
    wiki_text = text
    print(split_sentences)
    #replaced_text = facts.correct_facts(chatgpt_text, verified_fact_text)
    
    #fix_dict = [{"q": "replaced text", "snips": replaced_text}]



    #identify sources  
    # 
    # arr = [{"q": question, "snips": ["string", "string", "string"]}, {"q": question, "snips": ["string", "string", "string"]]

#arr = [ obj1, obj2]
 # obj = {"q": question, "snips": {"src": url, "text": text, "other meta info mb similarity" : }}}] 

    #set "arr" to arr to see text results from google. Set "arr" to fix_dict to see spacy replaced text (currently doesn't work)
    return jsonify({"gpt_response": split_sentences})


def get_single_replaced_sentence(sentence):
    wik_tex = wiki_text
    replaced_sent = sentence_match.evaluate_sentence_evidence(sentence, wiki_text)
    return replaced_sent

@app.route('/correct-facts', methods=['GET'])
def correct_facts_handler():
    args = request.args

    sentence = args['sentence']

    sentence.replace("+", " ")

    corrected_text = get_single_replaced_sentence(sentence)

    # Return the corrected text and any other data as a response
    response_data = {
        'corrected_text': corrected_text
    }
    return jsonify(response_data)

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