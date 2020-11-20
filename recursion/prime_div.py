# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
c=1

def prime_div(N):
 global c
 if c<N: 
   if N%c==0:
     print(N/c)
     c += 1 
     return prime_div(N)
   else:
    c += 1 
    return prime_div(N)
     

print(1.0)
print(2.0)
prime_div(16)
