# Напишите функцию, которая складывает два рациональных числа
# Структуру данных для хранения чисел выберите и реализуйте сами
#initializtion
num_1 = []
num_2 = []

num_1.append(int(input("Type the numerator of the first number:")))
num_1.append(int(input("Type the denominator of the first number:")))

num_2.append(int(input("\nType the numerator of the second number:")))
num_2.append(int(input("Type the denominator of the second number:")))



#function that finds the least common multiple
def gcd(a, b):
    if a == b:
        return a
    
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)
  


#function that finds least common multiple with help of the least common multiple
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
    

#main function
def sum_rat(num_1, num_2):
    num_1[0] = (lcm(num_1[1], num_2[1]) // num_1[1]) * num_1[0]
    num_2[0] = (lcm(num_1[1], num_2[1]) // num_2[1]) * num_2[0]
    num_1[1] = lcm(num_1[1], num_2[1])
    num_2[1] = lcm(num_1[1], num_2[1])
    
    #outing
    print("\nYour expression is: " + str(num_1[0]) + "/" + str(num_1[1]) + " + " + str(num_2[0]) + "/" + str(num_2[1]) + " = " + str((num_1[0] + num_2[0]) // gcd(num_1[0] + num_2[0], num_1[1]|num_2[1])) + "/" + str((num_1[1]|num_2[1]) // gcd(num_1[0] + num_2[0], num_1[1]|num_2[1])))


print(sum_rat(num_1, num_2))