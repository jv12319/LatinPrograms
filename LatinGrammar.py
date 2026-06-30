# word = "puella"
# meaning = "girl"

# print(word + " = " + meaning)

# latin_words = {
#     "puella":"girl",
#     "amIcus":"friend",
#     "bellum":"war",
#     "rEx":"king",
#     "corpus":"body"
# }

# print(latin_words["puella"])

# answer = input("What does bellum mean? ")

# if answer == "war":
#     print("Correct!")
# else:
#     print("Incorrect!")

# vocab = ["puella","amIcus","bellum","rEx","corpus"]

# for words in vocab:
#     print(words)

#MINI QUIZ
import random

latin_words = {
    "Unus":"one",
    "nUllus":["none","no"],
    "Ullus":"any",
    "sOlus":["only","alone"],
    "neuter":"neither",
    "alius":"another",
    "uter":"either",
    "tOtus":"entire",
    "alter":"the other"
}

word_count = len(latin_words)
Num_of_correct = 0
Num_of_incorrect = 0
words_missed = {}
# for words in latin_words:
#     print(latin_words[words])
#     print(latin_words[words][1])

while True:
    for words in latin_words:
        answer = input("Translate " + words +" ")

        if answer in latin_words[words]:
            print("You are correct")
            Num_of_correct+=1
            print("Correct: " + str(Num_of_correct))
            print("Incorrect: " + str(Num_of_incorrect))
        else:
            print("You are incorrect")
            Num_of_incorrect+=1
            print("Correct: " + str(Num_of_correct))
            print("Incorrect: " + str(Num_of_incorrect))
            if words in words_missed: 
                words_missed[words] = words_missed[words] + 1
            else:
                words_missed[words] = 1

        
    accuracy = (Num_of_correct / word_count) * 100
    print("Your accuracy is: "+f"{accuracy:.2f}"+ "%")
    print("Words you missed: " + str(words_missed))
    end = input("Would you like to go again? Enter y or n " )
    Num_of_correct = 0
    Num_of_incorrect = 0
    if end.lower() != "y":
         break