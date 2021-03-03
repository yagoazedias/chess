##-- FUNÇÕES AUXILIARES --##

#funcao na verdade é de house
def get_house(pos, board):
    row = pos[0]
    col = pos[1]
    return board[row][col]

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