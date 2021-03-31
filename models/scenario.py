#from models import partida
import numpy as np

from models.match import Match
from constants.colors import *
import copy
from util.move_ia import *
class Scenario:
    def __init__(self):
        pass

        #match_current_scenario eh uma instancia de tabuleiro, com as houses e pecas.
        #eh o cenario atual
        #self.match_current_scenario = match_current_scenario

        #uma lista com todos os estados possiveis do tabuleiro
        #considerando todas as jogadas.
        #eh uma lista de instancias do tabuleiro
        #self.next_match_scenarios = []

        #indicador de quem eh a vez
        #self.turn = 1
    

    # def copy_match(self, match):
    #     new_board = copy.copy(match.get_board())
    #     new_match = Match()
    #     new_match.set_board(new_board)
    #     #tuple_ = match.get_all()
    #     #new_match.set_all(tuple_[0], tuple_[1], tuple_[2], tuple_[3], tuple_[4])
    #     return new_match

    def print_matrix(self, matrix):
        for i in range(8):
            print('\n')
            print(matrix[i])


    def compare_before_after(self, board1, board2):
        selected_house = (0,0)
        desired_house = (0,0)
        for i in range(8):
            for j in range(8):
                prev_element = board1[i][j]
                current_element = board2[i][j]
                if prev_element != current_element:
                    if current_element == 0:
                        selected_house = (i,j)
                        continue
                    if current_element != 0:
                        desired_house = (i,j)
                        continue
        return (selected_house, desired_house)

    def invert(self,pos):
        return (pos[1], pos[0])


    def house_to_matrix(self, matrix):
        board = []
        for i in range(8):
            line = []
            for j in range(8):
                if matrix[i][j].get_piece() is not None:
                    line.append(matrix[i][j].get_piece().get_value())
                else:
                    line.append(0)

            board.append(line)
        return board

    
    def flip_board(self, board):
        fix_matrix = np.rot90(board, axes=(1,0))
        for i in range(8):
            fix_matrix[i] = np.flip(fix_matrix[i])
        
        return fix_matrix

    def unflip_board(self, board):
        for i in range(8):
            board[i] = np.flip(board[i])
        board = np.rot90(board, axes=(1,0), k=3)
        return board

    def play(self, match):
        matrix_houses = match.get_board().get_houses()

        # fix_matrix = np.rot90(matrix_houses, axes=(1,0))
        # for i in range(8):
        #     fix_matrix[i] = np.flip(fix_matrix[i])

        fix_matrix = self.flip_board(matrix_houses)
        board = self.house_to_matrix(fix_matrix)


        #print('\n\n\n')
        # for i in range(8):
        #     board[i] = np.flip(board[i])
        # board = np.rot90(board, axes=(1,0), k=3)


        # turn = match.get_turn()
        # if turn == WHITE:
        #     my_color = 1
        # else:
        #     my_color = -1
        

        # set_piece(board, (2,0), 900)
        # scenarios = self.getAllTurnScenarios(board, -3)
        # #print(np.array(scenarios))
        # # best = np.matrix(8*[8*[999]])
        # # for i in range(len(scenarios)):
        # #     if np.matrix(scenarios[i]).sum() < best.sum():
        # #         best = np.matrix(scenarios[i])
        # best = self.min_scenario(scenarios)

        #print(np.matrix(best))
        
        #alpha = self.negative_infinity()
        #beta = self.positive_infinity()
        #best_scenario = 8*[8*[0]]
        
        #best_scenario = self.minimax(board, 1, -3)
        
        #FUNCIONANDO! SEM MINIMAX. so com o min_scenario
        #all_moves = self.getAllTurnScenarios(board, -3)
        #best_scenario = self.min_scenario(all_moves)
        #-----------------------#####

        #esse if else eh inutil. smp vai entrar aqui
        #como pretas. e pretas sao o -1 (nao eh maximizing player)
        #e sim minimizing
        if match.get_turn() == WHITE:
            maximizing_player = 1
        else:
            maximizing_player = -1


        #ESTA AVALIANDO OS MOVIMENTOS DO BRANCO ERRADO (nao sei pq)
        #so funciona profundidade 1 (q é a mesma coisa de so usar a
        # funcao 'min_scenario' que eu comentei ali embaixo,
        # ffalando q funciona sem o minimax).
        #obs.: ele ta achando, com as pretas, que ele está embaixo no tabuleiro!!!
        #nao sei pq. ouuu ele ta achando q pode jogar qqr peca em qqr lugar. nao sei
        #tem q verificar. eu testei as funcoes de calcular os movimentos das brancas e 
        #tava tudo ok
        best_scenario = self.minimax(board, 2, False)

        #teste do allturncenario branco
        # board1 = [-50, -29, -30, -90, -1000, -30, -29, -50], \
        #   [-10,-10,-10,-10,-10,-10,-10,-10], \
        #   [0,0,0,0,0,0,0,0], \
        #   [0,0,0,0,0,0,0,0],  \
        #   [0,0,0,0,0,0,0,0], \
        #   [0,0,0,0,0,0,0,0], \
        #   [10,10,10,10,10,10,10,10], \
        #   [50, 29, 30, 90, 1000, 30, 29, 50], \
        
        # t = self.getAllTurnScenarios(board1, 1)
        # print(np.array(t))
        
        
        
        best_scenario = self.unflip_board(best_scenario)
        board = self.unflip_board(board)
        
        # board1 = [-50, -29, -30, -90, -1000, -30, -29, -50], \
        #   [-10,-10,-10,-10,-10,-10,-10,-10], \
        #   [0,0,0,0,0,0,0,0], \
        #   [0,0,0,0,0,0,0,0],  \
        #   [0,0,0,0,0,0,0,0], \
        #   [0,0,0,0,0,0,0,0], \
        #   [10,10,10,10,10,10,10,10], \
        #   [50, 29, 30, 90, 1000, 30, 29, 50], \
              
        # board2 = [-50, -29, -30, -90, -1000, -30, -29, -50], \
        #   [-10,-10,-10,-10,-10,-10,-10,-10], \
        #   [0,0,0,0,0,0,0,0], \
        #   [0,0,0,0,0,0,0,0],  \
        #   [0,0,0,0,0,0,0,0], \
        #   [0,0,0,0,0,0,0,0], \
        #   [10,10,10,10,10,10,10,10], \
        #   [50, 29, 30, 90, 1000, 30, 29, 50], \
        
        # selected_desired = self.compare_before_after(board1, board2)
        # print("AQUI:",selected_desired)

        selected_desired = self.compare_before_after(board, best_scenario)

        s_house = selected_desired[0]
        d_house = selected_desired[1]
        s_house = match.get_board().get_house(s_house)
        d_house = match.get_board().get_house(d_house)
        print(s_house.get_piece())
        return (s_house, d_house)
    
    def set_current_scenario(self, scenario):
        self.match_current_scenario = scenario
    
    def set_next_match_scenarios(self, board_scenarios):
        self.next_match_scenarios = board_scenarios

        #soma o valor de todas as pecas no tabuleiro
    def scenario_evaluation(self, board):
        result = 0
        for linha in board:
            for piece in linha:
                result = result + piece

        return result

    #FUNCIONANDO: (SEM MINIMAX)
    # def min_scenario(self, scenarios):
    #     best = np.full((8,8), 999)
    #     for i in range(len(scenarios)):
    #         if np.array(scenarios[i]).sum() < best.sum():
    #             best = np.array(scenarios[i])

    #     return best

    # def max_scenario(self, scenarios):
    #     best = np.full((8,8) -999)
    #     for i in range(len(scenarios)):
    #         if np.array(scenarios[i]).sum() > best.sum():
    #             best = np.array(scenarios[i])

    #     return best

    def min_scenario(self, minEval, board):
        if minEval.sum() < board.sum():
            return minEval
        return board

    def max_scenario(self, maxEval, board):
        if maxEval.sum() > board.sum():
            return maxEval
        return board
    
    # def min_scenario(self, scenario1, scenario2):
    #     if self.scenario_evaluation(scenario2) < self.scenario_evaluation(scenario2):
    #         return scenario1
    #     return scenario2
    
    def negative_infinity(self):
        return 8*[8*[-99]]
    def positive_infinity(self):
        return 8*[8*[99]]


    def maximizing_player(self, my_color):
        if my_color == -1:
            return False
        return True

    def minimax(self, board, depth, maximizing_player):
        if depth == 0:  #or scenario.game_over() <- implementar essa funcao de fim de jogo
            return np.array(board)
        if maximizing_player: #maximizingPlayer
            print('max')
            maxEval = np.full((8,8), -99)
            for sub_board in self.getAllTurnScenarios(board, 1):
                board_eval = self.minimax(sub_board, depth-1, False)
                maxEval = self.max_scenario(maxEval, board_eval)
            return maxEval
        
        else:
            print('min')
            minEval = np.full((8,8), 99)
            for sub_board in self.getAllTurnScenarios(board, -1):
                board_eval = self.minimax(sub_board, depth-1, True)
                minEval = self.min_scenario(minEval, board_eval)
            return minEval





        ####---------------FUNCOES DE "PARTIDA". organizar, nao sao daqui-----------------#####


    #dada uma peca e um movimento,
    # faz o movimento e retorna uma instancia do tabuleiro(copia) 
    # no estado apos o movimento
    def doMovement(self, board, current_pos, desired_pos):
        new_board = copy.deepcopy(board)
        # new_board = []
        # for line in board:
        #     linetemp = []
        #     for piece in line:
        #         linetemp.append(piece)
        # new_board.append(linetemp)
        move(new_board, current_pos, desired_pos)
        return new_board
        #faz o movimento, e retorna uma cópia do tabuleiro com o estado após o movimento



    #retorna todas as casas possiveis
    def getAllPossibleMoves(self, board, pos):
        all_moves = get_piece_all_moves(board, pos)
        return all_moves
    #     todosOsCenarios = [] 
    #     todos_os_movimentos= piece.get_all_possible_moves();
    #     for movement in all_movements:
    #         todosOsCenarios.append(self.doMovement(peca, posicao_desejada))

    #retorna uma lista com cada uma das casas onde estao
    #as pecas do turno atual
    def getAllPiecePositions(self, board, color):
        return get_all_piece_positions(board, color)


        #dada uma peca, faz todos os movimentos possiveis, e o resultado do tabuleiro depois de cada
    #um deles eh retornado. ou seja, 
    # tem q retornar uma lista com instancias do tabuleiro com diferentes estados
    def getAllPieceScenarios(self, board, pos, all_possible_moves):
        piece = get_piece(board, pos)
        all_piece_scenarios = []
        for possible_move in all_possible_moves:
            board_scenario = self.doMovement(board, pos, possible_move)
            all_piece_scenarios.append(board_scenario)
        return all_piece_scenarios

    # utiliza a funcao acima, mas para cada peca da vez escolhida
    #ou seja, vai retornar uma lista de todos os estados possiveis do tabuleiro
    #considerando todas as jogadas possiveis no turno.
    def getAllTurnScenarios(self, board, turn_color):
    #     todos_os_cenarios_do_turno = []
        all_match_turn_scenarios = []
        piece_position_list = self.getAllPiecePositions(board, turn_color)
        for position in piece_position_list:
            all_possible_houses = self.getAllPossibleMoves(board, position)
            all_possible_scenarios = self.getAllPieceScenarios(board, position, all_possible_houses)
            all_match_turn_scenarios = all_match_turn_scenarios + all_possible_scenarios
        
        return all_match_turn_scenarios
    #     for peca in tabuleiro:
#         if peca.cor = corDaVez:
#             todos_os_cenarios_do_turno. append(retornaTodosOsCenariosDaPeca(peca))
            
