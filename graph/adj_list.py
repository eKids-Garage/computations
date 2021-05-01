import random

# Graph A: Non-directed graph
# Vertices:
graph_a = [[3,4],[2,4],[1,3,5],[0,2,5],[0,1,5],[2,3,4]]


# Graph B: Directed graph
# Vertices:
graph_b = [[3, 4], [4],[1],[2],[5],[2,3]]


def is_adjacent(graph, vert_a, vert_b):
	och = graph[vert_a]
	ver = []
	while (len(och) > 0):
		if (och[0] == vert_b):
			return True
		elif (och[0] not in ver):
			ver.append(och[0])
			for i in range (len(graph[och[0]])):
				och.append(graph[och[0]][i])
			och.pop(0)
		else:
			och.pop(0)
	return False

print(is_adjacent(graph_a, 5, 2))
print(is_adjacent(graph_a, 0, 3))
print(is_adjacent(graph_a, 3, 4))
print(is_adjacent(graph_a, 2, 5))

print(is_adjacent(graph_b, 5, 2))
print(is_adjacent(graph_b, 0, 3))
print(is_adjacent(graph_b, 3, 4))
print(is_adjacent(graph_b, 2, 5))
print()
print(is_adjacent(graph_b, random.randint(0, 5), 0))

