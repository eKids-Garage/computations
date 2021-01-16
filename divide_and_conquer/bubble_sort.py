def sort_bubble(massiv): 
    for i in range(len(massiv)-1): 
        for j in range(0, len(massiv)-i-1): 
            if massiv[j] > massiv[j+1] : 
                e = massiv[j+1];
                massiv[j+1] = massiv[j];
                massiv[j] = e;

massiv = [1, 2, 5, 13, 8, 3, 7];
sort_bubble(massiv);
i = 0;
while i < len(massiv):
  print(massiv[i] , ' ');
  i = i + 1