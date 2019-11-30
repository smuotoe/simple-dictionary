import json
from difflib import get_close_matches

data = json.load(open('data.json', 'r'))

def translate(word):
    if word not in data:
        word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0]).lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input('Enter a word: ')

output = translate(word)

if type(output) == list:
    count = 1
    for item in output:
        print(str(count) + ". " + item)
        count = count + 1
else:
    print(output)
