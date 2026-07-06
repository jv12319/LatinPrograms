from LatinData import randomized_lat_dic
from quiz import quiz_func


quiz = input("Do you want to start your quiz on special latin adjectives? Enter y or n: ")
if quiz.lower() == "y":
    words_missed = quiz_func(randomized_lat_dic)
    while len(words_missed) != 0:
        retry_errors_answer = input("Would you like to repeat the words you missed? Enter y or n " )
        if retry_errors_answer.lower() == "y":
            words_missed = quiz_func(words_missed)
        else:
            print("Bye!")
    else:
        print("0 words missed. Great job!")
else:
    print("Bye!")
#07/04/26 Made small move over to linux