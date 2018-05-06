# -*- coding: utf-8 -*-

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import math

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Busca de Custo Uniforme
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #Inicializa a fila de prioridade (em ordem crescente para o custo do Caminho) dos nós/estados
    borda = util.PriorityQueue()
    #Vetor dos nos percorridos
    acoes = []
    #NoInicial recebe o estado do nó inicial
    #{{No, acao do agente(direcao), custo}, caminho percorrido, custoCaminho}
    noInicial = ((problem.getStartState(), None, 0), [], 0)
    #Inicializa a fila com o no do estado inicial
    borda.push(noInicial, None)
    #Enquanto a fila não for vazia
    while not borda.isEmpty():
        #Retira um elemento da fila
		atual = borda.pop()
		#Recebe o no do estado atual
		noAtual = atual[0][0]
		#Recebe a acao atual efetuada
		direcaoAtual = atual[0][1]
		#Recebe vetor de acoes efetuadas (caminho percorrido)
		caminhoAtual = atual[1]
		#Recebe o custo do caminho até o momento
		custoAtual = atual[2]
		#Verifica se o no não foi acessado
		if noAtual not in acoes:
			#Adiciona o no nao visitado no vetor acoes
			acoes.append(noAtual)
			#Verifica se o estado atual é o estado meta
			#Se sim, retorna o caminho percorrido
			if(problem.isGoalState(noAtual)):
				return caminhoAtual
			#Recebe os estados(nos) sucessores do estado atual
			noSucessores = problem.getSuccessors(noAtual)
			#Insere os estados(nos) sucessores em uma lista para armazenar tal informacao
			listaSucc = list(noSucessores)
			#Laço que percorre a lista de estados(nos) sucessores
			for no in listaSucc:
				#Verifica se o no(estado) esta no vetor de acoes
				if no[0] not in acoes:
					#Verifica se o no(estado) eh o estado meta/ no objetivo
					#Se sim, retorna o caminho percorrido ate o no objetivo
					if(problem.isGoalState(no[0])):
						return caminhoAtual+[no[1]]
					#Adiciona o no na fila de prioridade, caso este nao seja o no objetivo e nao foi visitado
					novoNo = (no, caminhoAtual+[no[1]], custoAtual + no[2])
					borda.push(novoNo, custoAtual + no[2])
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first """
    start = problem.getStartState()
    goal = problem.getGoalState()

    """ Conjunto de nós já avaliados """
    closedSet = []

    """ Conjunto de nós descobertos que ainda não foram avaliados.
    Inicialmente, apenas o nó inicial é conhecido """
    openSet = [start]

    """ Para cada nó, aquele nó que pode ser alcançado de forma mais eficiente.
    Se um nó pode ser alcançado de vários nós, cameFrom vai eventualmente conter
    o passo anterior mais eficiente """
    cameFrom = {}

    """ Para cada nó, o custo de pegar do nó inicial até aquele nó """
    gScore = {}

    """ O custo do início para o início é zero """
    gScore[start] = 0

    """ Para cada nó, o custo total de pegar do nó inicial para o final pela
    passagem por aquele nó. O valor é parcialmente conhecida, parcialmente heurística """
    fScore = {}

    """ Para o primeiro nó, o valor é completamente heurístico """
    from searchAgents import manhattanHeuristic
    fScore[start] = manhattanHeuristic(start, problem)

    while openSet:
        lowest = manhattanHeuristic(openSet[0], problem)
        for i in openSet:
            if lowest > manhattanHeuristic(i, problem):
                lowest = manhattanHeuristic(i, problem)
        current = lowest

        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        closedSet.append(current)

        print(current)
        neighbor = problem.getSuccessors(current)

        for i in neighbor:
            if gScore.get(i[0]) == None:
                gScore[i[0]] = float("inf")

            if i in closedSet:
                continue
                """ Ignora o vizinho que já foi avaliado """

            if i not in openSet:
                openSet.append(i)
                """ Descobre um novo nó """
            print(i)
            """ A distância do início até o vizinho """
            tentative_gScore = gScore[current] + abs(manhattanHeuristic(current, problem) - manhattanHeuristic(i[0], problem))
            if tentative_gScore >= gScore[i[0]]:
                continue
                """ Este não é o melhor caminho """

            """ Este caminho é o melhor até agora. Grave! """
            cameFrom[i[0]] = current
            gScore[i[0]] = tentative_gScore
            fScore[i[0]] = gScore[i[0]] + manhattanHeuristic(i[0], problem)

    return failure

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    return total_path

# Subida de encosta
def hillClimbing(problem):

    # recebe o Estado inicial
    atual = problem.getStartState()
    # Inicia o caminho em vazio
    caminho = []

    # Loop infinito
    while True:

        # Recebe os sucessores do Nodo atual
        sucessores = problem.getSuccessors(atual)
        listaSucessores = list(sucessores)

        # (successor, action, stepCost)
        # Inicia vizinho com o caminho
        vizinho = listaSucessores[0]

        # Passa por todos os sucessores
        for x in listaSucessores:
            # Fica com a menor distância entre um sucessor e o objetivo
            if distancia2pts(vizinho[0], problem.getGoalState()) > distancia2pts(x[0], problem.getGoalState()):
                vizinho = x

        # Se a distância for maior ou igual ao atual, retorna os caminhos
        if distancia2pts(atual, problem.getGoalState()) <= distancia2pts(vizinho[0], problem.getGoalState()):
            return caminho

        # Adiciona aos caminhos
        caminho.append(vizinho[1])
        atual = vizinho[0]

# Têmpera Simulada
def simmulatedAnnealing(problem):

    """
    function SIMULATED-ANNEALING(problem, schedule) returns a solution state
        inputs: problem, a problem
                schedule, a mapping from time to "temperature"

        current <- MAKE-NODE(problem.INITIAL-STATE)
        for t = 1 to INFINITE do
            T <- schedule(t)
            if T = 0 then return current
            next <- a randomly selected sucessor of current
            (DELTA)E <- next.VALUE - current.VALUE
            if (DELTA)E > 0 then current <- next
            else current <- next only with probability e^(DELTA)E/T
    """

    """
    Temperatura com valor elevado
    T = 1000
    Solução candidata inicial qualquer
    S = problem.getStartState()
    Vetor de acoes
    acoes = []
    Melhor recebe S
    Melhor = S

    Repita até Melhor = solucaoIdeal OU T < 0
    while
        R <- gerarVizinho(S)
        Qualidade(R) > Qualidade(S) OU Aleatorio() < P(R,S,T)
        P(R.S.T) = EXP(Qualidade(R)-Qualidade(S))/T
            S <- #R
        T <- novaTemperatura(T)
        Se Qualidade(S) > Qualidade(Melhor)
            Melhor <- S
    Return Melhor
    Retornar vetor de acoes(caminho percorrido)

    -------------------------------------------------------------------------

    S = S0
    T0 = TempInicial()
    T = T0
    j = 1
    /*Loop principal – Verifica se foram atendidas as condições de termino do algoritmo*/
    Repita
        i = 1
        nSucesso = 0
        /*Loop Interno – Realização de perturbação em uma iteração*/
        Repita
            Si = Perturba(S)
            ∆Fi = f(Si) – f(S)
            /*Teste de aceitação de uma nova solução*/
            Se (∆fi ≤ 0) ou (exp(-∆fi/T) > Randomiza()) então
            S= Si
            nSucesso = nSucesso + 1
            Fim-se
            i = i + 1
        Até (nSucesso ≥ L) ou (i > P)
        /*Actualização da Temperatura*/
        T = α.T
        /*Actualização do Contador de iterações*/
        j = j + 1
    Até (nSucesso = 0) ou (j > M)
    /*Saída do Algoritmo*/
    Imprima(S)
    """

# Distância entre 2 pontos
def distancia2pts(pos1, pos2):
    xy1 = pos1
    xy2 = pos2

    x = xy1[0] + xy2[0]
    y = xy1[1] + xy2[1]
    return abs(math.sqrt(x*x + y*y))

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
hc = hillClimbing
sa = simmulatedAnnealing
