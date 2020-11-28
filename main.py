import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        matchedWord = get_close_matches(w, data.keys())[0]
        yn = input("Did you mean %s instead (Y/N) :" % matchedWord)
        if yn == "Y":
            return data[matchedWord]
        elif yn == "N":
            return "The word doesn't exist, Please double check it!"
        else:
            return "We didn't understand that! Please try again."
    else:
        return "The word doesn't exist, Please double check it!"


word = input("Enter word: ")

output = translate(word)
if(type(output) == list):
    for w in output:
        print(w)
else:
    print(output)
