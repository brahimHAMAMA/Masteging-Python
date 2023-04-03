def remove_duplicate_words_from(sentence):
    words_list = sentence.split(" ")
    result = []
    for word in words_list:
        if word not in result:
            result.append(word)
    return " ".join(result)

# Testing Ouput
print(remove_duplicate_words_from("Hello Elzero Web Web Hello School"))
# Hello Elzero Web School
