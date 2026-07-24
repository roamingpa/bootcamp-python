# 🌿 Ayuda Memoria — Git para Principiantes

> Guía rápida de los comandos de Git que más vas a usar. Sin complicaciones.

---

## 📋 Índice

1. [¿Qué es Git?](#1-qué-es-git)
2. [Configuración inicial](#2-configuración-inicial)
3. [Crear o clonar un repositorio](#3-crear-o-clonar-un-repositorio)
4. [El ciclo básico de trabajo](#4-el-ciclo-básico-de-trabajo)
5. [Ver el estado y el historial](#5-ver-el-estado-y-el-historial)
6. [Ramas (branches)](#6-ramas-branches)
7. [Conectar con GitHub](#7-conectar-con-github)
8. [Deshacer cosas](#8-deshacer-cosas)
9. [Errores comunes](#9-errores-comunes)
10. [Resumen rápido](#10-resumen-rápido)

---

## 1. ¿Qué es Git?

Git es una herramienta que **guarda el historial de cambios** de tu código. Como tener una máquina del tiempo para tus archivos.

- **Git** = la herramienta que corre en tu computador
- **GitHub** = el sitio web donde subes tu código para guardarlo en la nube y compartirlo

---

## 2. Configuración inicial

Solo necesitas hacer esto una vez cuando instalas Git.

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

> 💡 Para verificar que quedó bien:
> ```bash
> git config --global user.name
> git config --global user.email
> ```

---

## 3. Crear o clonar un repositorio

### Crear uno nuevo desde cero

```bash
# Primero entra a la carpeta de tu proyecto
cd mi-proyecto

# Inicializa Git ahí
git init
```

### Clonar uno que ya existe en GitHub

```bash
git clone https://github.com/usuario/repositorio.git
```

Esto descarga todo el proyecto a tu computador.

---

## 4. El ciclo básico de trabajo

Este es el flujo que vas a repetir todo el tiempo:

```
1. Haces cambios en tus archivos
2. git add     → marcas qué cambios quieres guardar
3. git commit  → guardas esos cambios con un mensaje
4. git push    → subes los cambios a GitHub
```

### git add — marcar archivos para guardar

```bash
git add archivo.py              # Agrega un archivo específico
git add .                       # Agrega TODOS los archivos modificados
```

### git commit — guardar los cambios

```bash
git commit -m "Agrega función de login"
```

> 💡 El mensaje del commit debe describir **qué hiciste**, no cómo. Escríbelo como si completaras la frase "Este commit..."

**Buenos mensajes:**
- `"Agrega validación de formulario"`
- `"Corrige bug en el cálculo de descuento"`
- `"Actualiza README con instrucciones de instalación"`

**Malos mensajes:**
- `"cambios"` ❌
- `"asdfgh"` ❌
- `"arreglé cosas"` ❌

### git push — subir a GitHub

```bash
git push origin main
```

---

## 5. Ver el estado y el historial

### git status — ¿qué está pasando?

```bash
git status
```

Te muestra qué archivos cambiaste, cuáles están listos para commit y cuáles no.

```
Changes to be committed:    → listos para commit (ya hiciste git add)
Changes not staged:         → modificados pero sin git add todavía
Untracked files:            → archivos nuevos que Git no conoce aún
```

### git log — historial de commits

```bash
git log                     # Historial completo
git log --oneline           # Versión resumida (más útil)
```

```
a3f1c2d Agrega validación de formulario
b8e9f01 Corrige bug en login
c12d3e4 Primer commit
```

---

## 6. Ramas (branches)

Una rama es como una **copia paralela** de tu proyecto. Útil para trabajar en algo nuevo sin romper lo que ya funciona.

```bash
git branch                      # Ver en qué rama estás
git branch nombre-rama          # Crear una rama nueva
git checkout nombre-rama        # Cambiar a esa rama
git checkout -b nombre-rama     # Crear Y cambiar en un solo comando
```

### Fusionar una rama con main

```bash
git checkout main               # Primero vuelves a main
git merge nombre-rama           # Luego fusionas
```

### Eliminar una rama (cuando ya no la necesitas)

```bash
git branch -d nombre-rama
```

> 💡 Flujo típico: creas una rama para cada feature o fix → trabajas ahí → haces merge a main cuando está listo.

---

## 7. Conectar con GitHub

### Ver a qué remoto está conectado tu repo

```bash
git remote -v
```

### Agregar un remoto (si creaste el repo local primero)

```bash
git remote add origin https://github.com/usuario/repositorio.git
```

### Bajar cambios que otros subieron

```bash
git pull origin main
```

> ⚠️ Antes de empezar a trabajar cada día, haz `git pull` para tener la versión más reciente.

### Subir una rama nueva a GitHub por primera vez

```bash
git push -u origin nombre-rama
```

---

## 8. Deshacer cosas

### Sacar un archivo del staging (deshace el git add)

```bash
git restore --staged archivo.py
```

### Descartar cambios en un archivo (vuelve al último commit)

```bash
git restore archivo.py
```

> ⚠️ Esto **borra** los cambios que no guardaste. No se puede recuperar.

### Ver qué cambió en un archivo

```bash
git diff archivo.py
```

---

## 9. Errores comunes

### "nothing to commit"
No hiciste cambios, o olvidaste el `git add`.

```bash
git status    # Revisa qué está pasando
git add .     # Si tienes cambios sin agregar
```

### "rejected — non-fast-forward"
Alguien subió cambios antes que tú. Primero baja los cambios:

```bash
git pull origin main
# Resuelve conflictos si los hay, luego:
git push origin main
```

### "detached HEAD"
Estás en un commit antiguo sin estar en ninguna rama. Vuelve a main:

```bash
git checkout main
```

### Commiteé en la rama equivocada
Si el commit es reciente y no lo subiste aún, puedes moverlo:

```bash
git checkout la-rama-correcta
git cherry-pick <id-del-commit>   # copia el commit aquí
git checkout main
git reset --hard HEAD~1           # borra el commit de main
```

---

## 10. Resumen rápido

| Comando | ¿Qué hace? |
|---------|-----------|
| `git init` | Crea un repositorio nuevo |
| `git clone <url>` | Descarga un repositorio de GitHub |
| `git status` | Muestra el estado actual |
| `git add .` | Marca todos los cambios para guardar |
| `git commit -m "msg"` | Guarda los cambios con un mensaje |
| `git push origin main` | Sube los cambios a GitHub |
| `git pull origin main` | Baja los cambios desde GitHub |
| `git log --oneline` | Muestra el historial resumido |
| `git branch nombre` | Crea una rama nueva |
| `git checkout nombre` | Cambia de rama |
| `git merge nombre` | Fusiona una rama con la actual |
| `git diff` | Muestra qué cambió |
| `git restore archivo` | Deshace cambios en un archivo |

---

### El flujo del día a día

```bash
git pull origin main          # 1. Baja lo último
# ... haces tus cambios ...
git add .                     # 2. Marcas los cambios
git commit -m "descripción"   # 3. Guardas
git push origin main          # 4. Subes
```

---

*Git al principio puede parecer complicado, pero con práctica se vuelve automático. ¡Tú puedes, po!* 🚀
