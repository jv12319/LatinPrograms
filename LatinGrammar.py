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

#for calculating accuracy
word_count = len(latin_words)

Num_of_correct = 0
Num_of_incorrect = 0

#for repeat quiz
words_missed = {}

words_missed_again = {}

#randomize dictionary for iteration
list_of_lat_words = list(latin_words.items())
random.shuffle(list_of_lat_words)
randomized_lat_dic = dict(list_of_lat_words)

#function to determine if user answer is right
def check_adj_trans(answer, dictionary, word_to_be_checked):
    if answer in dictionary[word_to_be_checked]:
        return True
    else:
        return False
    
#function to print score information
def print_score_info(True_or_false, correct_count, incorrect_count):
    if True_or_false == True:
        print("You are correct")
        print("Correct: " + str(correct_count))
        print("Incorrect: " + str(incorrect_count))
    else:
        print("You are incorrect")
        print("Correct: " + str(correct_count))
        print("Incorrect: " + str(incorrect_count))

def quiz_func(variable_dict, Num_of_correct, Num_of_incorrect,func_words_missed):
    for words in variable_dict:
        user_answer = input("Translate " + words +" ")
        status_of_user_answer =check_adj_trans(user_answer,variable_dict,words)
        if status_of_user_answer == True:
            Num_of_correct+=1
            print_score_info(status_of_user_answer, Num_of_correct, Num_of_incorrect)
        else:
            Num_of_incorrect+=1
            print_score_info(status_of_user_answer, Num_of_correct, Num_of_incorrect)
            func_words_missed[words] = variable_dict[words]
    
    accuracy = (Num_of_correct / word_count) * 100
    print("Your accuracy is: "+f"{accuracy:.2f}"+ "%")
    print("Words you missed: " + str(func_words_missed))
    return func_words_missed
    


quiz = input("Do you want to start your quiz on special latin adjectives? Enter y or n: ")
if quiz.lower() == "y":
    quiz_func(randomized_lat_dic,Num_of_correct,Num_of_incorrect, words_missed )
    retry_errors_answer = input("Would you like to repeat the words you missed? Enter y or n " )
    Num_of_correct = 0
    Num_of_incorrect = 0
    retry_word_count = len(words_missed)
    if retry_errors_answer.lower() == "y":
        while True:
            for retry_word in words_missed:
                retry_answer = input("Translate " + retry_word + " ")
                retry_status_of_user_answer =check_adj_trans(retry_answer,words_missed,retry_word)
                if retry_status_of_user_answer == True:
                    Num_of_correct+=1
                    print_score_info(retry_status_of_user_answer,Num_of_correct,Num_of_incorrect)
                else:
                    Num_of_incorrect+=1
                    print_score_info(retry_status_of_user_answer,Num_of_correct,Num_of_incorrect)
                    words_missed_again[retry_word] = words_missed[retry_word]
                
                
            
            accuracy = (Num_of_correct / retry_word_count) * 100
            print("Your accuracy is: "+f"{accuracy:.2f}"+ "%")
            print("Words you missed: " + str(words_missed_again))
            Num_of_correct = 0
            Num_of_incorrect = 0
            break
    else:
        print("Bye!")
else:
    print("Bye!")
