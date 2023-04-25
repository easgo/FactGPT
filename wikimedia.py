from bs4 import BeautifulSoup
import requests

url = 'https://api.wikimedia.org/core/v1/wikipedia/en/search/page'
# Random chat gpt response from query: "What is the size of the sun?"
search_query = 'The size of the Sun can be measured in several ways, including its diameter, volume, and mass.'
number_of_results = 10
parameters = {'q': search_query, 'limit': number_of_results}

#personal access token used to access the wikimedia api
headers = {
  'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJkNTA1N2MyYjk3YjQyOWU1YTVkMjhhYmJiNmU4NDdkMyIsImp0aSI6IjhkNTg0YmY1ODBjZGU0YzdiY2IwZTEyM2UzZDBjMDU0NzZiNThiZDVmNzdkYWNlYWU3ZTZiMWY1YWRjMDIxNDdkZmEyM2U0ZmE2NWFjMjRkIiwiaWF0IjoxNjgyNDQyMjQyLjg4Njg5OSwibmJmIjoxNjgyNDQyMjQyLjg4NjkwMiwiZXhwIjozMzIzOTM1MTA0Mi44ODQ3MDUsInN1YiI6IjcyNjUzNTUwIiwiaXNzIjoiaHR0cHM6Ly9tZXRhLndpa2ltZWRpYS5vcmciLCJyYXRlbGltaXQiOnsicmVxdWVzdHNfcGVyX3VuaXQiOjUwMDAsInVuaXQiOiJIT1VSIn0sInNjb3BlcyI6WyJiYXNpYyJdfQ.lL3fvX89utGKQhoxLeTyRvKqZY30EIGAfVjFpVt9FoER_1TDXUkbammHK6IG5JN9-BcqtamOzypgUP1Uk_Xi7mzojBcJQznk2N2TNO06kms1ys5YP6QSC0fmr-FS7COe2bhqGMxPPonJNAHCWug5Q08q9d4cU22Y_hNilKUBUDr5HEoSoF391WBKSti_NRanlP75Ll0JhzhuwXimKSLCkKESZ8OUT7EfuhACpx4QNmNZ_dttj8udvR659VPNYU-NyvHvU9YT5npF1tMj5ClMFSCa7CRwoObrMk_T427mgowDCdAhukTF_6aZV6p1AXLCVDHH01TALRhmFrjZyYxdesPE3Tiu3NX-sop9qMF4iHuF0LPDTthEGJQWIicE1SvGBRXV8s4ZQgS6sM6KDfZaXPWGkDSB3Mb3lI5qVROARIp5Q252JstdO7yDMpu5gIO9eGER5J_-Rk0c2ZG-dOZyE-7nwtRGee186sRGuf1Pvt1Xkz5x-pnodhr0kocHAaVhNcls2eT5rWjUGv-fDuRJpOHtFcOg-OXItyvZhom5VDkteqg3on5qhbZAiZp84SqC7j53jhnA2pvlbodwU2lLkZUXFBwKzhq0B3UrdaHGM7BXtEaTrVOxwdx6yDN1XE4jF1eW8HAD0sAAcyLGLaJgfePAOnwTKjUVC6AsPpJed0E',
  'User-Agent': 'FactGPT (eton1234@outlook.com)'
}

response = requests.get(url, headers=headers, params=parameters)
data = response.json()
pages = data['pages']
for page in pages:
    soup = BeautifulSoup(page['excerpt'], 'html.parser')
    print("\n\n" + "title: " + page['title'] +"," + "id: " + str(page["id"]) + "\n")

    print(soup.get_text())