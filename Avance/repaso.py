def suma(a, b):
    res = a + b
    print(f"El resultado es: {res}")

def resta(a, b):
    res = a - b
    print(f"El resultado es: {res}")

def multi(a, b):
    res = a * b
    print(f"El resultado es: {res}")

def division(a, b):
    if b == 0:
        print("No se puede dividir por cero.")
    else:
        res = a / b
        print(f"El resultado es: {res}")

# Programa principal
print("Calculadora")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

suma(a, b)
resta(a, b)
multi(a, b)
division(a, b)
