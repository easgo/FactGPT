#Main file
import argparse
import chatgpt
import processtext
#in command line, take in initial prompt
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



#main code (maybe put in a main function?)
#prompt user to enter question (for now let's do this with command line)
user_input = getPrompt()
#make call to chatgpt using chatgpt.py and get response
response = chatgpt.getGptText(user_input)

#Identify relevant topics
topics = processtext.identify_topics(response)
#make calls to wikimedia.py to get relevant text

#run through 