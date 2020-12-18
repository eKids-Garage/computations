def is_power_of_two(N):
  if N == 2 or N == 1: 
    print('YES') 
  else:
    if N % 2 == 0:
      N = N // 2
      is_power_of_two(N) 
    else:
      print('NO')


is_power_of_two(1)