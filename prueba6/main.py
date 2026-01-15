# https://leetcode.com/problems/longest-common-prefix/
#mi solucion
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

#codigo optimizado
"""if not strs:
        return ""

    prefijo = strs[0]

    for palabra in strs[1:]:
        i = 0
        while i < len(prefijo) and i < len(palabra) and prefijo[i] == palabra[i]:
            i += 1
        prefijo = prefijo[:i]

        if prefijo == "":
            return ""
    return prefijo""
"""