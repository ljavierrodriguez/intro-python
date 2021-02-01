# Tipos de Datos
'''
String = str = "a", 'a', """ a """
Number = int = 1 -1
Number = float = 1.1 -1.4
Boolean = bool = True o False
Undefined = None
Null = None
Array = list = []
        tuple = ()
        set = {}

Object = dict = {
    "key": "value"
}
'''
a = "Luis"
b = 1
c = True
d = None
nombres = ["Hugo", "Paco", "Luis"] # list
status = ("Active", "Inactive", "Canceled", "Suspended") # tuple
frutas = {"Piña", "Manzana", "Uva", "Banana", "Mora"} # set

persona = {
    "nombre": "",
    "apellido": ""
} # dict

print(dir(frutas))

class Person:
    nombre = ""

    def __init__(self):
        pass

    def func():
        pass



class Student(Person):
    apellido = ""

    def __init__(self):
        pass

    def func():
        pass


p = Person()
p.func()