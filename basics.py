# imprimir en consola
print('hola mundo')

# asignacion (dinamica) de variable (memoria)
a = 1
b = 3
a = 'casa'

# arreglos
lista = [1,2,2,6,5]

# acceso a elementos de lista
print(lista[0])
print(lista[-1])


# diccionarios
diccionario = {
    'bar': 'foo',
    'input': 23 
}

# accesos a atributos de diccionarios
print(diccionario['bar'])
print(diccionario['input'])

# conjuntos
conjuntoa = set(lista)
conjuntob = set([1,3,5,4])
print(conjuntoa.union(conjuntob))

# listas exaustivas
newarr = [x**2 for x in lista]

# maps
objmap = map(lambda x: x**2, lista)

for cuadr in objmap:
    print(cuadr)

# filters
objfilter = filter(lambda x: x % 2 == 0, lista)

# metodos
def my_method(name):
    print(f'hola {name}')

print(my_method('jose'))

# clases
class A:
    def __init__(self, name=None, last_name=None):
        self.name = name
        self.last_name = last_name

    def get_fullname(self):
        return f'{self.name} {self.last_name}'


# herencia
class B(A):
    def get_fullname(self):
        return f'{self.last_name}, {self.name}'


objetoa = A(name='Jose', last_name='Espinoza')
objetob = B('Jose', 'Espinoza')

print(objetoa.get_fullname())
print(objetob.get_fullname())

print('finish!')
