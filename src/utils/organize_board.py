from class_piece.all_pieces import *
from class_piece.piece import Piece
from board.board import Board

board = Board()
display = board.display_board()

b_king = King('king', '\U0000265A', True, display, 0, 4)
b_queen = Queen('queen', '\U0000265B', True, display, 0, 3)
b_left_bishop = Bishop('bishop', '\U0000265D', True, display, 0, 2)
b_right_bishop = Bishop('bishop', '\U0000265D', True, display, 0, 5)
b_left_horse = Horse('horse', '\U0000265E', True, display, 0, 1)
b_right_horse = Horse('horse', '\U0000265E', True, display, 0, 6)
b_left_tower = Tower('tower', '\U0000265C', True, display, 0, 0)
b_right_tower = Tower('tower', '\U0000265C', True, display, 0, 7)

b_peon_1 = Peon('b_peon_1', '\U0000265F', True, display, 1, 0)
b_peon_2 = Peon('b_peon_2', '\U0000265F', True, display, 1, 1)
b_peon_3 = Peon('b_peon_3', '\U0000265F', True, display, 1, 2)
b_peon_4 = Peon('b_peon_4', '\U0000265F', True, display, 1, 3)
b_peon_5 = Peon('b_peon_5', '\U0000265F', True, display, 1, 4)
b_peon_6 = Peon('b_peon_6', '\U0000265F', True, display, 1, 5)
b_peon_7 = Peon('b_peon_7', '\U0000265F', True, display, 1, 6)
b_peon_8 = Peon('b_peon_8', '\U0000265F', True, display, 1, 7)

w_king = King('king', '\U00002654', False, display, 7, 4)
w_queen = Queen('queen', '\U00002655', False, display, 7, 3)
w_left_bishop = Bishop('bishop', '\U00002657', False, display, 7, 2)
w_right_bishop = Bishop('bishop', '\U00002657', False, display, 7, 5)
w_left_horse = Horse('horse', '\U00002658', False, display, 7, 1)
w_right_horse = Horse('horse', '\U00002658', False, display, 7, 6)
w_left_tower = Tower('tower', '\U00002656', False, display, 7, 0)
w_right_tower = Tower('tower', '\U00002656', False, display, 7, 7)

w_peon_1 = Peon('w_peon_1', '\U00002659', False, display, 6, 0)
w_peon_2 = Peon('w_peon_2', '\U00002659', False, display, 6, 1)
w_peon_3 = Peon('w_peon_3', '\U00002659', False, display, 6, 2)
w_peon_4 = Peon('w_peon_4', '\U00002659', False, display, 6, 3)
w_peon_5 = Peon('w_peon_5', '\U00002659', False, display, 6, 4)
w_peon_6 = Peon('w_peon_6', '\U00002659', False, display, 6, 5)
w_peon_7 = Peon('w_peon_7', '\U00002659', False, display, 6, 6)
w_peon_8 = Peon('w_peon_8', '\U00002659', False, display, 6, 7)

all_pieces = {b_king, b_queen, b_left_bishop, b_right_bishop, b_left_horse, b_right_horse, b_left_tower, b_right_tower,
              b_peon_1, b_peon_2, b_peon_3, b_peon_4, b_peon_5, b_peon_6, b_peon_7, b_peon_8, w_king, w_queen, w_left_bishop,
              w_right_bishop, w_left_horse, w_right_horse, w_left_tower, w_right_tower, w_peon_1, w_peon_2, w_peon_3, w_peon_4, 
              w_peon_5, w_peon_6, w_peon_7, w_peon_8}

def put_all_pieces():
    for piece in all_pieces:
        piece.put_piece()
