def sumPar(arr):
    lista=[]
    for i in arr:
        if i%2==0:
            lista.append(i)
    return sum(lista)

print(sumPar([1,2,3,4]))