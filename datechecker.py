import re

def Find_Date(text): 
    #x is the string input from CHatGPT
    #key is index, value is date 
    matches = {}
    #I put as many possible formats for dates that I could find 
    #but there are def more 
    dates = [r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s+(\d{4})\b", 
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{4}",
    r"\d{1,2}\/\d{1,2}\/\d{2,4}",
    r"\d{1,2}\-\d{1,2}\-\d{2,4}",        
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},?\s+\d{4}",
    r"\d{4}\-\d{2}\-\d{2}", 
    r'\d+\S\d+\S\d+', 
    r'[A-Z]\w+\s\d+', 
    r"\b(\d{4})\b",            
    r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})(\-\d{0,1}\d{0,1})?,\s+(\d{4})\b"]

    #creating a set so that it won't duplicate date outputs with all the options above
    found_positions = set()
    for i in dates:
        for match in re.finditer(i, text):
            #start and end variable to help match character to date
            start, end = match.start(), match.end()
            # Check if this match overlaps with any previously found matches
            if not any(start < found_end and end > found_start for found_start, found_end in found_positions):
              date_str = match.group()
              #adding to the dictionary with the start of the date
              matches[start] = date_str
              found_positions.add((start, end))

    if matches is not None: 
        return matches 
    else: 
        return None 