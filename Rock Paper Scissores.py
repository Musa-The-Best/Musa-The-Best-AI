import random
from colorama import Fore, Style, init

init(autoreset=True)

# Possible choices
choices = ["rock", "paper", "scissors"]

# AI strategy: remembers player's last move and tries to counter it
player_history = []

def get_ai_move():
    if not player_history:
        return random.choice(choices)
    last_move = player_history[-1]
    if last_move == "rock":
        return "paper"
    elif last_move == "paper":
        return "scissors"
    else:
        return "rock"

def get_result(player, ai):
    if player == ai:
        return "draw"
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return "win"
    else:
        return "lose"

def play_game():
    print(Fore.CYAN + "Welcome to Rock Paper Scissors!")
    print("Type rock, paper, or scissors to play. Type 'exit' to quit.\n")

    while True:
        player = input(Fore.WHITE + "Your move: ").lower()

        if player == "exit":
            print(Fore.YELLOW + "Thanks for playing! Goodbye.")
            break

        if player not in choices:
            print(Fore.RED + "Invalid move. Try again.")
            continue

        ai_move = get_ai_move()
        player_history.append(player)

        print(f"AI chose: {Fore.MAGENTA + ai_move}")
        result = get_result(player, ai_move)

        if result == "win":
            print(Fore.GREEN + "You win!")
        elif result == "lose":
            print(Fore.RED + "You lose!")
        else:
            print(Fore.YELLOW + "It's a draw!")

if __name__ == "__main__":
    play_game()
