#Main file
import argparse
import chatgpt
from goo import *
import time
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
#prompts 
prompt_engineer1 = "reformat as a list of context independent searchable questions for verification of the validity of all facts stated. No nonidentificable pronouns. Here is the response: "
prompt_engineer2 = "reformat as a list of context independent searchable questions for verification of the validity of important facts stated. Keep the questions precise as possible to make it easier for google to pull up a result. Try not to give more than 5 questions. No nonidentificable pronouns. Here is the response:"
prompt_engineer3 = "I  want a list of queries about the important basic facts/numbers/dates listed in the text. They will be used to verify correctness in the text.  Here is the response: "
prompt_engineers = [prompt_engineer1, prompt_engineer2, prompt_engineer3]


#questions
concept_questions = ["what is the OS", "explain how the NBA works", "explain binary trees", "Steven Krashen who is", "Murphy's law of love"]
famous_ppl = ["Bio for Barack Obama", "Bio of Haruki Murakami", "Bio of Elon Musk"]
lesser_known = ["Bio of Grace Hopper", "Bio of Alan Turing", "bio of daniel calegari", "Give me a bio for XXtentacion", "Give me a bio for Walter white"]

#chat gpt is wrong 
wrong = ["How many countries start with the letter 'v'"]
i = -1
file_name = ["prompt_engineer1", "prompt_engineer2", "prompt_engineer3"]
for prompt_engineer in prompt_engineers:
    i += 1
    with open(file_name[i] + ".txt", "w") as f:
        for prompt in concept_questions:
            #time how long response takes
            s = time.time()
            response = chatgpt.getGptText(prompt)
            e = time.time() - s
            f.write(response)
            print(response)
            time.sleep(20-e)
            s = time.time()
            topictext = chatgpt.getGptText( prompt_engineer + response)
            print(topictext)
            f.write(topictext)
            topictext = topictext.split("\n")
            print(topictext)
            e = time.time() - s
            time.sleep(20-e)

# for topic in topictext:
#     print("###########processing topic##########")
#     print("topic: " + topic)
#     if len(topic) > 1:
#         get_snips(topic)
#identify sources 

