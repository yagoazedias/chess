#from models import partida


class Scenario:
    def __init__(self, board_scenario_node):

        #board_scenario_node eh uma instancia de tabuleiro, com as houses e pecas.
        #eh o cenario atual
        self.board_scenario_node = board_scenario_node

        #uma lista com todos os estados possiveis do tabuleiro
        #considerando todas as jogadas.
        #eh uma lista de instancias do tabuleiro
        self.next_board_scenarios = []

        #indicador de quem eh a vez
        self.turn = 1



    #soma o valor de todas as pecas no tabuleiro
    def scenario_evaluation(self, scenario):
        result = 0
        for house in scenario.get_houses:
            #a peca devera ter um valor. eh fixo.
            #peao: 1
            #cavalo: 3
            #bispo: 3
            #torre: 5
            #rainha: 9
            #rei: 200
            result = result + house.get_piece().get_value()
        
        return result


    def chose_move(self, scenario):
        #minimax

    

    ####---------------FUNCOES DE "PARTIDA". organizar, nao sao daqui-----------------#####


#dada uma peca e um movimento,
# faz o movimento e retorna uma instancia do tabuleiro(copia) 
# no estado apos o movimento
def doMovement(board, pecaAtual, posicao_atual, posicao_desejada):
    #faz o movimento, e retorna uma cópia do tabuleiro com o estado após o movimento
    pass

#dada uma peca, faz todos os movimentos possiveis, e o resultado do tabuleiro depois de cada
#um deles eh retornado. ou seja, 
# tem q retornar uma lista com instancias do tabuleiro com diferentes estados
def getAllPieceScenarios(piece):
#     todosOsCenarios = [] 
#     todos_os_movimentos= piece.get_all_possible_moves();
#     for movement in all_movements:
#         todosOsCenarios.append(doMovement(peca, posicao_desejada))
        
    
# utiliza a funcao acima, mas para cada peca da vez escolhida
#ou seja, vai retornar uma lista de todos os estados possiveis do tabuleiro
#considerando todas as jogadas possiveis no turno.
def getAllTurnScenarios(corDaVez):
#     todos_os_cenarios_do_turno = []
#     for peca in tabuleiro:
#         if peca.cor = corDaVez:
#             todos_os_cenarios_do_turno. append(retornaTodosOsCenariosDaPeca(peca))
            
