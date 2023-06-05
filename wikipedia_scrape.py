import requests
from bs4 import BeautifulSoup
import nltk
from collections import Counter

# Global variables to store paragraphs and infobox information
all_paragraphs = []
infobox_info = {}


#grab the raw wiki stuff
def scrape_wikipedia(article_url):
    all_paragraphs = []
    infobox_info = {}

    # Send a GET request to the Wikipedia article URL
    response = requests.get(article_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Store all paragraphs in the global list
        all_paragraphs = soup.find_all('p')

        # Scrape the infobox information
        infobox_info = scrape_infobox(soup)
        return [all_paragraphs, infobox_info]
    else:
        # If the request was not successful, raise an exception
        raise Exception('Failed to retrieve the Wikipedia article.')
    
#HELPER
def scrape_infobox(soup):
    # Find the infobox section based on its class or other attributes
    try: 
        infobox = soup.find('table', {'class': 'infobox'})

        # Extract the key-value pairs from the infobox
        info_dict = {}
        rows = infobox.find_all('tr')
        for row in rows:
            header = row.find('th')
            if header:
                key = header.get_text(strip=True)
                td = row.find('td')
                if td:
                    value = td.get_text(strip=True)
                    info_dict[key] = value

        # Return the infobox information
        return info_dict
    except:
        return {}
#HELPER
def identify_relevant_paragraphs(sentence, n, all_paragraphs):
    # global all_paragraphs

    # Validate the value of n
    if n < 1:
        raise ValueError("The value of 'n' must be greater than or equal to 1.")

    # Tokenize the given sentence into keywords
    sentence_keywords = nltk.word_tokenize(sentence)

    # Find the relevant paragraphs based on keyword extraction
    relevant_paragraphs = []
    paragraph_scores = Counter()

    # Iterate over all stored paragraphs
    for paragraph in all_paragraphs:
        # Tokenize the paragraph into keywords
        paragraph_keywords = nltk.word_tokenize(paragraph.get_text())

        # Calculate the relevance score based on the number of overlapping keywords
        relevance_score = len(set(sentence_keywords) & set(paragraph_keywords))

        # Store the relevance score for the paragraph
        paragraph_scores[paragraph] = relevance_score

    # Select the top n paragraphs with the highest relevance scores
    for paragraph, _ in paragraph_scores.most_common(n):
        relevant_paragraphs.append(paragraph.get_text())

    # Return the relevant paragraphs
    return relevant_paragraphs


#called for each sentence
def get_evidence(sentence, all_paragraphs, infobox_dict, n=5):
    relevant_paragraphs = identify_relevant_paragraphs(sentence, n, all_paragraphs)
    # Create a list to store all the content
    content = []

    # Add the relevant paragraphs to the content list
    content.extend(relevant_paragraphs)
    text_content = "\n".join(content)

    infos = ["#infobox#"]
    # Add the infobox key-value pairs to the content list
    for key, value in infobox_dict.items():
        infos.append(f"{key}: {value}")
    infos.append("#content#")
    # Combine all the content into a single string
    infobox = "\n".join(infos)

    combined =  infobox + text_content
    print(combined)
    # Return the combined content string
    return combined


'''
# Example usage
article_url = "https://en.wikipedia.org/wiki/Jenny_Han"

# Scrape the Wikipedia page and store the paragraphs and infobox information
para, info = scrape_wikipedia(article_url)

# Prompt the user for a sentence
sentence = "Jenny Han was born on November 7th, 1875"

# Prompt the user for the number of relevant paragraphs to identify
n = 2

# Identify the relevant paragraphs
# relevant_paragraphs = identify_relevant_paragraphs(sentence, para)

# print(combine_paragraphs_infobox(relevant_paragraphs, infobox_info))
print(get_evidence(sentence,para,info))
'''