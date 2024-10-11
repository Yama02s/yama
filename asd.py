
class Biblioteca:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Biblioteca: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"



class Libro:
    def __init__(self, ISBN, titulo, autor):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo}, ISBN: {self.ISBN}, Autor: {self.autor}"



class DetalleLibro:
    def __init__(self, categoria, numero_paginas, editorial):
        self.categoria = categoria
        self.numero_paginas = numero_paginas
        self.editorial = editorial

    def __str__(self):
        return f"Detalle del libro - Categoría: {self.categoria}, Páginas: {self.numero_paginas}, Editorial: {self.editorial}"



class Editorial:
    def __init__(self, indice, nombre, telefono):
        self.indice = indice
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Editorial: {self.nombre}, Índice: {self.indice}, Teléfono: {self.telefono}"


class Usuario:
    def __init__(self, nombre, numero_identificacion, correo, celular, habilitado):
        self.nombre = nombre
        self.numero_identificacion = numero_identificacion
        self.correo = correo
        self.celular = celular
        self.habilitado = habilitado

    def __str__(self):
        return f"Usuario: {self.nombre}, Identificación: {self.numero_identificacion}, Correo: {self.correo}, Celular: {self.celular}, Habilitado: {self.habilitado}"

class Prestamo:
    def __init__(self, isbn, numero_identificacion, fecha_prestamo, fecha_entrega):
        self.isbn = isbn
        self.numero_identificacion = numero_identificacion
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega

    def __str__(self):
        return f"Préstamo - ISBN: {self.isbn}, Identificación Usuario: {self.numero_identificacion}, Fecha Préstamo: {self.fecha_prestamo}, Fecha Entrega: {self.fecha_entrega}"
    