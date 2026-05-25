print("Hola mundo inhumano")

def minium (a,b):

    if(a<=b):
        return a
    else:
        return b
a = 2
b = 4 
print(minium(a,b))

def rev_sentence(sentence):
    words= sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence

if __name__ == "__main__":
    input = ' geeks quiz ractice code' 
    print (rev_sentence(input))
#Realizar una suma de los elementos de una tupla

test_tup = (7, 8, 9, 1, 10, 7)
print ("the original tuple is : " + str(test_tup))
#Escriba un código que calcule una lista de números proporcionados.
res = sum (list(test_tup))
print ("la suma de los elementos d ela tuple es: " + str(res))
#Escriba un código que calcule una lista de números proporcionados.
def list_sum(num_list):
    if len(num_list)==1:
        return num_list[0]
    else: 
        return num_list[0] + list_sum(num_list[1:])
print (list_sum([3,5,8,9,9]))
#Escriba un código que desordene al azar una lista.
from random import shuffle 
x = ['tu', 'es', 'madre','guapa']
shuffle (x)
print (x)
#6. Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.

'''archivo = "archivo.txt"

with open(archivo) as fh:
    text = fh.read()

count = 0

for character in text:
    if character.isupper():
        count += 1

print(count)'''
#8. Escriba un programa para producir la serie Fibonacci en Python.
#9. Escriba un programa en Python para comprobar si un número es primo.
#10. Escribir un programa en Python para comprobar si un número es capicúa. Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.

#11. Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.
try:
    if '1' != 1:
        raise Exception("algun error")
    else:
        print("no")
except Exception:
    print("si")
    #14. ¿Como se puede acceder al último índice de una lista?

Respuesta: Supongamos que la lista1 es [2, 33, 222, 14, 25], Entonces mediante, lista1 [-1] obtendremos el ultimo índice de la lista. Es decir, 25.