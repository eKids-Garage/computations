n = int(input('Enter your number : '))
def power_of_two(n):
    if n % 2 == 0:
        if n == 2 :
            return "Yes"
        return power_of_two(n//2)
    else:
       return "No"
'''
print(power_of_two(128)) # Yes
print(power_of_two(16))  # Yes
print(power_of_two(32))  # Yes
print(power_of_two(64))  # Yes
print(power_of_two(1212))# No
print(power_of_two(5332))# No
'''
print(power_of_two(n))
