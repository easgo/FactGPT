#Main file
import argparse
import chatgpt
from goo import *
#Take initial prompt
def getPrompt():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='output file')
    args = parser.parse_args()
    if args.output:
        with open(args.output, 'w') as f:
            user_input = input('Enter a prompt to chatgpt: ')
            f.write(user_input)
    else:
        user_input = input('Enter a prompt for chatgpt: ')
        print('You entered:', user_input)
    return user_input


user_input = getPrompt()
#make call to chatgpt using chatgpt.py and get response
response = chatgpt.getGptText(user_input)
print(response)
topictext = chatgpt.getGptText("reformat as a list of context independent searchable questions for verification of the validity of all facts stated. No nonidentificable pronouns. Here is the response: " + response)
print(topictext)
topictext = topictext.split("\n")
print(topictext)
for topic in topictext:
    print("###########processing topic##########")
    print("topic: " + topic)
    if len(topic) > 1:
        get_snips(topic)
#identify sources 

