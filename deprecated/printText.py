import time 

#this function will cause a delay for each word of the text
def print_text_animated(text):
    for char in text: 
        print(char, end = "", flush = True)
        time.sleep(0.02)
