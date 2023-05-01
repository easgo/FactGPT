from bs4 import BeautifulSoup
import requests
import json
import wikipediaapi
import wikipedia

#outputs an array where each element is a dictionary with the format, {content: text, url: "https://..."}
def search_wikipedia(query):
  output = []
  #first try to search for the page directly
  try:
    page = returnPageContents(query)
    if page:
      # print("successfully found topic")
      output.append({"content": page.content,"url": str(page.url)})
      return output
  except:
     pass
#otherwise search for related search topics
  # print("searching for corresponding wikipage")
  search_results = wikipedia.search(query)
  # print(search_results)
  for result in search_results:
    page = returnPageContents(result)
    if page:
      output.append({"content": page.content,"url": str(page.url)})
  return output
  
#helper function
def returnPageContents(page):
  try:
    s = wikipedia.page(str(page))
    if s:
      return s
    else:
      return None
  except:
    return None





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
