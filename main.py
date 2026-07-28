import LatinData as L
import quiz as q


which_quiz = input("Latin Program: \n 1 Special Adjectives Translation \n 2 Declensions" \
" \n 3 Verb Conjugations \n 4 Demonstratives \n 5 Authentic Latin Text Translations \n Enter Num Here-> ")
if int(which_quiz) == 1:
    qwords_missed = q.quiz_func(L.randomized_lat_adj_dic)
    while len(qwords_missed) != 0:
        qretry_errors_answer = input("Would you like to repeat the words you missed? Enter y or n " )
        if qretry_errors_answer.lower() == "y":
            qwords_missed = q.quiz_func(qwords_missed)
        else:
            print("Bye!")
    else:
        print("0 words missed. Great job!")
elif int(which_quiz) == 2:
    which_dec = input(" 1 for First Declension " \
    "\n 2 for Second Declension" \
    " \n 2.5 for Second Declension Neuter \n 3 for Third Declension \n Enter Num Here-> ")
    if float(which_dec) == 1:
        q.main_choice_retry_logic(q.decl_func,L.first_declension)
    elif float(which_dec) == 2:
        q.main_choice_retry_logic(q.decl_func, L.second_declension)
    elif float(which_dec) == 2.5:
        q.main_choice_retry_logic(q.decl_func,L.second_declension_neuter)
    elif float(which_dec) == 3:
        which_gen = input("Which gender? m for masc, f for fem, n for neut: ")
        if which_gen == "m":
            masc = {"REx":L.third_declension["REx"]}
            q.main_choice_retry_logic(q.decl_func,masc)
        elif which_gen == "f":
            fem = {"VirtUs":L.third_declension["VirtUs"]}
            q.main_choice_retry_logic(q.decl_func, fem)
        elif which_gen == "n":
            neut = {"Corpus":L.third_declension["Corpus"]}
            q.main_choice_retry_logic(q.decl_func, neut)
else:
    print("Haven't started yet.")
#07/04/26 Made small move over to linux