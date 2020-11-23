N = int(input())

def prime_div_tail(n,k):
    if n < k:
        return 
    if n%k == 0:
        print(k)
        prime_div_tail(n//k, k)
    else:
        prime_div_tail(n, k+1)
prime_div_tail(N,2)


def prime_div_while(n,k):
    while n >= k:
        if n%k==0:
            print(k)
            n=n//k
        else:
            k += 1
prime_div_while(N,2)
    

def prime_div(n,k):
   if n/k < k:
     return [n]
   else:
     if n%k == 0:
       return [k]+prime_div(n//k,k)
     else:
       return prime_div(n,k+1)
print(prime_div(N,2))
