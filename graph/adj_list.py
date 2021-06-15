class graph:
  def __init__(self, type, list):
    self.type = type
    self.list = list

graph_a = graph("nonDirected", [[3, 5], [3, 2], [3, 0], [2, 5],
 [2, 1], [1, 4], [0, 4], [4, 5]])

graph_b = graph("directed", [[5, 3], [3, 2], [0, 3], [5, 2], 
  [2, 1], [1, 4], [0, 4], [4, 5]])


def is_adjacent(graph, vert_a, vert_b):
    if graph.type == "nonDirected":
      i = 0
      while i < len(graph.list):
        if vert_a in graph.list[i] and vert_b in graph.list[i]:
          return True
        i += 1
      return False 
    else:
      i = 0
      while i < len(graph.list):
        if graph.list[i][0] == vert_a and graph.list[i][1] == vert_b:
          return True
        i += 1
      return False
    
print("Graph a: ")
print(is_adjacent(graph_a, 5, 2))
print(is_adjacent(graph_a, 0, 3))
print(is_adjacent(graph_a, 3, 4))
print(is_adjacent(graph_a, 2, 5))

print("Graph b: ")
print(is_adjacent(graph_b, 5, 2))
print(is_adjacent(graph_b, 0, 3))
print(is_adjacent(graph_b, 3, 4))
print(is_adjacent(graph_b, 2, 5))
