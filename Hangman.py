import random

yOrn = ["y","n"]

#validating the inputs from the users to avoid mistakes.
def validate(options, question):
    while True:
        try:
            answer = input(question)
            if answer not in options: raise Exception
            return answer
        except Exception:
            print(f"This input is not valid. Input something else thatn {answer}")
            continue

score = 0

#loops thru the game rounds
while True:

    #word choice 
    words = ["apple", "bannana", "pear", "tomato", "salad", "strawberry"]
    word  = random.choice(words)

    word_hidden = ["*" for char in word] 

  
    #variables
    running = True
    tries = 6

    #while loop to run when you still have tries
    while tries > 0:
        #print out the guessed word
        print("Word: " , *word_hidden)
        #gets input from user
        userInput = input(f"Guess a letter or word (tries {tries}/6)")

        #checking the word
            #if the input equals the word
        if userInput == word:
            print("You have guessed the word!")
            score+=1
            break
        #if the input is a letter in the word
        elif userInput in word:
            #finds index of letter gussed
            index = [i for i,ltr in enumerate(word) if ltr == userInput]
            #changes the letter in the hidden word
            for i in range(0,len(index)):
                word_hidden[index[i]] = userInput
            #checks if the word is guessed, by checking if "*" doesn't exist in the list
            if "*" not in word_hidden:
                score+=1
                running = False
            #breaks if the word is guessed
            if running == False:
                print("Word: " , *word_hidden)
                break
        #if guess is wrong
        else:
            tries-=1
            print("Wrong, try again.")
        #if you are out of tries
        if tries == 0:
            print("You are out of tries.")

    #checks if the player wants to play again, and if the input is valid by using our validation function
    userInput = validate(yOrn, "Do you want to play again? (y/n)")
    #if no it breaks the upper loop (while true loop) and shows the score
    if userInput == "n":
        print(f"You guessed {score} words.")
        break
    