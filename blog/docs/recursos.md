# :material-book-open-variant: Recursos para el Docente

Herramientas, plugins y configuraciones útiles para preparar y publicar materiales de clase con MkDocs + Material.

---

## Plugins instalados en este sitio

| Plugin | Comando de instalación | Para qué sirve |
|--------|----------------------|----------------|
| **mkdocs-material** | `pip install mkdocs-material` | Tema base con todos los componentes de UI |
| **mkdocs-print-site** | `pip install mkdocs-print-site-plugin` | Genera `/print_page` con todo el sitio unificado para imprimir o exportar a PDF conservando los estilos |
| **mkdocs-glightbox** | `pip install mkdocs-glightbox` | Zoom en imágenes al hacer click (lightbox) |

---

## Plugins recomendados para agregar

### Para el aula

| Plugin | Instalación | Descripción |
|--------|------------|-------------|
| **mkdocs-git-revision-date-localized** | `pip install mkdocs-git-revision-date-localized` | Muestra la fecha de última modificación de cada página (útil para que los estudiantes sepan si hay contenido nuevo) |
| **mkdocs-minify-plugin** | `pip install mkdocs-minify-plugin` | Reduce el tamaño del HTML/CSS/JS generado (~30% más liviano, carga más rápido) |
| **mkdocs-awesome-pages-plugin** | `pip install mkdocs-awesome-pages-plugin` | Ordena la navegación con un archivo `.pages` sin tener que listar todo en `mkdocs.yml` |

### Para contenido interactivo

| Plugin | Instalación | Descripción |
|--------|------------|-------------|
| **mkdocs-jupyter** | `pip install mkdocs-jupyter` | Incluye notebooks de Jupyter directamente como páginas del sitio |
| **mkdocs-include-markdown-plugin** | `pip install mkdocs-include-markdown-plugin` | Incluye fragmentos de otros archivos `.md` — útil para reutilizar bloques de código o enunciados |
| **mkdocs-macros-plugin** | `pip install mkdocs-macros-plugin` | Variables y templates en los `.md` — sirve para personalizar el nombre del curso, fechas, etc. |

### Para mejor presentación

| Plugin | Instalación | Descripción |
|--------|------------|-------------|
| **mkdocs-redirects** | `pip install mkdocs-redirects` | Redirige URLs antiguas a nuevas cuando reorganizás el contenido |
| **mkdocs-tags-plugin** | (incluido en Material Insiders) | Etiquetas por tema en cada página — filtrá por `#python`, `#poo`, etc. |

---

## Extensiones de Markdown más útiles

Estas ya están habilitadas en este sitio:

### Bloques de advertencia (Admonitions)

```markdown
!!! tip "Tip para el docente"
    Acá va una nota destacada.

!!! warning "Atención"
    Esto puede generar confusión.

!!! danger "Error común"
    Descripción del error.

??? example "Ejemplo expandible (click para ver)"
    Contenido oculto por defecto.
```

Se ven así:

!!! tip "Tip para el docente"
    Acá va una nota destacada.

!!! warning "Atención"
    Esto puede generar confusión.

??? example "Ejemplo expandible (click para ver)"
    Código o explicación que no quieras mostrar de entrada.

---

### Tabs para comparar código

````markdown
=== "Python"
    ```python
    print("Hola mundo")
    ```

=== "JavaScript"
    ```javascript
    console.log("Hola mundo")
    ```
````

---

### Teclas de teclado

```markdown
Presioná ++ctrl+s++ para guardar.
Usá ++cmd+shift+p++ para abrir la paleta de comandos.
```

Se ve: Presioná ++ctrl+s++ para guardar.

---

### Grid cards (tarjetas)

```markdown
<div class="grid cards" markdown>

-   :material-language-python: **Python**

    ---

    Descripción del módulo.

    [Ver módulo](fundamentos.md)

</div>
```

---

## Comandos esenciales de MkDocs

```bash
# Preview local con recarga automática
cd blog
mkdocs serve

# Generar el sitio estático en blog/site/
mkdocs build

# Publicar en GitHub Pages manualmente
mkdocs gh-deploy

# Ver ayuda
mkdocs --help
```

---

## Estructura del proyecto

```
bootcamp-python/
├── blog/
│   ├── docs/          ← archivos fuente (.md, imágenes, CSS)
│   │   ├── stylesheets/extra.css
│   │   ├── blog/posts/    ← posts del blog
│   │   └── *.md           ← páginas del sitio
│   ├── mkdocs.yml     ← configuración del sitio
│   └── site/          ← output generado (no commitear)
├── clases/            ← ejercicios de cada clase
└── .github/workflows/deploy.yml  ← deploy automático a GitHub Pages
```

---

## Deploy automático

Cada `git push` a `main` dispara el workflow de GitHub Actions que publica el sitio en:

```
https://roamingpa.github.io/bootcamp-python/
```

El workflow está en [.github/workflows/deploy.yml](https://github.com/roamingpa/bootcamp-python/blob/main/.github/workflows/deploy.yml).
