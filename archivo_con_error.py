# Código con un error para la práctica de Git y GitHub
# Código con un error para la práctica de Git y GitHub

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    # ERROR: No maneja el caso cuando b es 0
    return a / b

# Pruebas
num1 = 10
num2 = 0  # Aquí está el error: la división por cero genera un error

print("Suma:", suma(num1, num2))
print("Resta:", resta(num1, num2))
print("Multiplicación:", multiplicacion(num1, num2))
print("División:", division(num1, num2))  # Provocará un error si num2 es 0

2242041623
