# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
# 
# 1. survive(n, k) - используя массив. 
# 2. survive_num(n, k) - без использования массива 

#initialization
n = int(input("Type the number of warriors:"))
k = int(input("Type the step:"))
i = 0
main_list = []


#making list with warriors
for any_var in range(n + 1):
    main_list.append(any_var)
main_list.remove(0)    


#nice outputing of the initial list
print("Initial list is:")
print(*main_list, sep=", ")


#main function
def survive(n, k):
    
    global i
    
    if len(main_list) < 2:
        return main_list
    else:
        main_list.remove(main_list[(i + k - 1) % len(main_list)])
        i += 1
        return survive(n, k)
    

print("\nThe survivor is warrior with number", *survive(n, k), sep=" ")