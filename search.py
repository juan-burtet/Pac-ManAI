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
			#Se sim, retorna o caminho percorrido9
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

# A*
def aStarSearch(problem, heuristic=nullHeuristic):

    # Inicializa a fila Prioritária
    fila = util.PriorityQueue()
    # Set com nós expandidos
    expandidos = set()
    # Nó inicial na fila, adicionado uma dupla
    # A primeira, é uma tripla (Nó, Rota, custo)
    # Segunda é o custo
    fila.push((problem.getStartState(), [], 0),0)

    # Enquanto a fila não for vazia
    while not fila.isEmpty():
        # Pop da fila pegando o nó atual, os movimentos até o nó e o custo até o nó
        nodoAtual, movimentos, custoAtual = fila.pop()
        # Se o nó atual já foi expandido, continua pro próximo
        if(nodoAtual in expandidos):
            continue
        # Se o nó atual é o nó objetivo, retorna os movimentos
        if problem.isGoalState(nodoAtual):
            return movimentos
        # Nó atual é adicionado aos expandidos
        expandidos.add(nodoAtual)

        # Percorre por todos os sucessores do Nó atual
        for nodo, movimento, custo  in problem.getSuccessors(nodoAtual):
            # Se o nodo já foi expandido, segue pro próximo sucessor
            if(nodo in expandidos):
                continue
            # Valor da heuristica
            h = heuristic(nodo, problem)
            # Adiciona aos nodos aberto a dupla:
            # Primeira posição (Nó aberto, movimentos até o nó, e o custo dele + custo somado)
            # Segunda posição (custo dele + custo somado + heuristica)
            fila.push((nodo, movimentos + [movimento], custoAtual + custo), custoAtual + custo + h)

    # Se não encontrou um caminho, retorna vazio
    return []

# Subida de encosta
def hillClimbing(problem, heuristic=nullHeuristic):

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
            if heuristic(vizinho[0], problem) > heuristic(x[0], problem):
                vizinho = x

        # Se a distância for maior ou igual ao atual, retorna os caminhos
        if heuristic(atual, problem) <= heuristic(vizinho[0], problem):
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
    #---------------------------------------------------------------------------

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
hc = hillClimbing
sa = simmulatedAnnealing
