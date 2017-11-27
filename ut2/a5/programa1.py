import sys


def num_vowels(text):
    vowels = "aeiou"
    num = 0
    for char in text:
        if char.lower() in vowels:
            num = num + 1
    return num


def num_whitespaces(text):
    space = 0
    for char in text:
        if char == " ":
            space = space + 1
    return space


def num_digits(text):
    digits = "0123456789"
    num = 0
    for char in text:
        if char in digits:
            num = num + 1
    return num


def num_words(text):
    stringtext = text.split()
    words = len(stringtext)
    return words


def reverse(text):
    size = len(text)
    rev = ""
    for char in range(1, size + 1):
        rev = rev + (text[-char])
    return rev


def length(text):
    ln = len(text)
    return ln


def halfs(text):
    half = len(text) / 2
    first_half = text[:int(half)]
    second_half = text[int(half):]
    return first_half + " | " + second_half


def upper_vowels(text):
    vowels = "aeiou"
    uppervowels = ""
    for vowel in text:
        if vowel in vowels:
            uppervowels = uppervowels + vowel.upper()
        else:
            uppervowels = uppervowels + vowel
    return uppervowels


def sorted_by_words(text):
    stringtext = text.split()
    stringlist = sorted(stringtext)
    sbw = " ".join(stringlist)
    return sbw


def length_of_words(text):
    stringtext = text.split()
    newlist = list()
    listsize = len(stringtext)
    for i in range(listsize):
        value = len(stringtext[i])
        newlist.append(str(value))
    low = " ".join(newlist)
    return low


text = sys.argv[1]
print("Number of vowels: ", num_vowels(text))
print("Number of whitespaces: ", num_whitespaces(text))
print("Number of digits: ", num_digits(text))
print("Number of words: ", num_words(text))
print("Reverse of text: ", reverse(text))
print("Length of text: ", length(text))
print("Halfs of text: ", halfs(text))
print("Text with uppercased vowels: ", upper_vowels(text))
print("Sorted by words: ", sorted_by_words(text))
print("Length of words: ", length_of_words(text))
