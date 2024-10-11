"""
Tic-tac-toe Game
projekt_2: druhý projekt do Engeto Online Python Akademie

autor: Vícha Dominik
email: dominik.vicha@gmail.com 
discord: Dominik V

"""


"""
ZADÁNÍ: 
2. program pozdraví uživatele,
3. vypíše v krátkosti pravidla hry,
4. zobrazí hrací plochu,
5. vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene,
6. pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní,
7. pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní,
8. pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené
9. jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy,
10. program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří,
11. pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu,
12. zápis organizovaný do krátkých a přehledných funkcí.

"""
# zabalit do funkce jako uvod

import random

print(f"\nWelcome to Tic Tac Toe.")
print(f"=" * 35)

game_rules = """
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
"""
print(game_rules)
print(f"=" * 35)

print("Let's start the game!")
print("-" * 35)

# funkce pro vytvoreni hraci plochy 

possible_numbers = [1,2,3,4,5,6,7,8,9]
game_board = [[1,2,3], [4,5,6], [7,8,9]]

rows = 3
cols = 3 


def print_Game_Board():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        
        for y in range(cols):
            print("", game_board[x][y], end=" |")
    print("\n+---+---+---+")


def modify_game_board(player): 
    global possible_numbers, game_board

    while True:

        if player == 'X':
            try:
                selected_number = input("Select number from the board: ")
                if not selected_number.isdigit():
                    print("Please eneter the numerical value")
                    continue

                selected_number = int(selected_number)
                if selected_number <1 or selected_number >9:
                    print("Enter the number between 1-9.")
                    continue
                if selected_number not in possible_numbers:
                    print("The cell youve selected is full.")
                    continue
            

            except ValueError:
                print("You selected wrong character, please enter a number.")
                continue
        
        else:
            selected_number = random.choice(possible_numbers)
            print(f"Pc selected: {selected_number}")

        
        for i in range(rows):
            for j in range(cols):
                if game_board[i][j] == selected_number:
                    game_board[i][j] = player 
                    possible_numbers.remove(selected_number) 
                    return True
                
    return False

def board_is_full():
    return len(possible_numbers) == 0


def play_game():
    global possible_numbers, game_board
    possible_numbers = list(range(1, 10))
    game_board = [[1,2,3], [4,5,6], [7,8,9]]

    print("\nStarting game board:")
    print_Game_Board()

    current_player = 'X'
    while True:
        if modify_game_board(current_player):
            print_Game_Board()
            winner = check_winner(game_board)
            if winner: 
                print(f"Player {winner} wins the game!")
                break
            if board_is_full():
                print("Its a tie! The field is full.")
                break
            current_player = '0' if current_player == 'X' else 'X'
        else:
            break


def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2] and row[0] in ['X', '0']:
            return row[0]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] in ['X', '0']:
            return board[0][col]
        
    if board [0][0] == board [1][1] == board [2][2] in ['X', '0']:
        return board[0][0]
    
    if board [0][2] == board [1][1] == board [2][0] in ['X', '0']:
        return board[0][2]

    return None

def main ():
    
    while True: 
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing.")
            break
        



if __name__ == "__main__":
    main()





# definice prniho hrace (realneho) + moznost volby 
# osetrit spatne volby a upozornit na ne 
# na pole kde uz neco je nejde dat neco dalsiho 

# definice 2 hrace (pc) knihovna random 



# po kazde spravne volbe dojde k zobrazeni pole 



# horizontalni, vert a diagonalni kontrola zda uz jeden hrac nema 3 


# bez volneho pole dojde k remize
