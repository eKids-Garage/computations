graph_a = [[3, 4], [2, 4], [1, 3, 5], [0, 2, 5], [0, 1, 5], [2, 3, 4]]
graph_b = [[3, 4], [4], [1], [2], [5], [3, 2]]


def is_adjacent(graph, vert_a, vert_b):
	arr = [graph[vert_a][i] for i in range(len(graph[vert_a]))]


	while len(arr):
		for vert in range(len(arr) - 1, -1,-1):
			if arr[vert] == vert_a:
				return False
			elif arr[vert] == vert_b:
				return True
		
		for i in range(len(arr)):
			ind = arr[0]
			del arr[0]
			arr += graph[ind]
		

	return False


print(is_adjacent(graph_a, 5, 2))
print(is_adjacent(graph_a, 0, 3))
print(is_adjacent(graph_a, 3, 4))
print(is_adjacent(graph_a, 2, 5))

print(is_adjacent(graph_b, 5, 2))
print(is_adjacent(graph_b, 0, 3))
print(is_adjacent(graph_b, 3, 4))
print(is_adjacent(graph_b, 2, 5))
