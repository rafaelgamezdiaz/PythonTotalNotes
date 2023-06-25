class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return int(self.cantidad_paginas)

    def __del__(self):
        print('Libro eliminado')


milibro = Libro('El señor de los anillos', 'J.R.R. Tolkien', 1500);

print(milibro)
print(len(milibro))
del milibro
