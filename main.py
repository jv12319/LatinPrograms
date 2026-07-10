from LatinData import randomized_lat_adj_dic
from quiz import quiz_func


quiz = input("Latin Program: \n 1 Special Adjectives Translation \n 2 Declensions" \
" \n 3 Verb Conjugations \n 4 Demonstratives \n 5 Authentic Latin Text Translations \n Enter Num Here->")
if int(quiz) == 1:
    words_missed = quiz_func(randomized_lat_adj_dic)
    while len(words_missed) != 0:
        retry_errors_answer = input("Would you like to repeat the words you missed? Enter y or n " )
        if retry_errors_answer.lower() == "y":
            words_missed = quiz_func(words_missed)
        else:
            print("Bye!")
    else:
        print("0 words missed. Great job!")
elif int(quiz) == 2:
    print("In progress.")
else:
    print("Haven't started yet.")
#07/04/26 Made small move over to linux