##-- FUNÇÕES AUXILIARES --##

# verifica se a posicao pos é valida. ou seja, esta dentro dos limites do tabuleiro
def is_valid_pos(pos):
    row = pos[0]
    col = pos[1]
    return (row >= 0 and row <= 7 and col >= 0 and col <= 7)

    
# verifica se a posicao pos tem peça branca (nao to usando)
def has_white(pos, board):
    row = pos[0]
    col = pos[1]
    return (board[row][col][0] == 'w')

# verifica se a posicao pos tem peça preta (nao to usando)
def has_black(pos, board):
    return (board[pos[0]][pos[1]][0] == 'b')

# verifica se a posicao pos tem um oponente
def has_oponent(pos, board):
    row = pos[0]
    col = pos[1]
    return get_color()[0] != board[row][col][0] and board[row][col][0] != '-'

# verifica se a posicao pos tem um companheiro de equipe
def has_teammate(pos, board):
    row = pos[0]
    col = pos[1]
    return get_color()[0] == board[row][col][0] and board[row][col][0] != '-'

# verifica se a posicao pos está vazia
def is_empty(pos, board):
    row = pos[0]
    col = pos[1]
    return (board[row][col] == '-')

# retorna a posicao à direita de pos
def right(pos):
    posy = pos[0]
    posx = pos[1]+1
    return (posy, posx)

# retorna a posicao à esquerda de pos
def left(pos):
    posy = pos[0]
    posx = pos[1]-1
    return (posy, posx)

# retorna a posicao 'acima' de pos
def up(pos):
    posy = pos[0]-1
    posx = pos[1]
    return (posy, posx)

# retorna a posicao abaixo de pos
def down(pos):
    posy = pos[0]+1
    posx = pos[1]
    return (posy, posx)

# retorna a posicao da 'diagonal direita superior' de pos
def up_right(pos):
    posy = pos[0]-1
    posx = pos[1]+1
    return (posy, posx)

# retorna a posicao da 'diagonal esquerda superior' de pos
def up_left(pos):
    posy = pos[0]-1
    posx = pos[1]-1
    return (posy, posx)

# retorna a posicao da 'diagonal direita inferior' de pos
def down_right(pos):
    posy = pos[0]+1
    posx = pos[1]+1
    return (posy, posx)

# retorna a posicao da 'diagonal esquerda inferior' de pos
def down_left(pos):
    posy = pos[0]+1
    posx = pos[1]-1
    return (posy, posx)

# dada uma posicao, retorna todas as casas validas 'para cima'
def all_up_moves(pos, board):
    moves = []
    pos = up(pos)
    while is_valid_pos(pos) and is_empty(pos, board):
        moves.append(pos)
        pos = up(pos)

    if is_valid_pos(pos) and has_oponent(pos, board):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas 'para direita'
def all_right_moves(pos, board):
    moves = []
    pos = right(pos)
    while is_valid_pos(pos) and is_empty(pos, board):
        moves.append(pos)
        pos = right(pos)

    if is_valid_pos(pos) and has_oponent(pos, board):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas 'para baixo'
def all_down_moves(pos, board):
    moves = []
    pos = down(pos)
    while is_valid_pos(pos) and is_empty(pos, board):
        moves.append(pos)
        pos = down(pos)

    if is_valid_pos(pos) and has_oponent(pos, board):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas 'para esquerda'
def all_left_moves(pos, board):
    moves = []
    pos = left(pos)
    while is_valid_pos(pos) and is_empty(pos, board):
        moves.append(pos)
        pos = left(pos)

    if is_valid_pos(pos) and has_oponent(pos, board):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas para 'diagonal superior direita'
def all_up_right_moves(pos, board):
    moves = []
    pos = up_right(pos)
    while is_valid_pos(pos) and is_empty(pos, board):
        moves.append(pos)
        pos = up_right(pos)

    if is_valid_pos(pos) and has_oponent(pos, board):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas para 'diagonal superior esquerda'
def all_up_left_moves(pos, board):
    moves = []
    pos = up_left(pos)
    while is_valid_pos(pos) and is_empty(pos, board):
        moves.append(pos)
        pos = up_left(pos)

    if is_valid_pos(pos) and has_oponent(pos, board):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas para 'diagonal inferior esquerda'
