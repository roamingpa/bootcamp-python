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
8. [Conjuntos (sets)](#8-conjuntos-sets)
9. [Tuplas](#9-tuplas)
10. [El bucle for](#10-el-bucle-for)
11. [El bucle while](#11-el-bucle-while)
12. [Comprehensions](#12-comprehensions)
13. [Módulo random](#13-módulo-random)
14. [Argumentos por consola (sys.argv)](#14-argumentos-por-consola-sysargv)
15. [Módulo math](#15-módulo-math)
16. [Errores comunes](#16-errores-comunes)

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

## 8. Conjuntos (sets)

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

## 9. Tuplas

Como una lista, pero **no se puede modificar** una vez creada.

```python
colores_semaforo = ("rojo", "amarillo", "verde")
coordenadas = (40.7, -74.0)

colores_semaforo[0]   # "rojo"
# colores_semaforo[0] = "azul"  ❌ Esto da error
```

> 💡 Usa tuplas cuando los datos no deben cambiar (días de la semana, coordenadas, etc.)

---

## 10. El bucle for

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

## 11. El bucle while

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

## 12. Comprehensions

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

## 13. Módulo random

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

## 14. Argumentos por consola (sys.argv)

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

## 15. Módulo math

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

## 16. Errores comunes

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
| Set `{}` | Guardar valores únicos sin orden |
| Tupla `()` | Guardar valores que no van a cambiar |
| Comprehension | Crear listas/diccionarios de forma corta |
| `input()` | Pedirle datos al usuario desde el teclado |
| `sys.argv` | Pasarle datos al programa desde la terminal |
| `random` | Generar valores al azar |
| `math` | Operaciones matemáticas avanzadas |

---

*Bootcamp Python — recuerda: programar es equivocarse, entender por qué, y volver a intentar. ¡Tú puedes, po!* 🚀
