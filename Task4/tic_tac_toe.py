import random


class Player:
    """Base player class"""

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError("Subclasses must implement make_move")


class HumanPlayer(Player):
    """Human player asks for input"""

    def make_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name} ({self.symbol}), choose position (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid input. Choose 1-9.")
                    continue
                if board.update(move, self.symbol):
                    break
                else:
                    print("That spot is already taken, try again.")
            except ValueError:
                print("Please enter a valid number.")


class ComputerPlayer(Player):
    """Computer player makes a random move"""

    def make_move(self, board):
        move = random.choice([i for i, x in enumerate(board._cells) if x not in ["X", "O"]])
        board.update(move, self.symbol)
        print(f"{self.name} ({self.symbol}) chose position {move+1}")


class Board:
    """Game board"""

    def __init__(self):
        # At the start, cells are numbered 1–9
        self._cells = [str(i + 1) for i in range(9)]

    def __str__(self):
        return (
            f"\n {self._cells[0]} | {self._cells[1]} | {self._cells[2]} \n"
            f"---+---+---\n"
            f" {self._cells[3]} | {self._cells[4]} | {self._cells[5]} \n"
            f"---+---+---\n"
            f" {self._cells[6]} | {self._cells[7]} | {self._cells[8]} \n"
        )

    def display(self):
        print(self)

    def update(self, position, symbol):
        """Update a cell if it's empty"""
        if self._cells[position] not in ["X", "O"]:
            self._cells[position] = symbol
            return True
        return False

    def check_winner(self, symbol):
        """Check if a player with `symbol` has won"""
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(self._cells[i] == symbol for i in combo) for combo in wins)

    def is_full(self):
        """Check if the board is full"""
        return all(cell in ["X", "O"] for cell in self._cells)


class Game:
    """Main game logic"""

    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_turn = 0

    def switch_turns(self):
        """Switch between players"""
        self.current_turn = 1 - self.current_turn

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        mode = input("Do you want to play with a friend (1) or vs computer (2)? ")

        if mode == "1":
            name1 = input("Enter name for Player 1: ")
            name2 = input("Enter name for Player 2: ")
            self.players = [HumanPlayer(name1, "X"), HumanPlayer(name2, "O")]
        else:
            name = input("Enter your name: ")
            self.players = [HumanPlayer(name, "X"), ComputerPlayer("Computer", "O")]

        self.board.display()

        while True:
            player = self.players[self.current_turn]
            player.make_move(self.board)
            self.board.display()

            if self.board.check_winner(player.symbol):
                print(f"{player.name} wins!")
                break

            if self.board.is_full():
                print("It's a draw!")
                break

            self.switch_turns()


if __name__ == "__main__":
    Game().play()
