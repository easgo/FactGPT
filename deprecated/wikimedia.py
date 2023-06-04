from bs4 import BeautifulSoup
import requests
import json
import wikipediaapi
import wikipedia
import re, string


class Source:
  def __init__(self, url, text):
    self.url = url
    self.text = text

class Wikipedia:
    def __init__(self,query):
      self.sources = []
      #loading sources
      try:
          #first try to search for the page directly
          s = wikipedia.page(str(query))
          if s:
            # print("successfully found topic")
            src = Source(s.url, s.content)
            self.sources.append(src)
      except:
        print("excepted first try. now searching for multiple pages")
        search_results = wikipedia.search(query)
        # print(search_results)
        for result in search_results:
          try:
            s= wikipedia.page(str(result))
            if s:
              src = Source(s.url, s.content)
              self.sources.append(src)
          except:
            pass
    def getTextSegs(self,leng=4000):
      segs = []
      for src in self.sources:
        #split up text into segments with leng number of characters
        text = src.text
        # use regex to replace this pattern \n\n\n==== Go ====\n
        # text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
        text = re.sub(' +', ' ', text)
        text = clean_string(text)
        while len(text) > leng:
          segs.append(text[:leng])
          text = text[leng:]
        segs.append(text)
      return segs
#helper function



def clean_string(input_string):
    cleaned_string = re.sub(r'==+.*?==+', '', input_string)  # Remove section headings
    cleaned_string = re.sub(r'{{.*?}}', '', cleaned_string)  # Remove templates
    cleaned_string = re.sub(r'\[\[.*?\]\]', '', cleaned_string)  # Remove internal links
    cleaned_string = re.sub(r'<.*?>', '', cleaned_string)  # Remove HTML tags
    cleaned_string = re.sub(r'[^a-zA-Z0-9()\s-]+', '', cleaned_string)  # Remove non-word characters except parentheses, dashes, and spaces
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string)  # Replace multiple spaces with a single space
    return cleaned_string.strip()
