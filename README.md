# 🐍 Python Bootcamp by Luis Correa

Repositorio con ejercicios, apuntes y guías técnicas del bootcamp de Python.

## Estructura

```
clases/        → Ejercicios por clase (clase15 – clase36)
blog/          → Sitio web estático (MkDocs)
  docs/        → Fuente: guías .md + posts del blog
  site/        → Output generado (no commitear)
  mkdocs.yml   → Configuración del sitio
contenido/     → Material del curso (slides, apuntes por semana)
excalidraw/    → Diagramas
```

## Sitio web

Las guías y el cheatsheet completo están en el sitio estático generado con MkDocs + Material.

```bash
# Preview local
cd blog && mkdocs serve

# Generar sitio estático en blog/site/
cd blog && mkdocs build
```
