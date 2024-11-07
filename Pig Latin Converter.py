word = str(input("Write a word: "))
def pig_latin(word):

    last_two = word[-2:]
    rest_letters = word[:-2]
    new_word = last_two + rest_letters + "ay"
    return  new_word

print(pig_latin(word))