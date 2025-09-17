def find_min(a):
    min = 0
    for n in a:
        if n < min:
            min = a[a.index(n)]
    return min

def find_max(a):
    max = 0
    for n in a:
        if n > max:
            max = a[a.index(n)]
    return max

def multiply_max_min(a):
    multi_max = a[a.index(find_max(a))] * a[a.index(find_min(a))]
    a[a.index(find_max(a))] = multi_max
    return a

array = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f"prima della modifica ->  {array}")
mod_array = multiply_max_min(array)
print(f"dopo la modifica ->  {mod_array}")