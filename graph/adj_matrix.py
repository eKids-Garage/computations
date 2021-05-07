# Graph A: Non-directed graph

          #  0  1  2  3  4  5  6  7
graph_a = [ [0, 0, 0, 1, 1, 0, 1, 0],  #  0
            [0, 0, 1, 0, 1, 0, 0, 0],  #  1
			[0, 1, 0, 0, 0, 1, 0, 0],  #  2
            [1, 0, 0, 0, 0, 1, 1, 0],  #  3
            [1, 1, 0, 0, 0, 0, 0, 1],  #  4
            [0, 0, 1, 1, 0, 0, 0, 1],  #  5
            [1, 0, 0, 1, 0, 0, 0, 1],  #  6
            [0, 0, 0, 0, 1, 1, 1, 0]   #  7
          ]



# Graph B: Directed graph

          #  0  1  2  3  4  5  6  7
graph_b = [ [0, 0, 0, 1, 1, 0, 1, 0],  #  0
            [0, 0, 0, 0, 1, 0, 0, 0],  #  1
			[0, 1, 0, 0, 0, 0, 0, 0],  #  2
            [0, 0, 0, 0, 0, 1, 1, 0],  #  3
            [0, 0, 0, 0, 0, 0, 0, 1],  #  4
            [0, 0, 1, 0, 0, 0, 0, 1],  #  5
            [0, 0, 0, 0, 0, 0, 0, 1],  #  6
            [0, 0, 0, 0, 0, 0, 0, 0]   #  7
          ]


def is_adjacent(graph, vert_a, vert_b):
	och = []
	ver = []
	for i in range (8):
		if (graph[vert_a][i] == 1):
			och.append(i)
	while (len(och) > 0):
		if (och[0] == vert_b):
			return True
		elif (och[0] not in ver):
			ver.append(och[0])
			for i in range (8):
				if (graph[och[0]][i] == 1):
					och.append(i)
			och.pop(0)
		else:
			och.pop(0)
	return False


print("Graph A: ")
for i in range(0, 8):
    for j in range(0, 8):
        print("Vertice {0} and vertice {1} are adjacent: {2}".format(i, j, is_adjacent(graph_a, i, j)))


print("Graph B: ")
for i in range(0, 8):
    for j in range(0, 8):
        print("Vertice {0} and vertice {1} are adjacent: {2}".format(i, j, is_adjacent(graph_b, i, j)))        

