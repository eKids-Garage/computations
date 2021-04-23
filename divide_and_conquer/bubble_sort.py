# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

def sort_bubble (arr):
	Sort_list = [0]
	for element in arr:
		for curret in range(0,len(Sort_list)):
			#print(curret,element,Sort_list)
			if element < Sort_list[curret] or element == Sort_list[curret]:
				Sort_list.insert(curret, element)
				break
			if curret == len(Sort_list)-1:
				Sort_list.insert(-1,element)
	Sort_list.pop()			
	return Sort_list

N=[6,1,2,4,5,3,7,32]
print(sort_bubble(N))
