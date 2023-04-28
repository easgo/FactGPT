import re

def Find_Date(text): 
    #x is the string input from CHatGPT
    matches = []
    #I put as many possible formats for dates that I could find 
    #but there are def more 

    dates = [r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s+(\d{4})\b", 
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{4}",
    r"\d{1,2}\/\d{1,2}\/\d{2,4}",
    r"\d{1,2}\-\d{1,2}\-\d{2,4}",
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},?\s+\d{4}",
    r"\d{4}\-\d{2}\-\d{2}", 
    r'\d+\S\d+\S\d+', 
    r'[A-Z]\w+\s\d+']

    #in case there's more than one date in the file that needs to be checked
    for i in dates: 
        matches.append(re.findall(i, text))

    if matches is not None: 
        return matches 