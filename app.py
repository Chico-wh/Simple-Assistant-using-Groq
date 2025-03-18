matriz_soma = [[],[],[]]
matriz1 = [[1,2,3], [4,5,6], [7,8,9]]
matriz2 = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(len(matriz1[1])):
    for j in range(len(matriz1[2])):
        soma = matriz1[i][j] + matriz2[i][j]
        matriz_soma[i].append(soma)


for items in matriz_soma:
    print(items)
