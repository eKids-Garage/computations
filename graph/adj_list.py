# Graph A: Non-directed graph
# Vertices:
graph_a = [[3, 4], [2, 4], [1, 3, 5], [0, 2, 5], [0, 1, 5],
           [2, 3, 4]]  # Complete the adjacency list for the Graph A

# Graph B: Directed graph
# Vertices:
graph_b = [[3, 4], [4], [1], [2], [5],
           [2, 3]]  # Complete the adjacency list for the Graph B


def is_adjacent(graph, vert_a, vert_b):

  # я не очень уверен в постановке задания, так что выберите решение которое нужно

  return vert_b in graph[vert_a] or vert_a in graph_b  # Если учитывать что даже в ориентированом графе две вершины смежные


#   return vert_b in graph[vert_a]  # Если учитывать переход из вершины а в б но не наоборот

print(is_adjacent(graph_a, 5, 2))
print(is_adjacent(graph_a, 0, 3))
print(is_adjacent(graph_a, 3, 4))
print(is_adjacent(graph_a, 2, 5))

print(is_adjacent(graph_b, 5, 2))
print(is_adjacent(graph_b, 0, 3))
print(is_adjacent(graph_b, 3, 4))
print(is_adjacent(graph_b, 2, 5))