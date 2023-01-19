from abc import ABC, abstractmethod
#classe Peça
class Piece(ABC): #classe abstrata para criar outras peças
    def __init__(self, name, unicode, is_black: bool, board: list, row, column):
        self._name = name
        self.unicode = unicode
        self._color = is_black
        self._table = board
        self.row = row
        self.column = column
        self._position = [self.row, self.column]

    @abstractmethod
    def moves(self):
        pass

    def put_piece(self):  #coloca Peça no tabuleiro[linha][coluna]
        self._table[self.row][self.column] = self.unicode

    def pegar_peca(self):
        self._table[self._position[0]][self._position[1]] = None

    def piece_moviments_dict(self): #método com os movimentos das peças
        self.dict_moviments = {
                                'vertical_down': [self._position[0] + 1, self._position[1]],
                                'vertical_up': [self._position[0] - 1, self._position[1]],
                                'horizontal_left': [self._position[0], self._position[1] - 1],
                                'horizontal_right': [self._position[0], self._position[1] + 1],
                                'diagonal_up_left': [self._position[0] - 1, self._position[1] - 1],
                                'diagonal_up_right': [self._position[0] - 1, self._position[1] + 1],
                                'diagonal_down_left': [self._position[0] + 1, self._position[1] - 1],
                                'diagonal_down_right': [self._position[0] + 1, self._position[1] + 1]
                               }

    def checa_limite(self):
        limit_dict = {
                       'vertical_down': [7 - self._position[0], self._position[1]],
                       'vertical_up': [(7 + self._position[0]) - 7, self._position[1]],
                       'horizontal_left': [self._position[0], (7 + self._position[1]) - 7],
                       'horizontal_right': [self._position[0], (7 - self._position[1] + 1) - 1],
                       'diagonal_up_left': [(7 + self._position[0]) - 7, (7 + self._position[1]) - 7],
                       'diagonal_up_right': [(7 + self._position[0]) - 7, (7 - self._position[1] + 1) - 1],
                       'diagonal_down_left': [7 - self._position[0], (7 + self._position[1]) - 7],
                       'diagonal_down_right': [7 - self._position[0], (7 - self._position[1] + 1) - 1]
                      }
        for i in limit_dict.items():
            print(i)

    def __len__(self):
        return self._table

    def pieces_moviments(self):
        if self._name == 'king':
            pass

    def _move(self, opt):
        self.pegar_peca()
        self.piece_moviments_dict()
        if opt == 1:
            self._table[self.dict_moviments['vertical_down'][0]][self.dict_moviments['vertical_down'][1]] = self.unicode
            self._position = [self.dict_moviments['vertical_down'][0], self.dict_moviments['vertical_down'][1]]

    
