from bs4 import BeautifulSoup
import requests
import json
import sys
from googleapiclient.discovery import build
import pprint
import re

'''SETUP '''
# query = sys.argv[1]
my_api_key = "AIzaSyCazeKt6NOwjg1uXNLhxxsb24hRHIjWrK8"
my_cse_id = "f18b63af5fa9d4bcc" #The search-engine-ID you created
pp = pprint.PrettyPrinter(indent=2)

'''HELPER FUNCTIONS'''
#Google search
def google_search(search_term, api_key, cse_id, **kwargs):
    #remove quotes and anything that would mess up the search query
    search_term = re.sub(r'[^a-zA-Z0-9\s\-:]', '', search_term)
    kwargs['siteSearch'] = 'wikipedia.org'
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']    

def google_search_wrapper(q, num):
    res = google_search(q, my_api_key, my_cse_id, num=num)
    return res

#scrape generc website 
def scrape_website(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the text content within the HTML tags
    text_content = soup.get_text()

    # Remove non-alphanumeric characters except spaces and dashes
    text_content = re.sub(r'[^a-zA-Z0-9\s\-:;.-]+', ' ', text_content)
    text_content = re.sub(r'\.', '. ', text_content)

    # Remove extra spaces and newlines
    text_content = re.sub(r'(\w+)(\s+)(?=edit\b)', r'\1.\2', text_content)
    text_content = re.sub(r'\s+', ' ', text_content).strip()
    return text_content

def get_snips(q):
    res = google_search(q, my_api_key, my_cse_id, num=1)
    output = []
    for result in res:
        print(result['snippet'] + "\n" + "Source link:" + result["link"])
        output.append(result['snippet'] + "\n\n" + "Source Link: " + result["link"])
    return output


'''TEST CODE'''
#TESTING
'''
#google search returns a list of results each being a dictionary
results = google_search(query, my_api_key, my_cse_id, num=2)

for result in results:
    #print the urls
    print(result['link']) 

if 'link' in results[0]:
    url = results[0]['link']  # Replace with the desired website URL
    url = str(url)
    print(url)
    result = scrape_website(url)
    print(result)
    #print(url)
'''

    