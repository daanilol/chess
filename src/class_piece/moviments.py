from class_piece.piece import Piece

class Rules:
    def __init__(self, piece, directions):
        self.piece = piece
        self.directions = directions

    def king_queen_moviments(self):
        king_queen_moves = ['vertical_move_up', 'vertical_move_down',
                      'horizontal_move_left', 'horizontal_move_right',
                      'diagonal_move_up_left', 'diagonal_move_up_right',
                      'diagonal_move_down_left', 'diagonal_move_down_right']
        return king_queen_moves

    def bishop_moviments(self):
        bishop_moves = ['diagonal_move_up_left', 'diagonal_move_up_right', 
                        'diagonal_move_down_left', 'diagonal_move_down_right']
        return bishop_moves

    def horse_moviments(self):
        horse_moves = []

    def tower_moviments(self):
        tower_moves = ['vertical_move_up', 'vertical_move_down', 
                      'horizontal_move_left', 'horizontal_move_right']
        return tower_moves

    def peon_moviments(self):
        peon_moves = ['vertical_move_up', 
                          'diagonal_move_up_left', 
                          'diagonal_move_up_right']
        return peon_moves
