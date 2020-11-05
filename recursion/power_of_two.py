
N = int(input())
def power(x):
    if x == 1 or x == 2:
        return ("YES")
    elif x % 2 != 0:
        return ("NO")
    else:
        return power(x//2)
print(power(N))