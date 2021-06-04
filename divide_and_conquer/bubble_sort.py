from random import shuffle,randint

# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

def sort_bubble (arr):
    return buble_sort_recursive(arr)

def buble_sort_recursive(unsorted):
	if len(unsorted) == 1:
		return unsorted
	for idx,i in enumerate(unsorted):
		if idx+1 >= len(unsorted): continue
		if unsorted[idx+1] < i:
			unsorted[idx+1],unsorted[idx] = unsorted[idx],unsorted[idx+1]
	return buble_sort_recursive(unsorted[:-1])+[unsorted[-1]]


def buble_sort_iterative(unsorted): 
	unsorted_length = len(unsorted)
	while unsorted_length > 1:

		for idx in range(unsorted_length):
			if idx+1 >= len(unsorted): continue
			if unsorted[idx+1] < unsorted[idx]:
				unsorted[idx+1],unsorted[idx] = unsorted[idx],unsorted[idx+1]	
		unsorted_length-=1
	return unsorted 


def main():
	unsorted = [randint(0,1000) for i in range(randint(10,20))]
	shuffle(unsorted)

	print(f"unsorted array:   {unsorted}")
	sorted_recursive = buble_sort_recursive(unsorted)
	print(f"sorted recursive: {sorted_recursive}")
	sorted_iterative = buble_sort_iterative(unsorted)
	print(f"sorted iterative: {sorted_iterative}")


if __name__ == '__main__':
	main()