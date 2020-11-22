N = int(input())
def prime_div(n,k):
    if n < k:
        return
    if n % k == 0:
        print(k)
        prime_div(n//k, k)
    else:
     prime_div(n, k+1)
prime_div(N,2)
