##-- FUNÇÕES AUXILIARES --##

# retorna a posicao à direita de pos
def right(pos):
    row = pos[0]
    col = pos[1] + 1
    return row, col


# retorna a posicao à esquerda de pos
def left(pos):
    row = pos[0] 
    col = pos[1] - 1
    return row, col


# retorna a posicao 'acima' de pos
def up(pos):
    row = pos[0] - 1
    col = pos[1] 
    return row, col


# retorna a posicao abaixo de pos
def down(pos):
    row = pos[0] + 1
    col = pos[1] 
    return row, col


# retorna a posicao da 'diagonal direita superior' de pos
def up_right(pos):
    row = pos[0] - 1
    col = pos[1] + 1
    return row, col


# retorna a posicao da 'diagonal esquerda superior' de pos
def up_left(pos):
    row = pos[0] - 1
    col = pos[1] - 1
    return row, col


# retorna a posicao da 'diagonal direita inferior' de pos
def down_right(pos):
    row = pos[0] + 1
    col = pos[1] + 1
    return row, col


# retorna a posicao da 'diagonal esquerda inferior' de pos
def down_left(pos):
    row = pos[0] + 1
    col = pos[1] - 1
    return row, col

def is_empty(board, pos):
    row = pos[0]
    col = pos[1]
    return board[row][col] == 0

def has_opponent(board, pos, my_color):
    piece = get_piece(board, pos)
    if my_color > 0:    
        if piece < 0:
            return True
    if my_color < 0:
        if piece > 0:
            return True
    return False

