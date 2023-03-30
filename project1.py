import random
from os import system, name

def main():
    word = rWord()
    lives = 6
    bList = ["_" for i in range(len(word))]
    guessedList = []
    notList = []
    while(True):
        system('cls')
        print(boardState(lives))
        printList(bList, notList)
        playing = checkWin(lives, word, bList)
        if playing == False:
            ans = input("Want to play again (y/n): ")
            if ans == "n":
                return False
            else:
                word = rWord()
                lives = 6
                bList = ["_" for i in range(len(word))]
                guessedList = []
                notList = []
                continue
        guess = wGuess(guessedList)
        boardList(word, bList, guessedList)
        lives = inWord(lives, word, guess, notList)

def checkWin(lives, word, bList):
    if "_" not in bList and lives > 0:
        print("YOU WON!!!")
        return False
    elif lives == 0:
        print("\nYOU LOST!\nThe word was", word,"\n")
        return False
    else:
        return True

def wGuess(guessedList):
    while True:    
        guess = input("Guess a letter: ")
        if guess not in guessedList:
            guessedList.append(guess)
            return guess
        else:
            print("\nYou already tried that letter!\n")

def inWord(lives, word, guess, notList):
    if guess not in word:
        lives = lives - 1
        notList.append(guess)
    return lives

def boardList(word, bList, guessedList):
    wList = list(word)
    for i in range(len(wList)):
        if wList[i] == guessedList[-1]:
            bList[i] = wList[i]
    return bList

def rWord():
    f = open("scrabble.txt", "r")
    word_list = f.readlines()
    rLine = int(random.uniform(0, len(word_list)))
    word = word_list[rLine].strip()
    f.close()
    return word

def boardState(lives):
    if lives == 6:
        return """ 
             ________
            |        |
            |     
            |
            |
            |
          ________
        """
    elif lives == 5:
        return """ 
             ________
            |        |
            |        O
            |
            |
            |
          ________
        """
    elif lives == 4:
        return """ 
             ________
            |        |
            |        O
            |        |
            |
            |
          ________
        """
    elif lives == 3:
        return """ 
             ________
            |        |
            |        O
            |      --|
            |
            |
          ________
        """
    elif lives == 2:
        return """ 
             ________
            |        |
            |        O
            |      --|--
            |
            |
          ________
        """
    elif lives == 1:
        return """ 
             ________
            |        |
            |        O
            |      --|--
            |       /
            |
          ________
        """
    elif lives == 0:
        return """ 
             ________
            |        |
            |        O
            |      --|--
            |       / \\
            |
          ________
        """

def printList(bList, notList):
    print()
    for i in bList:
        print(i+" ", end="")
    print("\t\t\t\t\t\t", notList)
    print("\n")

if __name__ == "__main__":
    main()