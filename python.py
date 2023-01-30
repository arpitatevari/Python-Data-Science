def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("\n")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("Incorrect!")
        return 0



    
questions = {
 "What is the capital of India?: ": "A",
 "What year was Python created?: ": "B",
 "Who is Prime Ministser of India?: ": "C"
}

options = [["A. Delhi", "B. Lucknow", "C. Shimla", "D. Manali"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"]]

new_game()
