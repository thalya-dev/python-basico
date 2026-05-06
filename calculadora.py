a = float(input("Número 1: "))
b = float(input("Número 2: "))
op = input("Operação (+ - * /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Operação inválida")
