import requests
from bs4 import BeautifulSoup

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

r = requests.get("https://www.google.com/search?q=gold+rate+india&safe=active&rlz=1C1GCEB_enIN960IN960&ei=gPF8ZMyjO7fNptQP5um9oAc&ved=0ahUKEwjM47jgt6r_AhW3pokEHeZ0D3QQ4dUDCBA&uact=5&oq=gold+rate+india&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQigUQsQMQQzIFCAAQgAQyBwgAEIoFEEMyBwgAEIoFEEMyBQgAEIAEMgcIABCABBAKMgUIABCABDIHCAAQgAQQCjIFCAAQgAQyBQgAEIAEOgoIABBHENYEELADOgoIABCKBRCwAxBDOg0IABCKBRCwAxBDEIsDOhEILhCABBCxAxCDARDHARDRAzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOgsIABCABBCxAxDJAzoICAAQigUQkgM6CwguEIAEELEDEIMBSgQIQRgAUIoIWOoSYIkUaANwAXgBgAHFAogB8w2SAQc1LjEuMy4ymAEAoAEBuAECwAEByAEK&sclient=gws-wiz-serp", headers=headers)
# print(r.status_code, r.content)
print(r.content)
soup = BeautifulSoup(r.content, 'lxml')

# result = soup.find('div', class_='vlzY6d')
print(soup.prettify)
