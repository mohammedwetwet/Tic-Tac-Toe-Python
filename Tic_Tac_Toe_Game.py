import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    
    def choice_name(self):
        while True:
            name = input("Please enter your name: ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use Letters only")
    def choice_symbol(self):
        while True:
            symbol = input(f"{self.name}, please enter your symbol (a single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid Symbol. Please enter a single letter only. ")

class Menu:
    def main_menu(self):
        print("Welcome to my X-O game")
        print("1. Start Game")
        print("2. Quit Game ")
        while True:
            nas1 = input("Please Choice 1 or 2 :  ")
            if self.validate_choice(nas1):
                return nas1
            print("Please Choice 1 or 2 only ")
    def endgame_menu(self):
        print("Game Over")
        print("1. Restart Game")
        print("2. Quit Game ")
        while True:
            nas2 = input("Please Choice 1 or 2 :  ")
            if self.validate_choice(nas2):
                return nas2
            print("Please Choice 1 or 2 only ")

    def validate_choice(self,ch):
        if ch == "1":
            return True
        elif ch == "2":
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]

    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-"*5)
    
    def updata_board(self,choice,symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False
    
    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()
    
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]


class Game:
    def __init__(self):
        self.players = [Player(),Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else :
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players ,start = 1):
            print(f"Player {number}, Pls enter your details ")
            player.choice_name()
            player.choice_symbol()
            clear_screen()
            if number == 0 :
                print("-"*30)
                print("-"*30)
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def check_draw(self):
        if (all(not cell.isdigit() for cell in self.board.board)):
            print("No one wins (a Draw)")
            return True

    def check_win(self):
        win_combinations = [
            [0,1,2],[3,4,5],[6,7,8], # rows
            [0,3,6],[1,4,7],[2,5,8], # columns
            [0,4,8],[2,4,6]          # diagonals 
        ]
        for combo in win_combinations:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                player = self.players[self.current_player_index-1]
                clear_screen()
                (self.board.display_board())
                print(f"({player.symbol}) {player.name} is the Winner ")
                return True
        return False

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("choice a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.updata_board(cell_choice,player.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Pls enter a number between 1 and 9 ")
        self.switch_player()


    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self):
        print("Thank You for Playing")
        quit()
 

g = Game()
g.start_game()
