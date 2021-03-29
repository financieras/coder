import sys

valor1 = int(sys.argv[1])
valor2 = int(sys.argv[2])
# para ejecutar tecleamos en la terminal:
# python3 calculadora.py 2 3


def suma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

# llamamos a la función suma 
# y le pasamos los dos parámetros
print(suma(valor1,valor2))

