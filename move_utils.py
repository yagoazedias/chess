##-- FUNÇÕES AUXILIARES --##

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
def all_up_moves(pos, board, my_color):
    moves = []
    pos = up(pos)
    while board.is_valid_pos(pos) and board.is_empty(pos):
        moves.append(pos)
        pos = up(pos)

    if board.is_valid_pos(pos) and board.has_oponent(pos, my_color):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas 'para direita'
def all_right_moves(pos, board, my_color):
    moves = []
    pos = right(pos)
    while board.is_valid_pos(pos) and board.is_empty(pos):
        moves.append(pos)
        pos = right(pos)

    if board.is_valid_pos(pos) and board.has_oponent(pos, my_color):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas 'para baixo'
def all_down_moves(pos, board, my_color):
    moves = []
    pos = down(pos)
    while board.is_valid_pos(pos) and board.is_empty(pos):
        moves.append(pos)
        pos = down(pos)

    if board.is_valid_pos(pos) and board.has_oponent(pos, my_color):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas 'para esquerda'
def all_left_moves(pos, board, my_color):
    moves = []
    pos = left(pos)
    while board.is_valid_pos(pos) and board.is_empty(pos):
        moves.append(pos)
        pos = left(pos)

    if board.is_valid_pos(pos) and board.has_oponent(pos, my_color):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas para 'diagonal superior direita'
def all_up_right_moves(pos, board, my_color):
    moves = []
    pos = up_right(pos)
    while board.is_valid_pos(pos) and board.is_empty(pos):
        moves.append(pos)
        pos = up_right(pos)

    if board.is_valid_pos(pos) and board.has_oponent(pos, my_color):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas para 'diagonal superior esquerda'
def all_up_left_moves(pos, board, my_color):
    moves = []
    pos = up_left(pos)
    while board.is_valid_pos(pos) and board.is_empty(pos):
        moves.append(pos)
        pos = up_left(pos)

    if board.is_valid_pos(pos) and board.has_oponent(pos, my_color):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas para 'diagonal inferior esquerda'
def all_down_left_moves(pos, board, my_color):
    moves = []
    pos = down_left(pos)
    while board.is_valid_pos(pos) and board.is_empty(pos):
        moves.append(pos)
        pos = down_left(pos)

    if board.is_valid_pos(pos) and board.has_oponent(pos, my_color):
        moves.append(pos)

    return moves

# dada uma posicao, retorna todas as casas validas para 'diagonal inferior direita'
def all_down_right_moves(pos, board, my_color):
    moves = []
    pos = down_right(pos)
    while board.is_valid_pos(pos) and board.is_empty(pos):
        moves.append(pos)
        pos = down_right(pos)

    if board.is_valid_pos(pos) and board.has_oponent(pos, my_color):
        moves.append(pos)

    return moves