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
   
## Relatório
  ### Introdução
   Este relatório tem como objetivo a apresentação dos resultados obtidos em testes pela
implementação dos seguintes algoritmos de busca: Busca de Custo Uniforme, A Estrela (A*); Têmpera
Simulada e o Subida de Encosta. Tal implementação consiste na geração de escolhas de caminhos
pelo protagonista do jogo Pac-man.

  ### Resultados
   A tabela a seguir exibe uma comparação dos resultados produzidos pelos testes efetuados
em mapas do jogo. Estes abrangem os originais do projeto e os criados pelo presente grupo
(nossoBig, nossoMedium e nossoSmall). Os dados obtidos mostram a relação entre o custo do
caminho e o número de nodos expandidos para a geração deste.

Mapas              | Custo Uniforme |  A estrela  | Subida de Encosta | Têmpera Simulada
-------------------|----------------|-------------|-------------------|------------------
Big Maze           | 210 / 617      | 210 / 557   | 2 / 3             | 210 / 471        
Contours Maze      | 13 / 165       | 13 / 60     | 13 / 14           | 13 / 13          
Medium Dotted Maze | 68 / 206       | 68 / 158    | 42 / 43           | 162 / 163        
Medium Maze        | 68 / 267       | 68 / 226    | 42 / 43           | 152 / 159        
Nosso Big          | 100 / 260      | 100 / 226   | 8 / 9             | 106 / 213        
Nosso Medium       | 32 / 132       | 32 / 89     | 32 / 33           | 32 / 32          
Nosso Small        | 21 / 66        | 21 / 41     | 9 / 10            | 21 / 28          
Open Maze          | 54 / 679       | 54 / 550    | 54 / 55           | 54 / 54          
Original Classic   | 49 / 292       | 49 / 230    | 49 / 50           | 49 / 49          
Small Maze         | 19 / 90        | 19 / 56     | 13 / 14           | 29 / 39          
Tiny Maze          | 8 / 15         | 8 / 13      | 8 / 9             | 8 / 8       

 
 - Os dados encontram-se na representação de custo do caminho/nodos expandidos.
  ### Conclusões
   Na tabela apresentada acima, o algoritmo Subida de Encosta foi o único a não completar seu
objetivo em alguns dos testes: em 6 dos 11 mapas, não alcançou o seu estado meta, ou seja, o
objetivo final. Entretanto, aquele que apresentou um melhor desempenho de acordo com o custo do
caminho em relação ao nodos expandidos foi o algoritmo de Tempera Simulada.
