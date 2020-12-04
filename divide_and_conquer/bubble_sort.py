# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.


#importing libraries and creating variables
import random
num_of_digits = random.randint(2, 15)
list_nums = []
v_1 = 0
v_2 = 0


#creating list with random length and digits
for list_of_nums in range(num_of_digits):
    list_nums.append(random.randint(0, 99))
print("Original list")    
print(list_nums)


#the main loop for bubble sort
while v_1 < num_of_digits - 1:
    v_2 = 0
    while v_2 < num_of_digits - 1 - v_1:
        if list_nums[v_2] > list_nums[v_2 + 1]:
            #process of element xchanging
            list_nums[v_2], list_nums[v_2 + 1] = list_nums[v_2 + 1], list_nums[v_2]
        v_2 = v_2 + 1
    v_1 = v_1 + 1
    
print("\nList after bubble sort")    
print(list_nums)