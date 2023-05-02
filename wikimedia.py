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
            self.sources.append(src)
          self.getPageContents(query)
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

##############################################################################
''' Deprecated --------------------------------------------------'''
def searchTopic(query):
  sourceToText = []
  #Wikimedia API call
  wiki_url = 'https://api.wikimedia.org/core/v1/wikipedia/en/search/page'
  numResults = 3
  #API token stuff  : currently it is a personal usaage token so may need to switch later
  #not sure if there is a rate limit
  headers = {
    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJkNTA1N2MyYjk3YjQyOWU1YTVkMjhhYmJiNmU4NDdkMyIsImp0aSI6IjhkNTg0YmY1ODBjZGU0YzdiY2IwZTEyM2UzZDBjMDU0NzZiNThiZDVmNzdkYWNlYWU3ZTZiMWY1YWRjMDIxNDdkZmEyM2U0ZmE2NWFjMjRkIiwiaWF0IjoxNjgyNDQyMjQyLjg4Njg5OSwibmJmIjoxNjgyNDQyMjQyLjg4NjkwMiwiZXhwIjozMzIzOTM1MTA0Mi44ODQ3MDUsInN1YiI6IjcyNjUzNTUwIiwiaXNzIjoiaHR0cHM6Ly9tZXRhLndpa2ltZWRpYS5vcmciLCJyYXRlbGltaXQiOnsicmVxdWVzdHNfcGVyX3VuaXQiOjUwMDAsInVuaXQiOiJIT1VSIn0sInNjb3BlcyI6WyJiYXNpYyJdfQ.lL3fvX89utGKQhoxLeTyRvKqZY30EIGAfVjFpVt9FoER_1TDXUkbammHK6IG5JN9-BcqtamOzypgUP1Uk_Xi7mzojBcJQznk2N2TNO06kms1ys5YP6QSC0fmr-FS7COe2bhqGMxPPonJNAHCWug5Q08q9d4cU22Y_hNilKUBUDr5HEoSoF391WBKSti_NRanlP75Ll0JhzhuwXimKSLCkKESZ8OUT7EfuhACpx4QNmNZ_dttj8udvR659VPNYU-NyvHvU9YT5npF1tMj5ClMFSCa7CRwoObrMk_T427mgowDCdAhukTF_6aZV6p1AXLCVDHH01TALRhmFrjZyYxdesPE3Tiu3NX-sop9qMF4iHuF0LPDTthEGJQWIicE1SvGBRXV8s4ZQgS6sM6KDfZaXPWGkDSB3Mb3lI5qVROARIp5Q252JstdO7yDMpu5gIO9eGER5J_-Rk0c2ZG-dOZyE-7nwtRGee186sRGuf1Pvt1Xkz5x-pnodhr0kocHAaVhNcls2eT5rWjUGv-fDuRJpOHtFcOg-OXItyvZhom5VDkteqg3on5qhbZAiZp84SqC7j53jhnA2pvlbodwU2lLkZUXFBwKzhq0B3UrdaHGM7BXtEaTrVOxwdx6yDN1XE4jF1eW8HAD0sAAcyLGLaJgfePAOnwTKjUVC6AsPpJed0E',
    'User-Agent': 'FactGPT (eton1234@outlook.com)'
  }
  searchParams = {'q': query, 'limit': numResults}
  response = requests.get(wiki_url, headers=headers, params=searchParams)
  wikiOut = response.json()
  print(wikiOut)
  #parse sources
  sources = wikiOut['pages']
  for src in sources:
      url, title = "https://en.wikipedia.org/?curid=" + str(src['id']), str(src['title'])
      '''TODO: Do we want to parse the excerpt to see if given src is relevant to topic? 
            soup = BeautifulSoup(src['excerpt'], 'html.parser')
            print(soup.get_text()) '''
      dict = {"title": title, "url": url , "text": ""}

      print(str(dict) + "------------" + "\n\n" )
      response = requests.get(str(url))
      soup = BeautifulSoup(response.text, 'html.parser')
      print(soup.get_text())