# dada uma posicao, retorna todas as casas validas 'para cima'
def all_up_moves(board, pos, my_color):
    moves = []
    pos = up(pos)
    while is_valid_pos(pos) and is_empty(board, pos):
        moves.append(pos)
        pos = up(pos)

    if is_valid_pos(pos) and  has_opponent(board, pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas 'para direita'
def all_right_moves(board, pos, my_color):
    moves = []
    pos = right(pos)
    while is_valid_pos(pos) and is_empty(board, pos):
        moves.append(pos)
        pos = right(pos)

    if is_valid_pos(pos) and  has_opponent(board, pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas 'para baixo'
def all_down_moves(board, pos, my_color):
    moves = []
    pos = down(pos)
    while is_valid_pos(pos) and is_empty(board, pos):
        moves.append(pos)
        pos = down(pos)

    if is_valid_pos(pos) and  has_opponent(board, pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas 'para esquerda'
def all_left_moves(board, pos, my_color):
    moves = []
    pos = left(pos)
    while is_valid_pos(pos) and is_empty(board, pos):
        moves.append(pos)
        pos = left(pos)

    if is_valid_pos(pos) and  has_opponent(board, pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas para 'diagonal superior direita'
def all_up_right_moves(board, pos, my_color):
    moves = []
    pos = up_right(pos)
    while is_valid_pos(pos) and is_empty(board, pos):
        moves.append(pos)
        pos = up_right(pos)

    if is_valid_pos(pos) and  has_opponent(board, pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas para 'diagonal superior esquerda'
def all_up_left_moves(board, pos, my_color):
    moves = []
    pos = up_left(pos)
    while is_valid_pos(pos) and is_empty(board, pos):
        moves.append(pos)
        pos = up_left(pos)

    if is_valid_pos(pos) and  has_opponent(board, pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas para 'diagonal inferior esquerda'
def all_down_left_moves(board, pos, my_color):
    moves = []
    pos = down_left(pos)
    while is_valid_pos(pos) and is_empty(board, pos):
        moves.append(pos)
        pos = down_left(pos)

    if is_valid_pos(pos) and  has_opponent(board, pos, my_color):
        moves.append(pos)

    return moves


# dada uma posicao, retorna todas as casas validas para 'diagonal inferior direita'
def all_down_right_moves(board, pos, my_color):
    moves = []
    pos = down_right(pos)
    while is_valid_pos(pos) and is_empty(board, pos):
        moves.append(pos)
        pos = down_right(pos)

    if is_valid_pos(pos) and  has_opponent(board, pos, my_color):
        moves.append(pos)

    return moves


# verifica se a posicao pos é valida. ou seja, esta dentro dos limites do tabuleiro
def is_valid_pos(pos):
    row = pos[0]
    col = pos[1]
    return 0 <= row <= 7 and 0 <= col <= 7


# verifica se a posicao pos tem um companheiro de equipe
def has_teammate(board, pos, my_color):
    if is_empty(board, pos):
        return False
    
    if my_color > 0:
        if get_piece(board, pos) > 0:
            return True
    
    if my_color < 0:
        if get_piece(board, pos) < 0:
            return True

    return False

    # verifica se a posicao pos tem um oponente
# def has_opponent(board, pos, my_color):
#     if get_piece(board, pos) < 0:
#         if my_color > 0:
#             return True
#         return False
#     if get_piece(board, pos) > 0:
#         if my_color < 0:
#             return True
#         return False
#     return False

def remove_piece(board, pos):
    row = pos[0]
    col = pos[1]
    board[row][col] = 0

def set_piece(board, pos, piece):
    row = pos[0]
    col = pos[1]
    board[row][col] = piece

def get_piece(board, pos):
    row = pos[0]
    col = pos[1]
    return board[row][col]

def move(board, current_pos, desired_pos):
    piece = get_piece(board, current_pos)
    set_piece(board, desired_pos, piece)
    remove_piece(board, current_pos)



def pawn_possible_moves(board, pos):
    move_list = []
    my_color = get_piece(board, pos)
    #se for branco
    if my_color > 0:
        pawn_move = up
        diag_right_house = up_right(pos)
        diag_left_house = up_left(pos)
    else:
        pawn_move = down
        diag_right_house = down_right(pos)
        diag_left_house = down_left(pos)

    move_front = pawn_move(pos)
    if is_valid_pos(move_front) and  is_empty(board, move_front):
         move_list.append(move_front)


    # Movimentos de captura normais
    if is_valid_pos(diag_left_house) and  has_opponent(board, diag_left_house, my_color):
         move_list.append(diag_left_house)

    if is_valid_pos(diag_right_house) and  has_opponent(board, diag_right_house, my_color):
         move_list.append(diag_right_house)

    return move_list




    # retorna os 2 L's: |--
def knight_left(pos):
    row = pos[0]
    col = pos[1]
    l_up = (row - 1, col - 2)
    l_down = (row + 1, col - 2)
    return [l_up, l_down]

# retorna os 2 L's: --|
def knight_right(pos):
    row =  pos[0]
    col =  pos[1]
    r_up = (row - 1, col + 2)
    r_down = (row + 1, col + 2)
    return [r_up, r_down]

# retorna os 2 L's: _|_
def knight_down(pos):
    row =  pos[0]
    col =  pos[1]
    d_left = (row + 2, col - 1)
    d_right = (row + 2, col + 1)
    return [d_left, d_right]

# retorna os 2 L's: T
def knight_up(pos):
    row =  pos[0]
    col =  pos[1]
    u_left = (row - 2, col - 1)
    u_right = (row - 2, col + 1)
    return [u_left, u_right]

# -- --#

def knight_possible_moves(board, pos):
    move_list = []
    my_color = get_piece(board, pos)
    move_list =  knight_down(pos) +  knight_up(pos) +  knight_left(pos) +  knight_right(pos)
    invalid_moves = []
    for move in  move_list:
        if not is_valid_pos(move) or has_teammate(board, move, my_color):
            invalid_moves.append(move)
        #     continue
        # if has_teammate(board, pos, my_color):
        #     invalid_moves.append(move)

    move_list = [x for x in  move_list if x not in invalid_moves]

    return move_list


def queen_possible_moves(board, pos):
    my_color = get_piece(board, pos)
    move_list = []
    move_list = all_down_moves(board, pos, my_color) + \
                        all_up_moves(board, pos, my_color) + \
                        all_right_moves(board, pos, my_color) + \
                        all_left_moves(board, pos, my_color) + \
                        all_up_left_moves(board, pos, my_color) + \
                        all_down_left_moves(board, pos, my_color) + \
                        all_down_right_moves(board, pos, my_color) + \
                        all_up_right_moves(board, pos, my_color)
    return move_list



def king_possible_moves(board, pos):
    move_list = []
    my_color = get_piece(board, pos)
    move_list = [up(pos), down(pos), left(pos), right(pos), up_left(pos),
                        up_right(pos), down_left(pos), down_right(pos)]
    invalid_moves = []
    for move in move_list:
        if not (is_valid_pos(move)) or has_teammate(board, pos, my_color):
            invalid_moves.append(move)

    move_list = [x for x in move_list if x not in invalid_moves]

    return move_list

def bishop_possible_moves(board, pos):
    move_list = []
    my_color = get_piece(board, pos)
    move_list = all_down_left_moves(board, pos, my_color) + \
                        all_down_right_moves(board, pos, my_color) + \
                        all_up_left_moves(board, pos, my_color) + \
                        all_up_right_moves(board, pos, my_color)
    return move_list



def rook_possible_moves(board, pos):
    move_list = []
    my_color = get_piece(board, pos)
    move_list = all_down_moves(board, pos, my_color) + \
                        all_up_moves(board, pos, my_color) + \
                        all_right_moves(board, pos, my_color) + \
                        all_left_moves(board, pos, my_color)
    return move_list


def get_piece_all_moves(board, pos):
    piece = get_piece(board, pos)
    if abs(piece) == 10:
        return pawn_possible_moves(board, pos)
    
    if abs(piece) == 29:
        return knight_possible_moves(board, pos)

    if abs(piece) == 30:
        return bishop_possible_moves(board, pos)

    if abs(piece) == 50:
        return rook_possible_moves(board, pos)

    if abs(piece) == 90:
        return queen_possible_moves(board, pos)
    
    if abs(piece) == 1000:
        return king_possible_moves(board, pos)


def get_all_black_pos(board):
    all_pos = []
    for i in range (8):
        for j in range(8):
            if board[i][j] < 0:
                all_pos.append((i,j))

    return all_pos

def get_all_white_pos(board):
    all_pos = []
    for i in range (8):
        for j in range(8):
            if board[i][j] > 0:
                all_pos.append((i,j))
    return all_pos

                
def get_all_piece_positions(board, my_color):
    if my_color < 0:
        return get_all_black_pos(board)
    if my_color > 0:
        return get_all_white_pos(board)



board = [-50, -29, -30, -90, -1000, -30, -29, -50], \
          [-10,-10,-10,-10,-10,-10,-10,-10], \
          [0,0,0,0,0,0,0,0], \
          [0,0,0,0,0,0,0,0],  \
          [0,0,0,0,0,0,0,0], \
          [0,0,0,0,0,0,0,0], \
          [10,10,10,10,10,10,10,10], \
          [50, 29, 30, 90, 1000, 30, 29, 50], \
                #a 

def print_board(board):
    tabuleiro = ""
    for line in board:
        print("\n")
        linha = ""
        for piece in line:
            linha = linha + str(piece) + " | "
    linha = linha + "\n"
    tabuleiro = tabuleiro + linha
    print(tabuleiro)


posi = (0,0)