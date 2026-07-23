"""


nombre
productos
costo_delivery

solicitar __nombre
solicitar __costo del delivery
__productos
"""
from abc import ABC, abstractmethod 

class Tienda(ABC):
    @abstractmethod
    def ingresar_producto(self):
       pass

    @abstractmethod
    def listar_productos(self):
       pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
       pass

class Restaurante(Tienda):
    def listar_productos(self):
        return ...
   
    def realizar_venta(self, nombre_producto, cantidad):
        return ...
   
class Farmacia(Tienda):
    def listar_productos(self):
        return ...
   
    def realizar_venta(self, nombre_producto, cantidad):
        return ...
   
class Producto:
    def __init__(self, nombre, precio, stock=0):       
        self.__nombre = nombre
        self.__precio = precio
        if stock < 0:
           stock = 0
        self.__stock = stock 
    
    @property
    def nombre(self):
       return self.__nombre
    
    @property
    def precio(self):
       return "$" + str(self.__precio)
    
    @property
    def stock(self):
       return self.__stock
    
    @stock.setter
    def stock(self, stock):
        if stock < 0:
           stock = 0
        self.__stock = stock 

loratadina = Producto("loratadina", 10_000, -5)
print(loratadina.stock)
loratadina.stock = -10
print(loratadina.stock)
print(loratadina.precio)
print(loratadina.nombre)


