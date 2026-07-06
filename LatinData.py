import random
#create dictionary for Latin adjectives
latin_words = {
    "Unus":["one"],
    "nUllus":["none","no"],
    "Ullus":["any"],
    "sOlus":["only","alone"],
    "neuter":["neither"],
    "alius":["another", "other"],
    "uter":["either"],
    "tOtus":["entire", "whole"],
    "alter":["the other"]
}

#randomize dictionary for iteration
list_of_lat_words = list(latin_words.items())
random.shuffle(list_of_lat_words)
randomized_lat_dic = dict(list_of_lat_words)