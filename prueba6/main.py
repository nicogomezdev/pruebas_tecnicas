# https://leetcode.com/problems/longest-common-prefix/
strs=["fdsmr","fdffmr", "kkada"]
lista={}
for k, palabra in enumerate(strs, start=1):
    lista[k] = list(palabra)

print(len(lista))
for i in range(1,len(lista)+1):
    for j in range (0,2):
        print(lista[i][j])
