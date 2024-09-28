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

print_Game_Board()






# definice prniho hrace (realneho) + moznost volby 
# osetrit spatne volby a upozornit na ne 
# na pole kde uz neco je nejde dat neco dalsiho 






# definice 2 hrace (pc) knihovna random 







# po kazde spravne volbe dojde k zobrazeni pole 









# horizontalni, vert a diagonalni kontrola zda uz jeden hrac nema 3 










# bez volneho pole dojde k remize 










