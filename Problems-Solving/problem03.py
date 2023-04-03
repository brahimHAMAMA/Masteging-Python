def longest_word_in(phrase):

    myList = phrase.split()
    print(myList)
    word = myList[0]
    for w in myList:
        if len(w) > len(word): 
            word = w
    return word

print(longest_word_in("In Programming We Love Elzero Academy Tooooooooooo Much")) # Tooooooooooo
# print("="*20)
# def longWord(phrase1, phrase2):
#     return len(phrase1) >= len(phrase2)
# def convertInList(phrase):
#     return phrase.spite()
# print reduce(longWord, )


# print(longest_word_in("In Programming We Love Elzero Academy Tooooooooooo Much")) # Tooooooooooo