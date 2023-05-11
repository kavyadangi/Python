#Define a function which counts vowels and consonants in a word.
def count(string):
    vowel=0
    consonant=0
    for i in range(0, len(string), 1):
        if (string[i]== "a" or string[i]== "e" or string[i]== "i" or string[i]== "o" or string[i]== "u" or string[i]== "A" or string[i]== "E" or string[i]== "I" or string[i]== "O" or string[i]== "U"):
            vowel+=1
        else:
            consonant+=1
    print("Vowel count :", vowel)
    print("Consonant count:", consonant)
string=str(input("Please enter a string"))
count(string)
