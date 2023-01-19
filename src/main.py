from utils.organize_board import *
from class_piece.piece import Piece

opt = 1

#put_all_pieces()
b_king.put_piece()
board.show_board()

print('\n')

opt = 1

b_king._move(opt)
board.show_board()
print('\n')

b_king.checa_limite()

