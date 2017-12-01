import sys


def count_words(sentence):

    summary = {}
    list_char = sentence.split(" ")
    for char in list_char:
        if char in summary:
            summary[char] += 1
        else:
            summary[char] = 1
    return summary

sentence = sys.argv[1]

recount = count_words(sentence).items()

for name, number in recount:
    print(name + ":" + str(number))
