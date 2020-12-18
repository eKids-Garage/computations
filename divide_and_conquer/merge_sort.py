# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта
import random
main_list = []



#learning the information about the list
length_of_stock_list = input("Type the length of your list:")
length_of_stock_list = int(length_of_stock_list)
max_number = input("Type the maximum number in your list:")
max_number = int(max_number)


#creating the list
for number in range(length_of_stock_list):
    main_list.append(random.randint(0, max_number))
print(main_list)



def merge(L, R):
    #creating some variables for further convenience
    sorted_list = []
    l_li =  0 #left list index
    r_li = 0  #right list index
  
    l_ll = len(L) #the length of left list
    r_ll =  len(R) #the length of right list
    
    #comparing first numbers
    for any_variable in range(l_ll + r_ll):
        if l_li < l_ll and r_li < r_ll:
            
            #adding numbers from left list(L)
            if L[l_li] <= R[r_li]:
                sorted_list.append(L[l_li])
                l_li += 1
            else:
                 #adding numbers from left right(R)
                sorted_list.append(R[r_li])
                r_li += 1

        #end of left list(L)       
        elif l_li == l_ll:
            sorted_list.append(R[r_li])
            r_li += 1
            
        #end of right list(R)
        elif r_li == r_ll:
            sorted_list.append(L[l_li])
            l_li += 1

    return sorted_list



def merge_sort(main_list):
    if len(main_list) == 1:
        return main_list
    
    mid = len(main_list) // 2
    L = main_list[:mid]
    R = main_list[mid:]

    L = merge_sort(L)
    R = merge_sort(R)
    
    return merge(R, L)

print(merge_sort(main_list))