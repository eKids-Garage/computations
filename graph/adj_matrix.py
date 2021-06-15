graph_a = [ [0, 0, 0, 1, 1, 0, 1, 0],  
            [0, 0, 1, 0, 1, 0, 0, 0], 
            [0, 1, 0, 0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 0, 1, 1, 0],  
            [1, 1, 0, 0, 0, 0, 0, 1],  
            [0, 0, 1, 1, 0, 0, 0, 1], 
            [1, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 0]  
          ]


graph_b = [ [0, 0, 0, 1, 1, 0, 1, 0],  
            [0, 0, 0, 0, 1, 0, 0, 0],  
            [0, 1, 0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 1, 1, 0],  
            [0, 0, 0, 0, 0, 0, 0, 1],  
            [0, 0, 1, 0, 0, 0, 0, 1],  
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0]  
          ]


def is_adjacent(graph, vert_a, vert_b):
    if graph[vert_a][vert_b] == 1 or graph[vert_a][vert_b] == 1:
      return True
    else:
      return False


print("Graph A: ")
for i in range(0, 8):
    for j in range(0, 8):
        print("Vertice {0} and vertice {1} are adjacent: {2}".format(i, j, is_adjacent(graph_a, i, j)))


print("Graph B: ")
for i in range(0, 8):
    for j in range(0, 8):
        print("Vertice {0} and vertice {1} are adjacent: {2}".format(i, j, is_adjacent(graph_b, i, j)))  
