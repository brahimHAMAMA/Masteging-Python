def remove_char_from(String, char):
    myList = String.lower().split()
    for word in myList:
        if char.lower() in word:
            word1 =  word.replace(char.lower(), "")
            myList[myList.index(word)] = word1.capitalize()
    return " ".join(myList)
# Testing Ouput
print(remove_char_from("ElddzeroD WebDD ddSchool", "d"))  # Elzero Web School
print(remove_char_from("ElxzeroX Web Sxchool", "x"))  # Elzero Web School
print(remove_char_from("Elzero@ Web@@ @@School", "@"))  # Elzero Web School


print("="*20)

def remove_char(String, char):
        felter = lambda w: w.lower().replace(char.lower(), "").capitalize() if (char.lower() in w or char.upper() in w) else w
        result = map(felter, String)
        return "".join(result)

print(remove_char("ElddzeroD WebDD ddSchool", "d"))  # Elzero Web School
print(remove_char("ElxzeroX Web Sxchool", "x"))  # Elzero Web School
print(remove_char("Elzero@ Web@@ @@School", "@"))  # Elzero Web School


print("="*20)

def remove_char(String, char):
        felter = lambda w:  char.lower() != w and char.upper() != w
        result = filter(felter, String)
        return "".join(result)

print(remove_char("ElddzeroD WebDD ddSchool", "d"))  # Elzero Web School
print(remove_char("ElxzeroX Web Sxchool", "x"))  # Elzero Web School
print(remove_char("Elzero@ Web@@ @@School", "@"))  # Elzero Web School