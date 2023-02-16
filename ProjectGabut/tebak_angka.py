import random
import os
randomNumber = random.randint(1,100)

def tryBlock():
    i = 20
    userInput = 0
    while(True):
        userInput = int(input("Tebak Nilai : "))
        os.system('cls')
        if userInput == randomNumber:
            print("Tebakan anda Tepat!")
            break;
        elif userInput < randomNumber :
            print("Tebakan lebih kecil")
        elif userInput > randomNumber :
            print("Tebakan lebih besar")
        
if __name__ == "__main__":
    tryBlock()