#from models import partida

from models.match import Match
from constants.colors import *
import copy
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
    

    def copy_match(self, match):
        new_board = copy.copy(match.get_board())
        new_match = Match()
        new_match.set_board(new_board)
        #tuple_ = match.get_all()
        #new_match.set_all(tuple_[0], tuple_[1], tuple_[2], tuple_[3], tuple_[4])
        return new_match


    def play(self, match):
        alpha = self.copy_match(match)
        alpha.set_evaluation(-999)
        beta = self.copy_match(match)
        beta.set_evaluation(999)
        best_scenario = self.minimax(match, 3, alpha, beta)
        match.set_board(best_scenario.get_board())
        match.set_turn(WHITE)
    
    def set_current_scenario(self, scenario):
        self.match_current_scenario = scenario
    
    def set_next_match_scenarios(self, board_scenarios):
        self.next_match_scenarios = board_scenarios

        #soma o valor de todas as pecas no tabuleiro
    def scenario_evaluation(self, scenario):
        result = 0
        for linha in scenario.get_board().get_houses:
            for house in linha:
                if house.get_piece() is None:
                    continue
                result = result + house.get_piece().get_value()
        scenario.set_evaluation(result)
        return scenario


    def max_scenario(self, scenario1, scenario2):
        if scenario1.get_value() > scenario2.get_value():
            return scenario1
        return scenario2
    
    def min_scenario(self, scenario1, scenario2):
        if scenario1.get_value() < scenario2.get_value():
            return scenario1
        return scenario2
                
    def minimax(self, scenario, depth, alpha, beta):
        if depth == 0:  #or scenario.game_over() <- implementar essa funcao de fim de jogo
            return self.scenario_evaluation(scenario)

        if scenario.get_turn() == WHITE: #maximizingPlayer
            maxEval = self.copy_match(scenario)
            maxEval.set_evaluation(-999)
            for scenario in self.getAllTurnScenarios(scenario):
                evaluation = minimax(scenario, depth-1, alpha, beta)
                maxEval = self.max_scenario(maxEval, evaluation)
                alpha = self.min_scenario(alpha, evaluation)
                if beta.get_evaluation() <= alpha.get_evaluation():
                    break
            return maxEval
        
        else:
            minEval = self.copy_match(scenario)
            minEval.set_evaluation(999)
            for scenario in self.getAllTurnScenarios(scenario):
                evaluation = minimax(scenario, depth-1, alpha, beta)
                minEval = self.min_scenario(minEval, evaluation)
                beta = self.min_scenario(beta, evaluation)
                if beta.get_evaluation() <= alpha.get_evaluation():
                    break
            return minEval





        ####---------------FUNCOES DE "PARTIDA". organizar, nao sao daqui-----------------#####


    #dada uma peca e um movimento,
    # faz o movimento e retorna uma instancia do tabuleiro(copia) 
    # no estado apos o movimento
    def doMovement(self, match, selected_house, desired_house):
        match_after_movement = self.copy_match(match)
        match_after_movement.movement_manager(selected_house, desired_house)
        return match_after_movement
        #faz o movimento, e retorna uma cópia do tabuleiro com o estado após o movimento

    #dada uma peca, faz todos os movimentos possiveis, e o resultado do tabuleiro depois de cada
    #um deles eh retornado. ou seja, 
    # tem q retornar uma lista com instancias do tabuleiro com diferentes estados
    def getAllPieceScenarios(self, match, house, all_possible_houses):
        all_piece_scenarios = []
        for possible_house in all_possible_houses:
            match_scenario = self.doMovement(match, house, possible_house)
            all_piece_scenarios.append(match_scenario)
        
        return all_piece_scenarios
    #retorna todas as casas possiveis
    def getAllPossibleHouses(self, match, house):
        all_moves = house.get_piece().get_possible_moves(match)
        all_possible_houses = []
        for move in all_moves:
            all_possible_houses.append(match.get_board().get_house(move))
        return all_possible_houses
    #     todosOsCenarios = [] 
    #     todos_os_movimentos= piece.get_all_possible_moves();
    #     for movement in all_movements:
    #         todosOsCenarios.append(self.doMovement(peca, posicao_desejada))

    #retorna uma lista com cada uma das casas onde estao
    #as pecas do turno atual
    def getAllTurnPieceHouses(self, match):
        house_list = []
        for linha in match.get_board().get_houses():
            for house in linha:
                if house.get_piece() is None:
                    continue
                if house.get_piece().get_color() == match.get_turn():
                    house_list.append(house)
        
        return house_list

    # utiliza a funcao acima, mas para cada peca da vez escolhida
    #ou seja, vai retornar uma lista de todos os estados possiveis do tabuleiro
    #considerando todas as jogadas possiveis no turno.
    def getAllTurnScenarios(self, match):
    #     todos_os_cenarios_do_turno = []
        all_match_turn_scenarios = []
        house_list = self.getAllTurnPieceHouses(match)
        for house in house_list:
            all_possible_houses = self.getAllPossibleHouses(match, house)
            all_possible_scenarios = self.getAllPieceScenarios(match, house, all_possible_houses)
            all_match_turn_scenarios.append(all_possible_scenarios)
        
        return all_match_turn_scenarios
    #     for peca in tabuleiro:
#         if peca.cor = corDaVez:
#             todos_os_cenarios_do_turno. append(retornaTodosOsCenariosDaPeca(peca))
            
