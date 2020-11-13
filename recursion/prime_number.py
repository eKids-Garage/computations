# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 

def is_prime(n, k):
  if k <= n / 2:
    if n % k > 0:
      is_prime(n, k + 1)
    else:
      print("NO")
  else:
    print("YES")

n = int(input("Number:"))
k = 2
is_prime(n, k)