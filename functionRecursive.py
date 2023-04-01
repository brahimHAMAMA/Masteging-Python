theWord =  "BBBBrrrraaaahiiiimmmm"

def cleanWord(word):
    if len(word) == 1:
        print(f" ++++ {word} ++++")
        return word
    print(f" **** {word} ****")
    if word[0] == word[1]:
        return cleanWord(word[1:])
    else:
        print(f"=> {word[0]} + {word[1:]}")
        return word + cleanWord(word[1:])

print(cleanWord(theWord))