def all_down_left_moves(pos, board):
    moves = []
    pos = down_left(pos)
    while is_valid_pos(pos) and is_empty(pos, board):
        moves.append(pos)
        pos = down_left(pos)

    if is_valid_pos(pos) and has_oponent(pos, board):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas para 'diagonal inferior direita'
def all_down_right_moves(pos, board):
    moves = []
    pos = down_right(pos)
    while is_valid_pos(pos) and is_empty(pos, board):
        moves.append(pos)
        pos = down_right(pos)

    if is_valid_pos(pos) and has_oponent(pos, board):
        moves.append(pos)

    return moves

def rook_valid_moves(pos, board):
    moves = all_down_moves(pos, board) + \
        all_up_moves(pos, board) + \
        all_right_moves(pos, board) + \
        all_left_moves(pos, board)
    return moves

def bishop_valid_moves(pos, board):
    moves = all_down_left_moves(pos, board) + \
        all_down_right_moves(pos, board) + \
        all_up_right_moves(pos, board) + \
        all_up_left_moves(pos, board)
    return moves

def queen_valid_moves(pos, board):
    moves = bishop_valid_moves(pos, board) + rook_valid_moves(pos, board)
    return moves


# retorna os 2 L's: |--
def knight_left_L(pos, board):
    row = pos[0]
    col = pos[1]
    l_up = (row-1, col-2)
    l_down = (row+1, col-2)
    return [l_up, l_down]

# retorna os 2 L's: --|
def knight_right_L(pos, board):
    row = pos[0]
    col = pos[1]
    r_up = (row-1, col+2)
    r_down = (row+1, col+2)
    return [r_up, r_down]

# retorna os 2 L's: _|_
def knight_down_L(pos, board):
    row = pos[0]
    col = pos[1]
    d_left = (row+2, col-1)
    d_right = (row+2, col+1)
    return [d_left, d_right]

# retorna os 2 L's: T
def knight_up_L(pos, board):
    row = pos[0]
    col = pos[1]
    u_left = (row-2, col-1)
    u_right = (row-2, col+1)
    return [u_left, u_right]

#retorna todos os movimentos validos de um cavalo, dada uma posicao
def knight_valid_moves(pos, board):
    moves = knight_down_L(pos, board) + knight_up_L(pos, board) \
        + knight_left_L(pos, board) + knight_right_L(pos, board)

    invalid_moves = []
    for move in moves:
        if not(is_valid_pos(move)) or has_teammate(move, board):
            invalid_moves.append(move)
    
    moves = [x for x in moves if x not in invalid_moves]

    return moves


def pawn_valid_moves(pos, board, color, first_move):
    moves = []
    first_move = first_move
    if color == 'white':
        pawn_move = up
        diag_right_house = up_right(pos)
        diag_left_house = up_left(pos)
    elif color == 'black':
        pawn_move = down
        diag_right_house = down_right(pos)
        diag_left_house = down_left(pos)

    move_front = pawn_move(pos)
    if is_valid_pos(move_front) and is_empty(move_front, board):
        moves.append(move_front)
        if first_move:
            first_move = False
            move_front = pawn_move(move_front)
            if is_valid_pos(move_front) and is_empty(move_front, board):
                moves.append(move_front)
    
    if is_valid_pos(diag_left_house) and has_oponent(diag_left_house, board):
        moves.append(diag_left_house)

    if is_valid_pos(diag_right_house) and has_oponent(diag_right_house, board):
        moves.append(diag_right_house)

    return moves

#retorna todos os movimentos validos de um rei, dada uma posicao (sem roque)
def king_valid_moves(pos, board):
    moves = [up(pos), down(pos), left(pos), right(pos), up_left(pos), 
            up_right(pos), down_left(pos), down_right(pos)]
    
    invalid_moves = []
    for move in moves:
        if not(is_valid_pos(move)) or has_teammate(move, board):
            invalid_moves.append(move)
    
    moves = [x for x in moves if x not in invalid_moves]
    return moves
