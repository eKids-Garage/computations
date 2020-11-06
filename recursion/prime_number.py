# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
def is_prime(N, c):
  if(N % c == 0):
    print("No")
  else:
    if(c < N-1):
      c = c + 1
      is_prime(N, c)
    else:
      print("YES")

N = int(input("Input any number: "))
c = 2
is_prime(N, c)
