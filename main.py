import LatinData as L
import quiz as q


which_quiz = input("Latin Program: \n 1 Special Adjectives Translation \n 2 Declensions" \
" \n 3 Verb Conjugations \n 4 Demonstratives \n 5 Authentic Latin Text Translations \n Enter Num Here-> ")
if int(which_quiz) == 1:
    iwords_missed = q.quiz_func(L.randomized_lat_adj_dic)
    while len(iwords_missed) != 0:
        iretry_errors_answer = input("Would you like to repeat the words you missed? Enter y or n " )
        if iretry_errors_answer.lower() == "y":
            iwords_missed = q.quiz_func(iwords_missed)
        else:
            print("Bye!")
    else:
        print("0 words missed. Great job!")
elif int(which_quiz) == 2:
    which_dec = input(" 1 for First Declension \n 2 for Second Declension \n 2.5 for Second Declension Neuter \n 3 for Third Declension \n Enter Num Here-> ")
    if float(which_dec) == 1:
         q.decl_func(L.first_declension)
    else:
        print("Bye!")
else:
    print("Haven't started yet.")
#07/04/26 Made small move over to linux