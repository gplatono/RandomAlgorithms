import random


class TicTacToe:
    class Board:
        def __init__(self, dim=3):
            self.dim = dim
            self.board_state = 0
        
        def __iter__(self):           
            return self
        
        def __next__(self):
            if self.board_state == 2 ** (self.dim * self.dim):
                raise StopIteration

            result = []
            current = self.board_state
            for i in range(self.dim * self.dim):
                if ((i % self.dim) == 0):
                    result.append([])                

                if (current % 2 == 0):
                    result[-1].append('x')
                else:
                    result[-1].append('o')

                current //= 2
            
            self.board_state += 1
            return result

    def __init__(self, dim=3):
        self.dim = dim
        #self.reset_board()

    # def reset_board(self):
    #     self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def check_winner(self, board, player='x'):
        """
        Check if the given player ('x' or 'o') has a winning row/column/diagonal.
        """
        for row in board:
            if all(i == player for i in row):
                return True               
        
        for i in range(len(board)):
            col_win = True
            for j in range(len(board)):
                if board[i][j] != player:
                    col_win = False
            if col_win:
                return True                

        d1_win = True
        d2_win = True
        for i in range(len(board)):
            if board[i][i] != player:
                d1_win = False
            if board[i][-1-i] != player:
                d2_win = False

        if d1_win or d2_win:
            return True
        
        return False
            
    def return_winner(self, board):
        x_wins = self.check_winner(board, 'x')
        o_wins = self.check_winner(board, 'o') 
        if x_wins and not o_wins:
            return 'x'
        elif not x_wins and o_wins:
            return 'o'
        else:
            return -1

    def count_win_combinations(self):
        """
        Computes the number of end game configurations in which either X or O 
        is a winner (i.e., exactly X or O has a row/column/diagonal filled).
        """

        boards = iter(self.Board(self.dim))        
        x_wins = 0
        o_wins = 0
        for board in boards:
            winner = self.return_winner(board)
            if winner == 'x':
                x_wins += 1                
            elif winner == 'o':
                o_wins += 1
                
        return {'x': x_wins, 'o': o_wins}

    def win_prob1(self):
        """
        This function computes the probability, for each player, that that player wins given the following random game scheme:
            For every cell of the board, we flip a coin and assign the mark based on the outcome.
            The player is consider a winner if they have a filled row/column/diaglonal, but the other
            player does not.
        """
        win_combinations = self.count_win_combinations()
        return {'x': win_combinations['x'] / 2 ** (self.dim * self.dim), 'o': win_combinations['o'] / 2 ** (self.dim * self.dim)}

    def win_prob2(self):
        """
        This function computes the probability, for each player, that that player wins given the following random game scheme:
            The players take turns with X starting. At their turn, each player places their mark uniformly at random into one
            of the free cells.
        """
        return random.randint(10, 20)
        #return win_combinations = random.randint(10,20)
        #return {'x': win_combinations['x'] / 2 ** (self.dim * self.dim), 'o': win_combinations['o'] / 2 ** (self.dim * self.dim)}

ttt = TicTacToe(3)
print (ttt.win_prob2())