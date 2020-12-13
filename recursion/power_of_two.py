def is_power_of_two(N):
  if(N == 1):
    return 'YES'
  if(N % 2 != 0):
    return 'NO'
  if(N == 2):
    return 'YES'
  return(is_power_of_two(N // 2))
N = int(input())
print(is_power_of_two(N))