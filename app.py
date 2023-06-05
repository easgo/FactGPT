#Main file
import argparse
import chatgpt
import openai
import time
import sentence_match
import sentences
import facts
from facts import correct_facts
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from goo import *
#for the sentence scraping
from wikipedia_scrape import *

app = Flask(__name__, static_folder='public')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')
#in command line, take in initial prompt

wiki_text = ""
url = ""
# Global variables to store paragraphs and infobox information
para = []
info = {}


@app.route('/main', methods=['POST'])
def main():
    global url
    global para
    global info
    user_input = request.json['prompt']

    #GET CHATGPT RESPONSE
    response_raw = chatgpt.getGptText(user_input)
    #printing
    response = "########ChatGPT Output########\n" + response_raw + "\n\n"
    print(response)

    output = ""
    arr = []
    #SEARCH (user's question)  => top result
    res = google_search_wrapper(user_input, 1)
    
    for results in res:
        link = results['link']
    #scraping and updating url global
    text = scrape_website(link)
    para, info = scrape_wikipedia(link)
    url = str(link)
    chatgpt_text = response_raw
    split_sentences = sentences.split_into_sentences(chatgpt_text)

    return jsonify({"gpt_response": split_sentences})

def get_single_replaced_sentence(sentence):
    wiki_text = get_evidence(sentence, para, info)
    print(wiki_text)
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
        'corrected_text': corrected_text,
        "url": url
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run()