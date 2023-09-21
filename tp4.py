#Crea una función lambda que tome un número como argumento y devuelva su cuadrado.

potencia = lambda x: x**2

potencia(6)

#Crea una función lambda que tome dos números como argumentos y devuelva su suma.

suma = lambda x,y: x + y

suma(2,3)

#Crea una función lambda que devuelva el mayor de dos números.

mayor = lambda x,y: x if x > y else y
mayor(6,9)

#A partir de una lista de números existente, crear una nueva lista incrementando en un 15% los valores originales usando map.

list_num = [2,5,7,2,8,4]

num_incrementados = list(map(lambda x: x * 0.15 + x ,list_num))


#Ordenar una lista de diccionarios por un elemento del diccionario. ej: ordenar por edad la siguiente lista:

personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]

sorted(personas, key=lambda x: x["edad"])

#Dada una lista con números, filtrar los números pares y devolverlos en una nueva lista.

list_number = [3,5,4,6,7,34]

list_pares = list(filter(lambda x: x % 2 == 0 ,list_number))



#Dada una lista de temperaturas en grados celsius generar una nueva lista con las temperaturas expresadas en grados fahrenheit, la fórmula para convertir la temperatura es °F=(°C*(9/5))+32.

temperaturas = [32,12,6,-9]

temp_farengheint = list(map(lambda x: (x *(9/5)) + 32,temperaturas))

#Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar la lista de acuerdo a la longitud de las palabras.

list_palabras = ["hola", "todobien", "es", "mañana"]

orden_palabras = sorted(list_palabras,key = lambda x: len(x))


#Dada una lista de palabras, generar una lista con las iniciales de cada palabra.

lista_palabras = ["Jorge","Holu","Cahu"]

nueva_lista = list(map(lambda x : x[0].split() ,lista_palabras))


#Dada una lista de diccionarios con los alumnos y notas de un curso, calcular el promedio del curso. Puede usar una lista como la siguiente:

# lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]

# promedio = note for note in 

# print(promedio)

