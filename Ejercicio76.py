def EsMultiplo(a, b):
    return b != 0 and a % b == 0
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if EsMultiplo(num1, num2):
    print(f"El {num1} ES múltiplo de {num2}")
else:
    print(f"El {num1} NO es múltiplo de {num2}")