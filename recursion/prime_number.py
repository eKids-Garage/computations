def is_prime(N, k):

    if N==1 or k>(N/2):
        return "YES!!"

    if N%k==0 :
        return "NO!!"

    return is_prime(N, k+1)
