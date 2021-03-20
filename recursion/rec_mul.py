# чила могут быть не одинаковы,разной длины, большими
# если нужно почитать очень большие числа , то в конце программы там где печатется результат нужно будет убрать окргуление (из-за него последние цифры будут не правильны)

def rec_mul(x, y, n): 
  if n <= 1:
    return x*y
  else:
    a = x // 10**(n/2)  
    b = x % 10**(n/2)      
    c = y // 10**(n/2)      
    d = y % 10**(n/2)      

    part1 = rec_mul(a,c,n/2) * (10**n)
    part2 = rec_mul(b,d,n/2)
    part3 = rec_mul(b,c,n/2) * 10**(n/2)
    part4 = rec_mul(a,d,n/2) * 10**(n/2)
    result = part1 + part2 + part3 + part4
    return  result

x = (input("Введи х: ")) # 123
y = (input("Введи y: "))# 123456789
n = (len(x) + len(y))/2
x = int(x)
y = int(y)


print("\tsimple multiplication :   ",x*y) #  15185185047
result = rec_mul(x, y, n)
print("\trecursion multiplication :",round(result))#  округляю результат потому что иногда получается результат = 15233729.999999996 => результат = 15233730


