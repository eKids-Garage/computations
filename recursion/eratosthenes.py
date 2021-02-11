# Написать программу, которая находит все простые числа в заданном 
# интервале методом "Решето Эратосфена". 
# start и finish - границы диапазона (включительно).

#retrieving two borders
start = int(input("Type first border: "))
finish = int(input("Type the second border: "))


#main function
def sieve(start, finish):
  
  
    #creating the main list with numbers from which you want to find prime numbers
    main_list = []
    for list_num in range(start, finish + 1):
        main_list.append(list_num)
        
    #outputing of this list
    print("Initial list:")    
    print(*main_list, sep=", ")
    
    #getting variable with first number with which we begin
    #to filter out complex numbers 
    num = 2
    
    #main algorithm
    while num <= finish // 2: 
        if num != 0: 
            num_plus_num = num + num
            while num_plus_num <= finish:
                if num_plus_num in main_list:
                    main_list[main_list.index(num_plus_num)] = 0
                num_plus_num = num_plus_num + num
        num += 1


    #removing accumulated zeros
    main_list = set(main_list)
    main_list.remove(0)
    
    
    #outputing prime numbers from list
    print("\nOnly prime numbers from initial list:")    
    print(*main_list, sep=", ")



print(sieve(start, finish))
