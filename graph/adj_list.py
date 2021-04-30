graph_a = [[3, 4], [2, 4], [1, 3, 5], [0, 2, 5], [0, 1, 5], [2, 3, 4]]
graph_b = [[3, 4], [4], [1], [2], [5], [2, 3]]


def is_adjacent(graph, vert_a, vert_b, prev = None):
    if prev is None:
        prev = []
    p1 = graph[vert_a]
    if vert_b in p1:
        return True
    for point in p1:
        if point not in prev:
          prev.append(point)
          res = is_adjacent(graph, point, vert_b, prev)
          if res == True:
            return True
    return False


print(is_adjacent(graph_a, 5, 2))
print(is_adjacent(graph_a, 0, 3))
print(is_adjacent(graph_a, 3, 4))
print(is_adjacent(graph_a, 2, 5))

print(is_adjacent(graph_b, 5, 2))
print(is_adjacent(graph_b, 0, 3))
print(is_adjacent(graph_b, 3, 4))
print(is_adjacent(graph_b, 2, 5))
