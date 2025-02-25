# Se piden los datos de entrada
print()
a = float(input("Longitud primer lado: "))
b = float(input("Longitud segundo lado: "))
c = float(input("Longitud tercer lado: "))


# Se decide qué tipo de triángulo es
if a == b and b == c:
    tipo = "equilátero"
elif a != b and a != c and b != c:
    tipo = "escaleno"
else:
    tipo = "isósceles"


# Se despliega el resultado
print("El triángulo es", tipo)
print()