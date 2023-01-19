#classe tabuleiro
class Board:
    def __init__(self): #metodo construtor
        self._board = [[None for row in range(8)] for house in range (8)]
    #mostra a matriz do tabuleiro
    def show_board(self):
        for row in self._board:
            print(row)
    #retorna o Objeto Board como uma matriz
    def display_board(self):
        board = []
        for row in self._board:
            board.append(row)
        return board
