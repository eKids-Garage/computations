graph_a = [[3, 4], [2, 4], [1, 3, 5], [0, 2, 5], [0, 1, 5], [2, 3, 4]] # 

graph_b = [[3, 4], [4], [1], [2], [5], [3, 2]]

def is_adjacent(graph, vert_a, vert_b):
  for n in range (0, len(graph[vert_a])):
    if graph[vert_a][n]==vert_b:
      return True
    if n+1==len(graph[vert_a]):
      return False



print('graph_a')
print(is_adjacent(graph_a, 5, 2))
print(is_adjacent(graph_a, 0, 3))
print(is_adjacent(graph_a, 3, 4))
print(is_adjacent(graph_a, 2, 5))
print('graph_b')
print(is_adjacent(graph_b, 5, 2))
print(is_adjacent(graph_b, 0, 3))
print(is_adjacent(graph_b, 3, 4))
print(is_adjacent(graph_b, 2, 5))

