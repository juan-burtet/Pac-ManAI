# Trabalho Prático de IA
  > Inteligência Artificial Pac-Man

### Algoritmos:
  - A*
  - Têmpera Simulada
  - Subida de Encosta
  - Busca de Custo Uniforme

### Criar novos labirintos para teste (pequenos, médios e grandes)

### Apresentar relatório sobre os resultados

### Entrada:
  - Estado Inicial
  - Estado Meta

### Deve Retornar:
  1. O número de estados (movimentos) testados.
  2. O caminho e número de estados para a solução.

#### Integrantes:
  - Juan Burtet
  - Isabelle Azevedo
  - Thales Castro

### COMO TESTAR OS ALGORITMOS(modificar _"MAPA"_ por mapa desejado):

  - A*
    > $ python pacman.py -l MAPA -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic

  - Têmpera Simulada
    > $ python pacman.py -l MAPA -p SearchAgent -a fn=sa,heuristic=euclideanHeuristic

  - Subida de Encosta
    > $ python pacman.py -l MAPA -p SearchAgent -a fn=hc,heuristic=euclideanHeuristic

  - Busca de custo Uniforme
    > $ python pacman.py -l MAPA -p SearchAgent -a fn=ucs
