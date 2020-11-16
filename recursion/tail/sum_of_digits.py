def sum(Value):

  Num=Value%10
  Value=Value//10

  if(Value!=0):
    return sum(Value)+Num


  else:
    return Num
    print(Value)

    
