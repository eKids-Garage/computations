def euclid(a, b):
  while a != 0 and b != 0:
    if a > b:
      a = a%b;
    else:
      b = b%a;  
  else:
    if b > a:
      print(b);
    else:
      print(a);

euclid(840, 320);    