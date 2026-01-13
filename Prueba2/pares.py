lista = [15,10,8,7]

def pares(arr):
    total=[]
    for i in arr:
        if i%2==0:
            total.append(i)
    return total
print(pares(lista))


