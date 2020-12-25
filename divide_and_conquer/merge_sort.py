# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта

def merge_sort(arr):

	
		#divide
	if len(arr) > 1:
		L = arr[:len(arr)//2]
		R = arr[len(arr)//2:]

		L = merge_sort(L) # L
		R = merge_sort(R) # R


		#merge
		K = []
		
		while L != [] and R != []:
			
			if L[0] >= R[0]:
				K.append(R.pop(0))    #L > r

			elif L[0] < R[0]:
				K.append(L.pop(0))	  # R > L 
		





		
		if L != [] or R != []:
			if L != []:      
				K.extend(L)  #L != []
			if R != []:
				K.extend(R)  #R !=[]


		return K
	return arr
				






print(merge_sort([0,21,435,1345,4351345,13450,46,246,5,134,54,6546,54,61,546,54601546,54,65,61,65,546,265,6,265,6,26562,6,5,62,6,]))


