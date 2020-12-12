# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта

def merge(a, b):
    c = []
    i = 0
    j = 0
    while len(c) != len(a) + len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
        if i == len(a):
            while j < len(b):
                c.append(b[j])
                j += 1
        if j == len(b):
            while i < len(a):
                c.append(a[i])
                i += 1
            
    return c
    

def merge_sort(a):
    if len(a) == 1:
        return a
    else:
        n = len(a) // 2
        a1 = merge_sort(a[:n])
        a2 = merge_sort(a[n:])
        return merge(a1, a2)

