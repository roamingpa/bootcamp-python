# 🐍 Ayuda Memoria — Funciones en Python

> Guía rápida para crear y usar funciones en Python. Sin complicaciones.

---

## 📋 Índice

1. [¿Qué es una función?](#1-qué-es-una-función)
2. [Definir una función](#2-definir-una-función)
3. [Parámetros y argumentos](#3-parámetros-y-argumentos)
4. [Retornar valores](#4-retornar-valores)
5. [Parámetros por defecto](#5-parámetros-por-defecto)
6. [Argumentos con nombre (keyword arguments)](#6-argumentos-con-nombre-keyword-arguments)
7. [*args y **kwargs](#7-args-y-kwargs)
8. [Funciones lambda](#8-funciones-lambda)
9. [Scope — variables locales y globales](#9-scope--variables-locales-y-globales)
10. [Errores comunes](#10-errores-comunes)
11. [Resumen rápido](#11-resumen-rápido)

---

## 1. ¿Qué es una función?

Una función es un **bloque de código reutilizable** que hace una tarea específica. La defines una vez y la puedes llamar cuantas veces quieras.

```python
# Sin función (código repetido 😩)
print("Hola, Juan")
print("Hola, Pedro")
print("Hola, María")

# Con función (limpio y reutilizable 😎)
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Juan")
saludar("Pedro")
saludar("María")
```

---

## 2. Definir una función

Se usa la palabra clave `def`, seguida del nombre y paréntesis.

```python
def nombre_de_la_funcion():
    # código que ejecuta la función
    print("Hola mundo")

# Llamar la función
nombre_de_la_funcion()
```

> 💡 Por convención los nombres de funciones van en `snake_case` (minúsculas con guiones bajos).

---

## 3. Parámetros y argumentos

- **Parámetro**: la variable que defines en la función
- **Argumento**: el valor que le pasas al llamarla

```python
# "nombre" y "edad" son parámetros
def presentar(nombre, edad):
    print(f"Soy {nombre} y tengo {edad} años")

# "Ana" y 25 son argumentos
presentar("Ana", 25)
# Output: Soy Ana y tengo 25 años
```

---

## 4. Retornar valores

Con `return` la función **devuelve un resultado** que puedes guardar o usar.

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print(resultado)
# Output: 7

# También puedes usar el resultado directo
print(sumar(10, 5))
# Output: 15
```

> ⚠️ Todo lo que esté después del `return` dentro de la función **no se ejecuta**.

```python
def ejemplo():
    return "esto sí se ejecuta"
    print("esto nunca se ejecuta")   # código muerto
```

### Retornar múltiples valores

```python
def min_max(lista):
    return min(lista), max(lista)

minimo, maximo = min_max([3, 1, 7, 2])
print(minimo)  # 1
print(maximo)  # 7
```

---

## 5. Parámetros por defecto

Puedes darle un valor por defecto a un parámetro. Si no se pasa el argumento, usa el valor por defecto.

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Carlos")            # Output: Hola, Carlos!
saludar("Carlos", "Buenas")  # Output: Buenas, Carlos!
```

> ⚠️ Los parámetros con valor por defecto siempre van **al final**.

```python
# ❌ Esto da error
def mal(saludo="Hola", nombre):
    pass

# ✅ Esto está bien
def bien(nombre, saludo="Hola"):
    pass
```

---

## 6. Argumentos con nombre (keyword arguments)

Puedes pasar argumentos usando el nombre del parámetro, así no importa el orden.

```python
def crear_usuario(nombre, rol, activo):
    print(f"{nombre} | {rol} | Activo: {activo}")

# Sin nombre — el orden importa
crear_usuario("Luis", "admin", True)

# Con nombre — el orden no importa
crear_usuario(rol="admin", activo=True, nombre="Luis")
# Output: Luis | admin | Activo: True
```

---

## 7. *args y **kwargs

### `*args` — cantidad variable de argumentos posicionales

```python
def sumar_todo(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(sumar_todo(1, 2, 3))        # 6
print(sumar_todo(10, 20, 30, 40)) # 100
```

> `*args` llega como una **tupla** dentro de la función.

### `**kwargs` — cantidad variable de argumentos con nombre

```python
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, ciudad="Santiago")
# Output:
# nombre: Ana
# edad: 30
# ciudad: Santiago
```

> `**kwargs` llega como un **diccionario** dentro de la función.

---

## 8. Funciones lambda

Son funciones **pequeñas y anónimas** que se definen en una sola línea.

```python
# Función normal
def doblar(x):
    return x * 2

# Lambda equivalente
doblar = lambda x: x * 2

print(doblar(5))  # 10
```

Se usan mucho con `map()`, `filter()` y `sorted()`:

```python
numeros = [3, 1, 4, 1, 5, 9, 2]

# Ordenar de mayor a menor
ordenados = sorted(numeros, key=lambda x: -x)
print(ordenados)  # [9, 5, 4, 3, 2, 1, 1]

# Filtrar solo los pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [4, 2]

# Multiplicar cada uno por 3
triplicados = list(map(lambda x: x * 3, numeros))
print(triplicados)  # [9, 3, 12, 3, 15, 27, 6]
```

---

## 9. Scope — variables locales y globales

- **Local**: variable creada dentro de una función. Solo existe ahí.
- **Global**: variable creada fuera de una función. Existe en todo el script.

```python
mensaje = "soy global"

def mostrar():
    mensaje_local = "soy local"
    print(mensaje)        # puede leer la global
    print(mensaje_local)  # puede leer la local

mostrar()
print(mensaje)        # ✅ funciona
# print(mensaje_local)  # ❌ error: no existe fuera
```

### Modificar una variable global desde una función

```python
contador = 0

def incrementar():
    global contador    # le avisas a Python que vas a modificar la global
    contador += 1

incrementar()
incrementar()
print(contador)  # 2
```

> 💡 En general, modificar variables globales dentro de funciones no es buena práctica. Mejor retornar el valor.

---

## 10. Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `TypeError: missing argument` | Llamaste la función sin todos los argumentos requeridos | Revisa cuántos parámetros tiene la función |
| `TypeError: takes X positional arguments but Y were given` | Pasaste más argumentos de los que acepta | Cuenta los parámetros |
| `NameError: name 'x' is not defined` | Intentaste usar una variable local fuera de su scope | Retorna el valor con `return` |
| Función siempre retorna `None` | Te olvidaste el `return` | Agrega `return resultado` |
| Parámetro por defecto mutable (lista, dict) | El valor se comparte entre llamadas | Usa `None` como default y crea el objeto adentro |

```python
# ❌ Bug clásico con default mutable
def agregar(item, lista=[]):
    lista.append(item)
    return lista

print(agregar("a"))  # ['a']
print(agregar("b"))  # ['a', 'b']  ← se acumuló!

# ✅ La forma correcta
def agregar(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

---

## 11. Resumen rápido

```python
# Función simple
def saludar():
    print("Hola!")

# Con parámetros
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Con retorno
def sumar(a, b):
    return a + b

# Con valor por defecto
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

# Con *args (varios argumentos posicionales)
def sumar(*nums):
    return sum(nums)

# Con **kwargs (varios argumentos con nombre)
def info(**datos):
    for k, v in datos.items():
        print(f"{k}: {v}")

# Lambda (función en una línea)
doblar = lambda x: x * 2

# Llamar con keyword arguments
sumar(a=3, b=4)
```

| Concepto | Sintaxis |
|---------|---------|
| Definir | `def nombre(params):` |
| Retornar | `return valor` |
| Default | `def f(x=10):` |
| Keyword arg | `f(nombre="Ana")` |
| Args variables | `def f(*args):` |
| Kwargs variables | `def f(**kwargs):` |
| Lambda | `lambda x: x * 2` |
| Global | `global variable` |
