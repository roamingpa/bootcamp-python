# 🧩 Ayuda Memoria — Características de POO en Python

> Los pilares de la Programación Orientada a Objetos explicados con ejemplos. Sin complicaciones.

---

## 📋 Índice

1. [Herencia](#1-herencia)
2. [Encapsulamiento](#2-encapsulamiento)
3. [Abstracción](#3-abstracción)
4. [Polimorfismo](#4-polimorfismo)
5. [Composición](#5-composición)
6. [Agregación](#6-agregación)
7. [Colaboración](#7-colaboración)
8. [Herencia múltiple](#8-herencia-múltiple)
9. [Resumen comparativo](#9-resumen-comparativo)

---

## 1. Herencia

Una clase **hija** reutiliza atributos y métodos de una clase **padre**.  
Relación: *"es un"* → un `Perro` **es un** `Animal`.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def respirar(self):
        print(f"{self.nombre} respira")

class Perro(Animal):              # Perro hereda de Animal
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")

fido = Perro("Fido")
fido.respirar()   # heredado de Animal → Fido respira
fido.ladrar()     # propio de Perro   → Fido dice: ¡Guau!
```

### `super()` — llamar al padre

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)   # delega al __init__ del padre
        self.raza = raza

fido = Perro("Fido", "Labrador")
print(fido.nombre, fido.raza)  # Fido Labrador
```

---

## 2. Encapsulamiento

Ocultar los detalles internos de un objeto y controlar el acceso a sus datos.  
Relación: *"los datos son míos, accede por mis métodos"*.

| Convención | Acceso | Ejemplo |
|-----------|--------|---------|
| `atributo` | Público — desde cualquier lugar | `self.nombre` |
| `_atributo` | Protegido — señal de "no tocar" | `self._saldo` |
| `__atributo` | Privado — Python cambia el nombre | `self.__pin` |

```python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular      # público
        self._saldo  = saldo        # protegido
        self.__pin   = "1234"       # privado

    # Getter — leer el saldo de forma controlada
    def get_saldo(self):
        return self._saldo

    # Setter — modificar con validación
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto

cuenta = CuentaBancaria("Ana", 100_000)
cuenta.depositar(50_000)
print(cuenta.get_saldo())   # 150000
# print(cuenta.__pin)       # ❌ AttributeError
```

### `@property` — getter/setter elegante

```python
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):              # getter
        return self._celsius

    @celsius.setter
    def celsius(self, valor):       # setter con validación
        if valor < -273.15:
            raise ValueError("Temperatura imposible")
        self._celsius = valor

    @property
    def fahrenheit(self):           # calculado al vuelo
        return self._celsius * 9/5 + 32

t = Temperatura(100)
print(t.celsius)      # 100
print(t.fahrenheit)   # 212.0
t.celsius = 0
print(t.fahrenheit)   # 32.0
```

---

## 3. Abstracción

Definir una **interfaz común** sin implementar los detalles.  
Obliga a las clases hijas a implementar ciertos métodos.  
Se logra con el módulo `abc` (Abstract Base Classes).

```python
from abc import ABC, abstractmethod

class Figura(ABC):                  # clase abstracta — no se puede instanciar
    @abstractmethod
    def area(self):                 # método abstracto — las hijas DEBEN implementarlo
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def describir(self):            # método concreto — se hereda tal cual
        print(f"Área: {self.area()} | Perímetro: {self.perimetro()}")

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto  = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14159 * self.radio

r = Rectangulo(4, 5)
r.describir()   # Área: 20 | Perímetro: 18

# f = Figura()  # ❌ TypeError: no se puede instanciar una clase abstracta
```

---

## 4. Polimorfismo

El **mismo método** se comporta distinto según el objeto que lo llame.  
Relación: *"misma interfaz, distinto comportamiento"*.

```python
class Perro:
    def hablar(self):
        return "¡Guau!"

class Gato:
    def hablar(self):
        return "¡Miau!"

class Pato:
    def hablar(self):
        return "¡Cuac!"

# La función no sabe ni le importa qué tipo de animal recibe
def hacer_hablar(animal):
    print(animal.hablar())

animales = [Perro(), Gato(), Pato()]
for a in animales:
    hacer_hablar(a)
# ¡Guau!
# ¡Miau!
# ¡Cuac!
```

### Polimorfismo con herencia (override)

```python
class Vehiculo:
    def mover(self):
        print("El vehículo se mueve")

class Auto(Vehiculo):
    def mover(self):
        print("El auto rueda por la pista")

class Barco(Vehiculo):
    def mover(self):
        print("El barco navega por el mar")

for v in [Auto(), Barco(), Vehiculo()]:
    v.mover()
```

---

## 5. Composición

Un objeto **contiene** a otro objeto como parte de sí mismo.  
Si el contenedor se elimina, el contenido también desaparece.  
Relación: *"tiene un"* (dependiente) → un `Auto` **tiene un** `Motor`.

```python
class Motor:
    def __init__(self, cilindros):
        self.cilindros = cilindros

    def encender(self):
        print(f"Motor de {self.cilindros} cilindros encendido")

class Auto:
    def __init__(self, marca, cilindros):
        self.marca  = marca
        self.motor  = Motor(cilindros)   # Auto CREA y posee el Motor

    def arrancar(self):
        print(f"{self.marca} arrancando...")
        self.motor.encender()

auto = Auto("Toyota", 4)
auto.arrancar()
# Toyota arrancando...
# Motor de 4 cilindros encendido

# Si el auto desaparece, el motor también
```

---

## 6. Agregación

Un objeto **contiene una referencia** a otro, pero ambos pueden existir por separado.  
Si el contenedor se elimina, el contenido **sigue existiendo**.  
Relación: *"tiene un"* (independiente) → un `Departamento` **tiene** `Empleados`.

```python
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Departamento:
    def __init__(self, nombre):
        self.nombre     = nombre
        self.empleados  = []         # recibe objetos creados afuera

    def agregar(self, empleado):
        self.empleados.append(empleado)

    def listar(self):
        for e in self.empleados:
            print(f"  - {e.nombre}")

# Los empleados existen independientemente del departamento
ana   = Empleado("Ana")
pedro = Empleado("Pedro")

depto = Departamento("Tecnología")
depto.agregar(ana)
depto.agregar(pedro)
depto.listar()
# - Ana
# - Pedro

# Si el departamento desaparece, Ana y Pedro siguen existiendo
del depto
print(ana.nombre)   # Ana  ✅
```

---

## 7. Colaboración

Dos objetos **interactúan entre sí** llamándose mutuamente sus métodos.  
No hay jerarquía ni contención — simplemente trabajan juntos.  
Relación: *"usa a"* → un `Cajero` **usa a** un `Producto` para calcular el total.

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Cajero:
    def cobrar(self, productos):
        total = 0
        for p in productos:
            total += p.precio           # Cajero colabora con Producto
            print(f"  {p.nombre}: ${p.precio}")
        print(f"Total: ${total}")

carrito = [
    Producto("Café",    2500),
    Producto("Pan",     1200),
    Producto("Jugo",    1800),
]

cajero = Cajero()
cajero.cobrar(carrito)
# Café: $2500
# Pan: $1200
# Jugo: $1800
# Total: $5500
```

---

## 8. Herencia múltiple

Una clase puede heredar de **más de una clase padre**.

```python
class Volador:
    def volar(self):
        print("¡Estoy volando!")

class Nadador:
    def nadar(self):
        print("¡Estoy nadando!")

class Pato(Volador, Nadador):   # hereda de ambas
    def hablar(self):
        print("¡Cuac!")

donald = Pato()
donald.volar()   # ¡Estoy volando!
donald.nadar()   # ¡Estoy nadando!
donald.hablar()  # ¡Cuac!
```

> ⚠️ Con herencia múltiple puede haber conflicto si ambos padres tienen el mismo método.  
> Python resuelve el orden con el **MRO** (Method Resolution Order) — de izquierda a derecha.

```python
print(Pato.__mro__)
# (<class 'Pato'>, <class 'Volador'>, <class 'Nadador'>, <class 'object'>)
```

---

## 9. Resumen comparativo

| Característica | Relación | Pregunta clave | Ejemplo |
|---------------|---------|----------------|---------|
| **Herencia** | *"es un"* | ¿Es una subclase? | `Perro` es un `Animal` |
| **Encapsulamiento** | *"oculta"* | ¿Controla el acceso a sus datos? | `__pin`, `_saldo` |
| **Abstracción** | *"define interfaz"* | ¿Obliga a implementar métodos? | Clase abstracta con `ABC` |
| **Polimorfismo** | *"misma interfaz"* | ¿Mismo método, distinto resultado? | `.hablar()` en Perro, Gato, Pato |
| **Composición** | *"tiene un"* (dependiente) | ¿El hijo no existe sin el padre? | `Auto` crea su `Motor` |
| **Agregación** | *"tiene un"* (independiente) | ¿Pueden existir por separado? | `Departamento` recibe `Empleados` |
| **Colaboración** | *"usa a"* | ¿Se pasan como argumento? | `Cajero` recibe `Producto` |
| **Herencia múltiple** | *"es un + un"* | ¿Hereda de más de una clase? | `Pato(Volador, Nadador)` |

```
Herencia        → clase Hija(Padre)
Encapsulamiento → self._protegido / self.__privado / @property
Abstracción     → class MiClase(ABC) + @abstractmethod
Polimorfismo    → override de métodos / duck typing
Composición     → self.parte = ClaseParte(args)      # creado adentro
Agregación      → self.parte = parte                  # recibido por parámetro
Colaboración    → def metodo(self, otro_objeto):      # pasado como argumento
Herencia múltiple → class Hija(Padre1, Padre2)
```
