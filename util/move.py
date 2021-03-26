##-- FUNÇÕES AUXILIARES --##

# retorna a posicao à direita de pos
def right(pos):
    col = pos[0] + 1
    row = pos[1]
    return col, row


# retorna a posicao à esquerda de pos
def left(pos):
    col = pos[0] - 1
    row = pos[1]
    return col, row


# retorna a posicao 'acima' de pos
def up(pos):
    col = pos[0]
    row = pos[1] - 1
    return col, row


# retorna a posicao abaixo de pos
def down(pos):
    col = pos[0]
    row = pos[1] + 1
    return col, row


# retorna a posicao da 'diagonal direita superior' de pos
def up_right(pos):
    col = pos[0] + 1
    row = pos[1] - 1
    return col, row


# retorna a posicao da 'diagonal esquerda superior' de pos
def up_left(pos):
    col = pos[0] - 1
    row = pos[1] - 1
    return col, row


# retorna a posicao da 'diagonal direita inferior' de pos
def down_right(pos):
    col = pos[0] + 1
    row = pos[1] + 1
    return col, row


# retorna a posicao da 'diagonal esquerda inferior' de pos
def down_left(pos):
    col = pos[0] - 1
    row = pos[1] + 1
    return col, row


# dada uma posicao, retorna todas as casas validas 'para cima'
def all_up_moves(pos, match, my_color):
    moves = []
    pos = up(pos)
    while is_valid_pos(pos) and match.board.is_empty(pos):
        moves.append(pos)
        pos = up(pos)

    if is_valid_pos(pos) and match.board.has_opponent(pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas 'para direita'
def all_right_moves(pos, match, my_color):
    moves = []
    pos = right(pos)
    while is_valid_pos(pos) and match.board.is_empty(pos):
        moves.append(pos)
        pos = right(pos)

    if is_valid_pos(pos) and match.board.has_opponent(pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas 'para baixo'
def all_down_moves(pos, match, my_color):
    moves = []
    pos = down(pos)
    while is_valid_pos(pos) and match.board.is_empty(pos):
        moves.append(pos)
        pos = down(pos)

    if is_valid_pos(pos) and match.board.has_opponent(pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas 'para esquerda'
def all_left_moves(pos, match, my_color):
    moves = []
    pos = left(pos)
    while is_valid_pos(pos) and match.board.is_empty(pos):
        moves.append(pos)
        pos = left(pos)

    if is_valid_pos(pos) and match.board.has_opponent(pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas para 'diagonal superior direita'
def all_up_right_moves(pos, match, my_color):
    moves = []
    pos = up_right(pos)
    while is_valid_pos(pos) and match.board.is_empty(pos):
        moves.append(pos)
        pos = up_right(pos)

    if is_valid_pos(pos) and match.board.has_opponent(pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas para 'diagonal superior esquerda'
def all_up_left_moves(pos, match, my_color):
    moves = []
    pos = up_left(pos)
    while is_valid_pos(pos) and match.board.is_empty(pos):
        moves.append(pos)
        pos = up_left(pos)

    if is_valid_pos(pos) and match.board.has_opponent(pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas para 'diagonal inferior esquerda'
def all_down_left_moves(pos, match, my_color):
    moves = []
    pos = down_left(pos)
    while is_valid_pos(pos) and match.board.is_empty(pos):
        moves.append(pos)
        pos = down_left(pos)

    if is_valid_pos(pos) and match.board.has_opponent(pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas para 'diagonal inferior direita'
def all_down_right_moves(pos, match, my_color):
    moves = []
    pos = down_right(pos)
    while is_valid_pos(pos) and match.board.is_empty(pos):
        moves.append(pos)
        pos = down_right(pos)

    if is_valid_pos(pos) and match.board.has_opponent(pos, my_color):
        moves.append(pos)

    return moves


# verifica se a posicao pos é valida. ou seja, esta dentro dos limites do tabuleiro
def is_valid_pos(pos):
    col = pos[0]
    row = pos[1]
    return 0 <= row <= 7 and 0 <= col <= 7


# verifica se a posicao pos tem um companheiro de equipe
def has_teammate(pos, my_color, board):
    if not is_valid_pos(pos):
        return False
    if board.get_house(pos).get_piece() is None:
        return False
    return my_color == board.get_house(pos).get_piece().get_color()


    # verifica se a posicao pos tem um oponente
def has_opponent(board, house, piece_color):
    if house.get_piece() is None:
        return False
    return piece_color != house.get_piece().get_color()