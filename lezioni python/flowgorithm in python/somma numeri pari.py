def summ(x:int):
    if x == 0:
        return 0
    elif x%2==0:
        return x + summ(x-2)
    return None


n = int(input())
print(summ(n))
