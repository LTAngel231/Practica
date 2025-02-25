# Se piden los datos de entrada
print()
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

#Se realizan los calculos
if a % b == 0:
    conclusion = "a es divisor de b"
elif b % a == 0:
    conclusion = "b es divisor de a"
else:
     conclusion = "no son divisores"

#Se muestra el resultado
print("el resultado es: ", conclusion)
print()