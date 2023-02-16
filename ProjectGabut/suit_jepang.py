import random

def botGuess():
    botRandom = random.randint(1,3)
    if botRandom == 1 : return "Gunting"
    if botRandom == 2 : return "Batu"
    if botRandom == 3 : return "Kertas"

def userGuess():
    return input("Pilih Gunting, Batu, Kertas : ")

def gameRules(userGuess, botGuess):
    if userGuess == botGuess : return "Seri"

    if userGuess == "Gunting":
        if botGuess == "Batu": return "Kalah"
        if botGuess == "Kertas": return "Menang"
    elif userGuess == "Batu":
        if botGuess == "Gunting": return "Menang"
        if botGuess == "Kertas": return "Kalah"
    elif userGuess == "Kertas":
        if botGuess == "Batu": return "Menang"
        if botGuess == "Gunting": return "Kalah"
if __name__ == '__main__':
    bot = botGuess()
    user = userGuess()
    print("===\nAnda ",gameRules(user,bot),"\n===")
    print("User memilih ", user)
    print("Bot memilih ", bot)