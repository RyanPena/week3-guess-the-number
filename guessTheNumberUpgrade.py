import random
def generateNumber( topLimit ):
    secretnumber = random.randint (1, str(toplimit))

def askUserToGuess( times, secretNumber ):
    for guessesTaken in range(1, times+1):
        print('Take your guess #' + str(guessesTaken) + ': ')
        guess = int(input())

        if evaluateAnswer( guess, secretNumber ) == True:
            return True
        
    return False
def evaluateAnswer( userGuess, userSecretNumber ):
    if userGuess < userSecretNumber:
        print('Your guess is too low.')
        return False
    elif userGuess > userSecretNumber:
        print('Your guess is too high')
        return False
    elif userGuess == userSecretNumber:
        return True
    
def playGame( showAnswer ):
    print('Hello. What is your name?')
    name = input()
    print('Hello there,' + name + ',this game is as hard as you want it to be.')
    print('Lets pick a number shall we?')
    topLimit = input()
    print('Now lets picks the amount of guesses you would like?')
    totalGuesses = input()
    thenumber = random.randint (1, topLimit)
    print('Now guess of a number between 1-' + topLimit + '. Good Luck!')


    if( showAnswer == True ):
        print('--shhh, the real number is ' + str(theNumber) + '.')
    if askUserToGuess(totalGuesses,theNumber) == True:
        print('Good job! You guessed my number!')
    else:
        print('Nope. The number I was thinking of was ' + str(theNumber))
