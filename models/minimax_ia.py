#from models import partida
import numpy as np
from random import randint
from models.match import Match
from constants.colors import *
import copy
from util.move_ia import *

class MinimaxIA:
    def __init__(self):
        pass
    
    #dada a diferenca entre um tabuleiro e outro,
    #retorna a casa selecionada e a desejada para que o 
    #estado do tabuleiro mude de board1 para board2
    def extract_movement(self, board1, board2):
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
    

    #converte a matriz de houses em uma matriz de inteiros
    #cada peca tem um valor definido
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

    #converte o tabuleiro do (coluna, linha) para o formato (linha, coluna)
    def flip_board(self, board):
        fix_matrix = np.rot90(board, axes=(1,0))
        for i in range(8):
            fix_matrix[i] = np.flip(fix_matrix[i])
        
        return fix_matrix

    
    #converte o tabuleiro do formato (linha, coluna) para o formato (coluna, linha)
    def unflip_board(self, board):
        for i in range(8):
            board[i] = np.flip(board[i])
        board = np.rot90(board, axes=(1,0), k=3)
        return board

    #retorna e prepara o tabuleiro para fazer os calculos
    #de melhor movimento
    def prepare_board(self, match):
        #recebe a matriz de houses
        matrix_houses = match.get_board().get_houses()
        #inverte(explicacao na declaracao da funcao flip_board())
        fix_matrix = self.flip_board(matrix_houses)
        #transforma em matriz de numeros
        board = self.house_to_matrix(fix_matrix)
        return board
    
    #recebe uma lista de duas coordenadas e retorna as houses correspondentes
    #usado para retornar a posição atual e a posição desejada, ou seja, o movimento desejado
    def coords_to_houses(self, match, coords):
        selected_house = coords[0]
        desired_house = coords[1]
        selected_house = match.get_board().get_house(selected_house)
        desired_house = match.get_board().get_house(desired_house)
        print(selected_house.get_piece(), desired_house.get_piece())
        return (selected_house, desired_house)
        
    
    def play(self, match):
        
        board = self.prepare_board(match)
        
        #calcula o melhor movimento e retorna o tabuleiro resultante
        best_scenario = self.calculate_best_move(board)
        
        #explicação na declaração da função unflip_board()
        best_scenario = self.unflip_board(best_scenario)
        board = self.unflip_board(board)
        
        #explicação na declaração da função extract_movement()
        selected_and_desired_house = self.extract_movement(board, best_scenario)
        
        #retorna o movimento desejado
        move = self.coords_to_houses(match, selected_and_desired_house)
        return move


    #dentre todas as jogadas possíveis, retorna a que tiver o menor valor,
    #pois a IA joga com as pretas, e as pretas são valores negativos. Então,
    #quanto menor o valor da soma do tabuleiro, melhor para a IA
    def calculate_best_move(self, board):
        #retorna todos os cenarios possiveis do turno
        all_scenarios = self.get_all_turn_scenarios(board, -1)
        
        #inicialização das variáveis
        best_scenario = np.full((8,8), 999)
        best_scenario_value = best_scenario.sum()
        
        #para cada jogada possível...
        for scenario in all_scenarios:
            #...calcula o valor dela usando minimax
            scenario_evaluation = self.minimax(scenario, 2, -999, 999, 1)
            print(np.array(scenario))
            print(scenario_evaluation)
            #comparação para descobrir o menor valor
            if best_scenario_value > scenario_evaluation:
                best_scenario = np.array(scenario)
                best_scenario_value = scenario_evaluation
                
        return best_scenario
        
        
    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0:
            return np.array(board).sum()
        
        if maximizing_player == 1:
            maxEval = -99999
            for sub_board in self.get_all_turn_scenarios(board, 1):
                board_eval = self.minimax(sub_board, depth-1, alpha, beta, -1)
                maxEval = max(maxEval, board_eval)
                alpha = max(alpha, board_eval)
                if beta <= alpha:
                    break
            return maxEval
        
        else:
            minEval = 99999
            for sub_board in self.get_all_turn_scenarios(board, -1): #self.get_all_turn_scenarios(board, -1):
                board_eval = self.minimax(sub_board, depth-1, alpha, beta, 1)
                minEval = min(minEval, board_eval)
                beta = min(beta, board_eval)
                if beta <= alpha:
                    break
            return minEval



    #dada uma peca e um movimento,
    # faz o movimento e retorna uma instancia do tabuleiro(copia) 
    # no estado apos o movimento
    def do_movement(self, board, current_pos, desired_pos):
        new_board = copy.deepcopy(board)
        move(new_board, current_pos, desired_pos)
        return new_board



    #retorna todas as casas possiveis
    def get_all_possible_moves(self, board, pos):
        all_moves = get_piece_all_moves(board, pos)
        return all_moves

    #retorna uma lista com cada uma das casas onde estao
    #as pecas do turno atual
    def get_all_piece_positions(self, board, color):
        return get_all_piece_positions(board, color)


    #dada uma peca, faz todos os movimentos possiveis, e o resultado do tabuleiro depois de cada
    #um deles eh retornado. ou seja, 
    # tem q retornar uma lista com instancias do tabuleiro com diferentes estados
    def get_all_piece_scenarios(self, board, pos, all_possible_moves):
        piece = get_piece(board, pos)
        all_piece_scenarios = []
        for possible_move in all_possible_moves:
            board_scenario = self.do_movement(board, pos, possible_move)
            all_piece_scenarios.append(board_scenario)
        return all_piece_scenarios

    # utiliza a funcao acima, mas para cada peca da vez escolhida
    #ou seja, vai retornar uma lista de todos os estados possiveis do tabuleiro
    #considerando todas as jogadas possiveis no turno.
    def get_all_turn_scenarios(self, board, turn_color):
        all_match_turn_scenarios = []
        piece_position_list = self.get_all_piece_positions(board, turn_color)
        for position in piece_position_list:
            all_possible_houses = self.get_all_possible_moves(board, position)
            all_possible_scenarios = self.get_all_piece_scenarios(board, position, all_possible_houses)
            all_match_turn_scenarios = all_match_turn_scenarios + all_possible_scenarios
        
        return all_match_turn_scenarios



    # teste: da p usar essa funcao em vez do minimax. 
    # eh como se fosse um minimax de profundidade 1
    ####################
    # def min_scenario(self, scenarios):
    #     best = np.full((8,8), 999)
    #     for i in range(len(scenarios)):
    #         if np.array(scenarios[i]).sum() < best.sum():
    #             best = np.array(scenarios[i])

    #     return best

    # def max_scenario(self, scenarios):
    #     best = np.full((8,8), -999)
    #     for i in range(len(scenarios)):
    #         if np.array(scenarios[i]).sum() > best.sum():
    #             best = np.array(scenarios[i])

    #     return best
    
    ##################
            