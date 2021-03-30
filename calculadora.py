
import sys

valor1 = int(sys.argv[1])
valor2 = int(sys.argv[2])
operacion = sys.argv[3]
# para ejecutar tecleamos en la terminal:
# python3 calculadora.py 2 3 suma

def suma(numero1, numero2):
    resultado = numero1 + numero2
    return 
def resta(numero1, numero2):
    resultado = numero1 - numero2
    return resultado
def multiplica(numero1, numero2):
    resultado = numero1 * numero2
    return resultado
def divide(numero1, numero2):
    resultado = numero1 / numero2
    return resultado

if operacion =="suma":
    print(suma(valor1,valor2))
elif operacion =="resta":
    print(resta(valor1,valor2))
elif operacion =="multiplica":
    print(multiplica(valor1,valor2))
elif operacion =="divide":
    print(divide(valor1,valor2))
else:
    print("Operación no reconocida")