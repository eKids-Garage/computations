print("Enter your rational numbers (example: 3/7) : ") 

def getDataAndDivideByNumbers (array1,array2) :
    if '/' in array1 and '/' in array2 :
      if '0' not in array1 and '0' not in array2:
        print('hwujg')
        index1 = array1.index('/') 
        x1 = array1[:index1] 
        y1 = array1[index1+1:]

        index2 = array2.index('/') 
        x2 = array2[:index2] 
        y2 = array2[index2+1:]

        x1 = int(''.join(x1)) 
        y1 = int(''.join(y1))
        x2 = int(''.join(x2)) 
        y2 = int(''.join(y2))
        return [x1,y1,x2,y2]
      return ["You have 0 in one of your number! It is not a rational number ."]
    return ["Wrong data !"]
array1 = list(input("first num : "))
array2 = list(input("second Num :" ))

def euclidus(numerator, denominator):
  if numerator == denominator:
    return(numerator)
  else:
    if numerator > denominator:
      return euclidus(numerator - denominator, denominator)
    else:
      return euclidus(numerator, denominator - numerator)

def rat() : # main function
    array = getDataAndDivideByNumbers (array1,array2)
    if type(array[0]) == str:
      return(array[0])
    numerator = array[0] * array[-1] + array[2] * array[1]
    denominator = array[1]*array[-1]
    euclid = euclidus(numerator,denominator)
    numerator = int(numerator / euclid)
    denominator = int(denominator / euclid)
    if numerator > denominator : # если смешанная дробь
      bigNum = int(numerator / denominator )
      #print(" numerator ==",numerator,"denominator ==",denominator,"bigNum == ",bigNum)
      if numerator % denominator == 0 :
        return "Result == " + str(bigNum)
      result = "Result == " + str(bigNum) + '-   ' + str(numerator % denominator ) + "\n\t\t      " + str(denominator)
      return result
    fraction = str(numerator) + "/" + str(denominator)
    result = "Result == " + fraction
    return  result
print(rat())

