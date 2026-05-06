notas = []

for i in range(3):
    n = float(input("Digite a nota: "))
    notas.append(n)

media = sum(notas) / len(notas)

print("Média:", media)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
