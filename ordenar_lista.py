numeros = []

for i in range(5):
    n = int(input("Digite um número: "))
    numeros.append(n)

for i in range(len(numeros)):
    for j in range(0, len(numeros)-i-1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print("Lista ordenada:", numeros)
