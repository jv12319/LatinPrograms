import random

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

word_count = len(latin_words)
Num_of_correct = 0
Num_of_incorrect = 0
words_missed = {}

def check_adj_trans(answer, dictionary, word_to_be_checked):
    if answer in dictionary[word_to_be_checked]:
        return True
    else:
        return False
    
# def check_boolean_print (first_func_result,correct_count,incorrect_count):
#     if first_func_result == True:
#         correct_count+=1
#         print("You are correct")
#         print("Correct: " + str(correct_count))
#         return correct_count
#     else:
#         incorrect_count+=1
#         print("You are incorrect")
#         print("Incorrect: " + str(incorrect_count))
#         return incorrect_count
        #print("You are correct")
        #print("You are incorrect")
        #  Num_of_correct+=1
        #  print("Correct: " + str(Num_of_correct))
        #  print("Incorrect: " + str(Num_of_incorrect))
        # Num_of_incorrect+=1
        # print("Correct: " + str(Num_of_correct))
        # print("Incorrect: " + str(Num_of_incorrect))
        # if random_word in words_missed: 
        #     words_missed[random_word] = words_missed[random_word] + 1
        # else:
        #     words_missed[random_word] = 1

while True:
    for words in latin_words:
        random_word = random.choice(list(latin_words.keys()))
        user_answer = input("Translate " + random_word +" ")
        status_of_user_answer =check_adj_trans(user_answer,latin_words,random_word)
        if status_of_user_answer == True:
            print("You are correct")
            Num_of_correct+=1
            print("Correct: " + str(Num_of_correct))
            print("Incorrect: " + str(Num_of_incorrect))
        else:
            print("You are incorrect")
            Num_of_incorrect+=1
            print("Correct: " + str(Num_of_correct))
            print("Incorrect: " + str(Num_of_incorrect))
        # check_boolean_print(status_of_user_answer, Num_of_correct, Num_of_incorrect)
        # if answer in latin_words[random_word]:
        #     print("You are correct")
        #     Num_of_correct+=1
        #     print("Correct: " + str(Num_of_correct))
        #     print("Incorrect: " + str(Num_of_incorrect))
        # else:
        #     print("You are incorrect")
        #     Num_of_incorrect+=1
        #     print("Correct: " + str(Num_of_correct))
        #     print("Incorrect: " + str(Num_of_incorrect))
        #     if random_word in words_missed: 
        #         words_missed[random_word] = words_missed[random_word] + 1
        #     else:
        #         words_missed[random_word] = 1

        
    accuracy = (Num_of_correct / word_count) * 100
    print("Your accuracy is: "+f"{accuracy:.2f}"+ "%")
    print("Words you missed: " + str(words_missed))
    retry_errors_answer = input("Would you like to repeat the words you missed? Enter y or n " )
    Num_of_correct = 0
    Num_of_incorrect = 0
    if retry_errors_answer.lower() == "y":
        while True:
            for random_word in words_missed:
                repeats_answer = input("Translate " + random_word + " ")

                if repeats_answer in latin_words[random_word]:
                    print("You are correct")
                    Num_of_correct+=1
                    print("Correct: " + str(Num_of_correct))
                    print("Incorrect: " + str(Num_of_incorrect))
                    #words_missed.pop(random_word)
                else:
                    print("You are incorrect")
                    Num_of_incorrect+=1
                    print("Correct: " + str(Num_of_correct))
                    print("Incorrect: " + str(Num_of_incorrect))
                    if random_word in words_missed: 
                        words_missed[random_word] = words_missed[random_word] + 1
                    else:
                        words_missed[random_word] = 1
            
            accuracy = (Num_of_correct / word_count) * 100
            print("Your accuracy is: "+f"{accuracy:.2f}"+ "%")
            print("Words you missed: " + str(words_missed))
            retry_errors_answer = input("Would you like to repeat the words you missed? Enter y or n " )
            Num_of_correct = 0
            Num_of_incorrect = 0
            if retry_errors_answer.lower() != "y":
                print("Bye!")
            break
    else:
        print("Bye!")
        break
