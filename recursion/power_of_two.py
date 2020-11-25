

def is_power_of_two(N):
    if N==0 or N==1:
        return "YES!"
    elif N%2!=0:
        return "NO!"

    return is_power_of_two(N/2)
