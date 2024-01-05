import os


class TicTacToeGame:
    def __init__(self):
        self.spots = {1: '1️⃣', 2: '2️⃣', 3: '3️⃣', 4: '4️⃣', 5: '5️⃣', 6: '6️⃣', 7: '7️⃣', 8: '8️⃣', 9: '9️⃣'}
        self.winning_combs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.winner = None
        self.turn = 0
        self.prev_turn = -1
        self.player_1 = {
            "name": 'Player 1',
            "mark": '❌',
            "spots": []
        }
        self.player_2 = {
            "name": 'Player 2',
            "mark": '⭕',
            "spots": []
        }

    def draw_board(self):
        board = f'''
     {self.spots[1]} ¦ {self.spots[2]} ¦ {self.spots[3]} 
    --------------
     {self.spots[4]} ¦ {self.spots[5]} ¦ {self.spots[6]} 
    --------------
     {self.spots[7]} ¦ {self.spots[8]} ¦ {self.spots[9]} 
    '''
        os.system('cls' if os.name == 'nt' else 'clear')
        print(board)

    def make_move(self, move):
        """
        Updates game board, current and previous turn
        :param move: player's move
        """
        self.prev_turn = self.turn

        if self.is_valid_move(move):
            move = int(move)
            self.turn += 1
            if self.turn % 2 == 0:
                self.player_2["spots"].append(move)
                self.spots[move] = self.player_2["mark"]
            else:
                self.player_1["spots"].append(move)
                self.spots[move] = self.player_1["mark"]

    def is_valid_move(self, move):
        """
        Checks if move is an available spot on game board
        :param move: player's move
        :return: True/False
        """
        if str.isdigit(move) and int(move) in self.spots:
            if not self.spots[int(move)] in {self.player_1["mark"], self.player_2["mark"]}:
                return True
        return False

    def check_for_win(self):
        """
        Updates 'winner' variable if one the players won
        """
        for comb in self.winning_combs:
            if set(comb).issubset(self.player_1["spots"]):
                self.winner = self.player_1
            elif set(comb).issubset(self.player_2["spots"]):
                self.winner = self.player_2

