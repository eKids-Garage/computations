# Graph A: Non-directed graph

          #  0  1  2  3  4  5  6  7
graph_a = [ [0, 0, 0, 1, 1, 0, 1, 0],  #  0
            [0, 0, 0, 0, 0, 0, 0, 0],  #  1
            [0, 0, 0, 0, 0, 0, 0, 0],  #  3
            [0, 0, 0, 0, 0, 0, 0, 0],  #  4
            [0, 0, 0, 0, 0, 0, 0, 0],  #  5
            [0, 0, 0, 0, 0, 0, 0, 0],  #  6
            [0, 0, 0, 0, 0, 0, 0, 0]   #  7
          ]



# Graph B: Directed graph

          #  0  1  2  3  4  5  6  7
graph_b = [ [0, 0, 0, 1, 1, 0, 1, 0],  #  0
            [0, 0, 0, 0, 0, 0, 0, 0],  #  1
            [0, 0, 0, 0, 0, 0, 0, 0],  #  3
            [0, 0, 0, 0, 0, 0, 0, 0],  #  4
            [0, 0, 0, 0, 0, 0, 0, 0],  #  5
            [0, 0, 0, 0, 0, 0, 0, 0],  #  6
            [0, 0, 0, 0, 0, 0, 0, 0]   #  7
          ]


def is_adjacent(graph, vert_a, vert_b):
    #Complete the function
    return False


print("Graph A: ")
for i in range(0, 8):
    for j in range(0, 8):
        print("Vertice {0} and vertice {1} are adjacent: {2}".format(i, j, is_adjacent(graph_a, i, j)))


print("Graph B: ")
for i in range(0, 8):
    for j in range(0, 8):
        print("Vertice {0} and vertice {1} are adjacent: {2}".format(i, j, is_adjacent(graph_b, i, j)))        

