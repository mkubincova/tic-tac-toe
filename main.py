import os
from tic_tac_toe import TicTacToeGame


game = TicTacToeGame()

playing = True
complete = False

while playing:
    game.draw_board()

    if game.prev_turn == game.turn:
        print("🚫 Invalid spot selected, please pick another.")

    # Get players move
    print(f"Player {(game.turn % 2) + 1}'s turn, pick spot (or press 'q' to quit): ")
    choice = input()

    if choice == 'q':
        playing = False
    else:
        game.make_move(choice)
        game.check_for_win()

    if game.winner:
        playing = False
        complete = True
    if game.turn > 8:
        playing = False

# Reset screen
os.system('cls' if os.name == 'nt' else 'clear')
game.draw_board()

if complete:
    print(f"{game.winner['mark']} {game.winner['name']} wins!")
else:
    print("🤝 No winner, it's a tie.")

print("⭐ Thanks for playing! ⭐")
