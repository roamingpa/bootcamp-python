# 🐍 Ayuda Memoria — Python para Principiantes

> Una guía rápida con todo lo que vimos en el bootcamp. Sin complicaciones.

---

## 📋 Índice

1. [Tipos de datos básicos](#1-tipos-de-datos-básicos)
2. [Variables](#2-variables)
3. [Operadores matemáticos](#3-operadores-matemáticos)
4. [Print e input](#4-print-e-input)
5. [Condicionales (if / elif / else)](#5-condicionales-if--elif--else)
6. [Listas](#6-listas)
7. [Diccionarios](#7-diccionarios)
8. [Métodos de diccionarios](#8-métodos-de-diccionarios)
9. [Conjuntos (sets)](#9-conjuntos-sets)
10. [Tuplas](#10-tuplas)
11. [El bucle for](#11-el-bucle-for)
12. [El bucle while](#12-el-bucle-while)
13. [Comprehensions](#13-comprehensions)
14. [Módulo random](#14-módulo-random)
15. [Argumentos por consola (sys.argv)](#15-argumentos-por-consola-sysargv)
16. [Módulo math](#16-módulo-math)
17. [Funciones](#17-funciones)
18. [Parámetros avanzados en funciones](#18-parámetros-avanzados-en-funciones)
19. [Docstrings](#19-docstrings)
20. [Modularización](#20-modularización)
21. [Errores comunes](#21-errores-comunes)

---

## 1. Tipos de datos básicos

Python tiene distintos tipos de datos. Los más usados son:

| Tipo | ¿Qué es? | Ejemplo |
|------|----------|---------|
| `int` | Número entero | `42`, `-5`, `0` |
| `float` | Número con decimales | `3.14`, `-0.5` |
| `str` | Texto (cadena) | `"hola"`, `"Python"` |
| `bool` | Verdadero o falso | `True`, `False` |

```python
edad = 25          # int
precio = 99.9      # float
nombre = "Ana"     # str
activo = True      # bool
```

> 💡 **¿Cómo saber de qué tipo es algo?** Usa `type()`
> ```python
> print(type(42))      # <class 'int'>
> print(type("hola"))  # <class 'str'>
> ```

---

## 2. Variables

Una variable es una "cajita" donde guardas información.

```python
nombre = "Luis"
edad = 30
ciudad = "Santiago"
```

**Reglas:**
- No pueden empezar con números: ❌ `1nombre`, ✅ `nombre1`
- Sin espacios: ❌ `mi variable`, ✅ `mi_variable`
- Son sensibles a mayúsculas: `nombre` y `Nombre` son distintas

---

## 3. Operadores matemáticos

```python
10 + 3   # Suma        → 13
10 - 3   # Resta       → 7
10 * 3   # Multiplicación → 30
10 / 3   # División    → 3.333...
10 // 3  # División entera → 3
10 % 3   # Módulo (resto) → 1
10 ** 2  # Potencia    → 100
```

> 💡 El módulo `%` es útil para saber si un número es par o impar:
> ```python
> if numero % 2 == 0:
>     print("Es par")
> ```

---

## 4. Print e input

### print — mostrar algo en pantalla

```python
print("Hola mundo")
print("Tu nombre es", nombre)
print(f"Hola {nombre}, tienes {edad} años")  # f-string (recomendado)
```

### input — pedirle algo al usuario

```python
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))   # convertir a número entero
precio = float(input("¿Cuál es el precio? ")) # convertir a decimal
```

> ⚠️ `input()` **siempre devuelve texto**. Si necesitas un número, conviértelo con `int()` o `float()`.

---

## 5. Condicionales (if / elif / else)

Permiten tomar decisiones: "si pasa esto, haz aquello".

```python
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

### Operadores de comparación

```python
a == b   # ¿Son iguales?
a != b   # ¿Son distintos?
a > b    # ¿a es mayor que b?
a < b    # ¿a es menor que b?
a >= b   # ¿a es mayor o igual que b?
a <= b   # ¿a es menor o igual que b?
```

### Operadores lógicos

```python
if edad >= 18 and tiene_dni:    # Las dos condiciones deben ser verdaderas
    print("Puede votar")

if llueve or hace_frio:          # Al menos una debe ser verdadera
    print("Quédate en casa")

if not esta_cerrado:             # Niega la condición
    print("Puedes entrar")
```

---

## 6. Listas

Una lista guarda **varios valores en orden**, y se puede modificar.

```python
frutas = ["manzana", "pera", "banana"]
numeros = [10, 20, 30, 40]
mixto = [1, "hola", True]       # puede mezclar tipos
```

### Acceder a elementos

```python
frutas[0]    # "manzana"  (el primero es índice 0)
frutas[1]    # "pera"
frutas[-1]   # "banana"   (el último)
```

### Operaciones útiles

```python
frutas.append("uva")        # Agregar al final
frutas.remove("pera")       # Eliminar un elemento
len(frutas)                 # Cantidad de elementos → 3
"manzana" in frutas         # ¿Está en la lista? → True

frutas.sort()               # Ordenar alfabéticamente
numeros.sort(reverse=True)  # Ordenar de mayor a menor
```

### Recorrer una lista

```python
for fruta in frutas:
    print(fruta)
```

---

## 7. Diccionarios

Un diccionario guarda pares **clave: valor**. Como un contacto en el celular.

```python
persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Rosario"
}
```

### Acceder y modificar

```python
persona["nombre"]           # "Ana"
persona["edad"] = 29        # Modificar
persona["email"] = "a@b.com" # Agregar nueva clave

# Forma segura (no da error si la clave no existe)
persona.get("telefono", "No tiene")  # → "No tiene"
```

### Recorrer un diccionario

```python
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

for clave in persona:
    print(clave)              # Solo las claves

for valor in persona.values():
    print(valor)              # Solo los valores
```

### Diccionarios anidados

```python
estudiantes = {
    "Ana": {"edad": 20, "notas": [8, 7, 9]},
    "Luis": {"edad": 22, "notas": [6, 5, 7]}
}

print(estudiantes["Ana"]["notas"])   # [8, 7, 9]
```

---

## 8. Métodos de diccionarios

### Acceder a claves, valores y pares

```python
persona = {"nombre": "Ana", "edad": 28, "ciudad": "Rosario"}

persona.keys()    # dict_keys(['nombre', 'edad', 'ciudad'])
persona.values()  # dict_values(['Ana', 28, 'Rosario'])
persona.items()   # dict_items([('nombre', 'Ana'), ('edad', 28), ...])
```

### .get() — acceso seguro (sin error si la clave no existe)

```python
persona.get("nombre")              # "Ana"
persona.get("telefono")            # None  (no da error)
persona.get("telefono", "Sin tel") # "Sin tel"  (valor por defecto)
```

### .update() — agregar o modificar varias claves a la vez

```python
persona.update({"edad": 29, "email": "ana@mail.com"})
# persona ahora tiene edad=29 y email nuevo
```

### .pop() — eliminar una clave y obtener su valor

```python
telefono = persona.pop("telefono", None)  # elimina y devuelve el valor
# Si la clave no existe y no se pone valor por defecto, da KeyError
```

### .popitem() — eliminar el último par insertado

```python
ultimo = persona.popitem()  # devuelve (clave, valor) del último par
```

> 💡 **Cuándo usar cada método:**
> - `.get()` → cuando la clave puede no existir
> - `.update()` → cuando querés cambiar o agregar varios campos a la vez
> - `.pop()` → cuando necesitás eliminar Y usar el valor al mismo tiempo

---

## 9. Conjuntos (sets)

Un conjunto guarda valores **únicos** y **sin orden**. Ideal para eliminar duplicados.

```python
colores = {"rojo", "verde", "azul", "rojo"}  # "rojo" queda una sola vez
print(colores)   # {"rojo", "verde", "azul"}
```

### Operaciones útiles

```python
inscriptos = {"Ana", "Luis", "Maria", "Pedro"}
rindieron  = {"Ana", "Pedro"}

inscriptos - rindieron      # Quiénes NO rindieron → {"Luis", "Maria"}
inscriptos & rindieron      # Quiénes están en ambos → {"Ana", "Pedro"}
inscriptos | rindieron      # Todos juntos (sin repetidos)

"Ana" in inscriptos         # ¿Está en el conjunto? → True
```

---

## 10. Tuplas

Como una lista, pero **no se puede modificar** una vez creada.

```python
colores_semaforo = ("rojo", "amarillo", "verde")
coordenadas = (40.7, -74.0)

colores_semaforo[0]   # "rojo"
# colores_semaforo[0] = "azul"  ❌ Esto da error
```

> 💡 Usa tuplas cuando los datos no deben cambiar (días de la semana, coordenadas, etc.)

---

## 11. El bucle for

Repite algo para cada elemento de una secuencia.

```python
# Recorrer una lista
frutas = ["manzana", "pera", "banana"]
for fruta in frutas:
    print(fruta)

# Repetir N veces con range()
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8  (de 2 en 2)
    print(i)
```

### break y continue

```python
# break: salir del bucle antes de terminar
for i in range(10):
    if i == 5:
        break       # Para en 5, no llega a 10
    print(i)

# continue: saltear una vuelta
for i in range(5):
    if i == 2:
        continue    # Salta el 2, sigue con 3
    print(i)
```

---

## 12. El bucle while

Repite mientras una condición sea verdadera.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1    # ¡Importante! Si no actualizas, es un bucle infinito
```

### Patrón clásico: seguir hasta que el usuario diga "no"

```python
gastos = []
while True:
    gasto = int(input("Ingresa un gasto: "))
    gastos.append(gasto)
    
    continuar = input("¿Quieres agregar otro? (si/no): ")
    if continuar.lower() == "no":
        break

print(f"Total: {sum(gastos)}")
```

> ⚠️ Siempre asegúrate de que el `while` en algún momento se detenga. Si no, el programa corre pa' siempre.

---

## 13. Comprehensions

Una forma **corta y elegante** de crear listas o diccionarios.

### List comprehension

```python
# Forma larga:
cuadrados = []
for i in range(1, 6):
    cuadrados.append(i ** 2)

# Forma corta (comprehension):
cuadrados = [i ** 2 for i in range(1, 6)]
# → [1, 4, 9, 16, 25]
```

### Con condición (filtro)

```python
notas = [4, 7, 3, 9, 5, 8]

aprobados = [nota for nota in notas if nota >= 6]
# → [7, 9, 8]
```

### Dictionary comprehension

```python
precios = {"leche": 100, "pan": 50, "jugo": 200}

caros = {producto: precio for producto, precio in precios.items() if precio > 80}
# → {"leche": 100, "jugo": 200}
```

---

## 14. Módulo random

Sirve para generar cosas al azar.

```python
import random

# Número entero aleatorio entre 1 y 10
numero = random.randint(1, 10)

# Elegir un elemento al azar de una lista
opciones = ["piedra", "papel", "tijera"]
eleccion = random.choice(opciones)

# Mezclar una lista
cartas = [1, 2, 3, 4, 5]
random.shuffle(cartas)

# Número decimal aleatorio entre 0 y 1
decimal = random.random()
```

---

## 15. Argumentos por consola (sys.argv)

Permiten pasarle datos al programa cuando lo ejecutas desde la terminal.

```python
import sys

# Si ejecutas: python programa.py Juan 25
nombre = sys.argv[1]   # "Juan"
edad = sys.argv[2]     # "25" (siempre es texto, convertir si es necesario)

print(f"Hola {nombre}, tienes {edad} años")
```

```bash
# En la terminal:
python programa.py Juan 25
# Salida: Hola Juan, tienes 25 años
```

> 💡 `sys.argv[0]` siempre es el nombre del archivo. Los argumentos empiezan en `sys.argv[1]`.

---

## 16. Módulo math

Para operaciones matemáticas más avanzadas.

```python
import math

math.sqrt(16)       # Raíz cuadrada → 4.0
math.pow(2, 10)     # Potencia → 1024.0
math.log(100, 10)   # Logaritmo base 10 → 2.0
math.pi             # El número π → 3.14159...
math.ceil(4.2)      # Redondear hacia arriba → 5
math.floor(4.9)     # Redondear hacia abajo → 4
```

---

## 17. Funciones

Una función es un bloque de código reutilizable que tiene un nombre, puede recibir datos (**parámetros**) y puede devolver un resultado (**return**).

```python
# Definir una función
def saludar(nombre):
    return f"Hola, {nombre}!"

# Llamar (invocar) la función
print(saludar("Ana"))   # Hola, Ana!
print(saludar("Luis"))  # Hola, Luis!
```

### Función con múltiples parámetros y return

```python
def calcular_promedio(lista):
    return sum(lista) / len(lista)

notas = [7, 8, 9, 6]
print(calcular_promedio(notas))   # 7.5
```

### Función que retorna múltiples valores (tupla)

```python
def estadisticas(lista):
    return min(lista), max(lista), sum(lista) / len(lista)

minimo, maximo, promedio = estadisticas([3, 7, 1, 9])
print(minimo, maximo, promedio)   # 1 9 5.0
```

> 💡 `def` define la función, `return` devuelve el resultado. Sin `return` la función devuelve `None`.

---

## 18. Parámetros avanzados en funciones

### Parámetros por defecto (opcionales)

```python
def presentar(nombre, rol="estudiante"):
    print(f"Soy {nombre} y soy {rol}.")

presentar("Ana")               # Soy Ana y soy estudiante.
presentar("Luis", "instructor") # Soy Luis y soy instructor.
```

### *args — cantidad variable de argumentos

```python
def sumar(*args):
    return sum(args)

print(sumar(1, 2))         # 3
print(sumar(1, 2, 3, 4))   # 10
print(sumar())             # 0
```

### **kwargs — argumentos nombrados variables

```python
def crear_perfil(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

crear_perfil(nombre="Ana", edad=28, ciudad="Rosario")
# nombre: Ana
# edad: 28
# ciudad: Rosario
```

### Función como argumento

```python
def aplicar(lista, funcion):
    return funcion(lista)

numeros = [3, 1, 7, 2]
print(aplicar(numeros, sum))   # 13
print(aplicar(numeros, max))   # 7
print(aplicar(numeros, len))   # 4
```

> 💡 Al pasar una función como argumento, se escribe **sin paréntesis**: `sum` no `sum()`.

---

## 19. Docstrings

Un docstring es la documentación que se escribe dentro de una función para explicar qué hace, qué recibe y qué devuelve.

```python
def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio final luego de aplicar un descuento.

    Args:
        precio (float): Precio original del producto.
        porcentaje (float): Porcentaje de descuento a aplicar.

    Returns:
        float: Precio con el descuento aplicado.
    """
    return precio * (1 - porcentaje / 100)
```

Para ver el docstring de una función:

```python
help(calcular_descuento)
# o en algunos editores, hover sobre el nombre de la función
```

> 💡 Las comillas triples `"""..."""` pueden ser simples o dobles. El formato más usado es **Google style** (Args / Returns).

---

## 20. Modularización

Dividir un proyecto en varios archivos `.py` (módulos) para mantener el código ordenado y reutilizable.

### Crear un módulo

```python
# archivo: operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
```

### Las 3 formas de importar

```python
# Forma 1: import módulo  → llamar con módulo.funcion()
import operaciones
operaciones.sumar(3, 5)

# Forma 2: import módulo as alias  → llamar con alias.funcion()
import operaciones as op
op.sumar(3, 5)

# Forma 3: from módulo import función  → llamar directo
from operaciones import sumar
sumar(3, 5)
```

### Estructura recomendada de un proyecto

```
mi_proyecto/
    main.py          ← script principal, llama a los módulos
    operaciones.py   ← funciones matemáticas
    datos.py         ← funciones para manejar datos
```

```python
# main.py
from operaciones import sumar, restar

a = float(input("Número A: "))
b = float(input("Número B: "))
print("Suma:", sumar(a, b))
print("Resta:", restar(a, b))
```

> 💡 El archivo `main.py` es la **entrada** del programa. Los módulos son herramientas que `main.py` usa.

---

## 21. Errores comunes

### NameError — variable no definida
```python
print(nombre)    # ❌ Error si "nombre" no fue definida antes
nombre = "Ana"
print(nombre)    # ✅
```

### TypeError — tipo de dato incorrecto
```python
edad = input("Edad: ")
print(edad + 1)              # ❌ No puedes sumar texto y número
print(int(edad) + 1)         # ✅
```

### IndexError — índice fuera de rango
```python
lista = ["a", "b", "c"]
lista[5]    # ❌ Solo existen los índices 0, 1, 2
lista[2]    # ✅
```

### ZeroDivisionError — dividir por cero
```python
10 / 0      # ❌ División por cero
if divisor != 0:
    10 / divisor    # ✅
```

### Signo = vs ==
```python
x = 5       # Asignación: le doy el valor 5 a x
x == 5      # Comparación: ¿x es igual a 5?

if x = 5:   # ❌ Error de sintaxis
if x == 5:  # ✅
```

---

## 🔁 Resumen rápido

| Concepto | Cuándo usarlo |
|----------|---------------|
| `if/elif/else` | Tomar decisiones según una condición |
| `for` | Repetir algo para cada elemento de una lista o un rango |
| `while` | Repetir mientras algo sea verdadero |
| `break` | Salir de un bucle antes de que termine |
| `continue` | Saltear la vuelta actual del bucle |
| Lista `[]` | Guardar varios valores en orden, se puede modificar |
| Diccionario `{}` | Guardar pares clave-valor |
| `.get()` | Acceder a clave de dict sin riesgo de error |
| `.update()` | Agregar o modificar varias claves a la vez |
| `.pop()` | Eliminar clave de dict y obtener su valor |
| Set `{}` | Guardar valores únicos sin orden |
| Tupla `()` | Guardar valores que no van a cambiar |
| Comprehension | Crear listas/diccionarios de forma corta |
| `input()` | Pedirle datos al usuario desde el teclado |
| `sys.argv` | Pasarle datos al programa desde la terminal |
| `random` | Generar valores al azar |
| `math` | Operaciones matemáticas avanzadas |
| `def` / `return` | Definir una función reutilizable |
| Parámetro por defecto | Parámetro opcional con valor preestablecido |
| `*args` | Función que acepta cualquier cantidad de argumentos |
| `**kwargs` | Función que acepta argumentos nombrados variables |
| Función como argumento | Pasar `sum`, `len`, etc. como parámetro |
| Docstring `"""..."""` | Documentar qué hace una función |
| `import módulo` | Usar código de otro archivo `.py` |

---

*Bootcamp Python — recuerda: programar es equivocarse, entender por qué, y volver a intentar. ¡Tú puedes, po!* 🚀
