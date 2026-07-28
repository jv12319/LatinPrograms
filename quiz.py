import LatinData as LD
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

def quiz_func(variable_dict):
    Num_of_correct = 0
    Num_of_incorrect = 0
    func_words_missed = {}
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
    
    retry_word_count = len(func_words_missed)
    if retry_word_count == 0:
        return func_words_missed
    else:
        accuracy = (Num_of_correct / len(variable_dict)) * 100
        print("Your accuracy is: "+f"{accuracy:.2f}"+ "%")
        print("Words you missed: " + str(func_words_missed))
    return func_words_missed

def decl_func(variable_dict):
    Num_of_correct=0
    Num_of_incorrect=0
    decl_words_missed = {}
    for noun, forms in variable_dict.items():
        for form, cases in forms.items():
            for case, answer in cases.items():
                user_answer = input(f"Decline {noun.lower()} in the {form} case {case.lower()} ")
                if user_answer == answer:
                    Num_of_correct+=1
                    print(f"Eureka!\nCorrect: {Num_of_correct} Incorrect: {Num_of_incorrect}")
                else:
                    Num_of_incorrect+=1
                    print(f"NOPE\nCorrect: {Num_of_correct} Incorrect: {Num_of_incorrect}")
                    if noun not in decl_words_missed:
                        decl_words_missed[noun] = {}
                    if form not in decl_words_missed[noun]:
                        decl_words_missed[noun][form] = {}
                    if case not in decl_words_missed:
                            decl_words_missed[noun][form][case] = answer
    if len(decl_words_missed) == 0:
        print("Great job no errors!")
        return decl_words_missed
    else:
        accuracy = (Num_of_correct / (len(variable_dict[noun][form]) * 2))*100
        print(f"Words you missed:  {decl_words_missed}\nAccuracy: {accuracy:.2f}%")
    return decl_words_missed

#Function to carry out some of the main files logic with choosing quizes/retries
def main_choice_retry_logic(var_func, variable_dict):
    words_missed = decl_func(variable_dict)
    while len(words_missed) != 0:
        retry_errors_answer = input("Would you like to repeat the words you missed? Enter y or n " )
        if retry_errors_answer.lower() == "y":
            words_missed = decl_func(words_missed)
        else:
            print("Bye!")
            break

def conj_func(variable_dict):
    