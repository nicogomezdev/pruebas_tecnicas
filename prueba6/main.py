# https://leetcode.com/problems/longest-common-prefix/
strs=["fdsmr","fdffmr"]
lista=[]
sublista=[]

for i in range(len(strs)):
    resul= list(strs[i])
    lista.append(resul)

for k in range(len(lista)):
    sublista.append("".join(lista[k][:2]))
    
print(sublista)

if all(elem == sublista[0] for elem in sublista):
    print(type(sublista[1]))
    
else :
    print("")