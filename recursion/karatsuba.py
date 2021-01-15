#retrieving two numbers
x = input("Type your first number with 'power of two' size:")
x = int(x)
y = input("Type your second number with 'power of two' size:")
y = int(y)

#retrieving N
N = len(str(x))


#method 'recursive multiplication'
def rec_mult(x, y, N):
    
    if N == 1:
        return x * y
    else:
        a = x // 10**(N//2)
        b = x % 10**(N//2)
        c = y // 10**(N//2)
        d = y % 10**(N//2)
        
        return 10**N * rec_mult(a, c, N//2) + 10**(N//2) * rec_mult(a, d, N//2) + 10**(N//2) * rec_mult(b, c, N//2) + rec_mult(b, d, N//2) 
        


#karatsuba method
def karatsuba(x, y, N):
    
    if N == 1:
        return x * y
    else:
        
       a = x // 10**(N//2)
       b = x % 10**(N//2)
       c = y // 10**(N//2)
       d = y % 10**(N//2)
    
    
       res_1 = karatsuba(a, c, N//2)
       res_2 = karatsuba(b, d, N//2)
       res_3 = karatsuba(a + b, c + d, N//2)
       res_4 = res_3 - res_2 - res_1
       res_5 = res_1 * 10**N + res_4 * 10**(N//2) + res_2
       
       return res_5
       
       
print('\nThe result after rec_ mult:' + str(rec_mult(x, y, N)))
print('The result after karatsuba:' + str(karatsuba(x, y, N)))
print('The result after usual calculating:' + str(x * y))