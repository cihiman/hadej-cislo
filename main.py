import random
from art import logo
from replit import clear


EASY = 10
HARD = 5

def new_game():
    new_game = input("Chcete hrát znovu? ano / ne: ")
    if new_game == "ano":
        game()
    if new_game == "ne":
        print("Díky za hru!")
        
def clear_screen():
    clear()
    print(logo)

def set_difficulty():
    level = input("Vyberte obtížnost: lehka, tezka: ")
    if level == "lehka":
        return EASY
    if level == "tezka":
        return HARD

def game_check(guess, answer, turn):
    if guess > answer:
        clear_screen()
        print("Moc vysoko!")
        return turn - 1
    if guess < answer:
        clear_screen()
        print("Moc nízko!")
        return turn - 1
    else:
        clear_screen()
        print(f"Správně, uhodli jste náhodné číslo: {answer}!")
        new_game()

def game():
    turn = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"Zbývá Vám {turn} pokusů!")
        guess = int(input("Hádej: "))
        turn = game_check(guess, answer, turn)
        if turn == 0:
            print(f"Máte {turn} pokusů, KONEC HRY!")
            return
        
print(logo)
print("Vítejte ve hře!")
print("Myslím si číslo mezi 1 až 100...")
answer = random.randint(1,100)
print(f"Psst, odpověď je: {answer}!")
game()

    
