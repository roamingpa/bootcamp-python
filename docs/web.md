# 🌐 Ayuda Memoria — HTML, CSS, JavaScript, jQuery y Bootstrap

> Guía rápida para construir páginas web. Sin complicaciones.

---

## 📋 Índice

1. [¿Cómo se relacionan HTML, CSS y JS?](#1-cómo-se-relacionan-html-css-y-js)
2. [HTML — estructura](#2-html--estructura)
3. [CSS — estilos](#3-css--estilos)
4. [JavaScript — comportamiento](#4-javascript--comportamiento)
5. [jQuery — JS más fácil](#5-jquery--js-más-fácil)
6. [Bootstrap — diseño sin esfuerzo](#6-bootstrap--diseño-sin-esfuerzo)
7. [Cómo conectar todo](#7-cómo-conectar-todo)
8. [Errores comunes](#8-errores-comunes)
9. [Resumen rápido](#9-resumen-rápido)

---

## 1. ¿Cómo se relacionan HTML, CSS y JS?

Piensa en una casa:

| Tecnología | Rol | Ejemplo |
|-----------|-----|---------|
| **HTML** | La estructura (paredes, puertas) | "Aquí hay un botón" |
| **CSS** | La decoración (pintura, muebles) | "Ese botón es azul y grande" |
| **JavaScript** | La electricidad (lo que hace cosas) | "Al hacer clic, muestra un mensaje" |
| **jQuery** | JS con atajos (electricidad más fácil) | Misma idea, menos código |
| **Bootstrap** | CSS prefabricado (muebles de IKEA) | Diseño bonito sin escribir CSS |

---

## 2. HTML — estructura

### Estructura base de una página

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi página</title>
  </head>
  <body>
    <!-- Aquí va el contenido visible -->
    <h1>Hola mundo</h1>
  </body>
</html>
```

### Etiquetas más usadas

```html
<!-- Títulos (h1 es el más grande, h6 el más pequeño) -->
<h1>Título principal</h1>
<h2>Subtítulo</h2>
<h3>Sub-subtítulo</h3>

<!-- Texto -->
<p>Esto es un párrafo.</p>
<strong>Texto en negrita</strong>
<em>Texto en cursiva</em>

<!-- Enlace -->
<a href="https://google.com">Ir a Google</a>
<a href="otra-pagina.html">Ir a otra página</a>

<!-- Imagen -->
<img src="foto.jpg" alt="Descripción de la imagen">

<!-- Listas -->
<ul>                          <!-- Lista con puntos -->
  <li>Manzana</li>
  <li>Pera</li>
</ul>

<ol>                          <!-- Lista numerada -->
  <li>Primero</li>
  <li>Segundo</li>
</ol>

<!-- Divisiones (contenedores) -->
<div>Bloque genérico</div>
<span>Texto en línea</span>

<!-- Botón -->
<button>Haz clic aquí</button>

<!-- Formulario -->
<input type="text" placeholder="Escribe algo">
<input type="number" placeholder="Tu edad">
<input type="email" placeholder="Tu email">
```

### Atributos importantes

```html
<!-- id: identificador único (para CSS y JS) -->
<div id="mi-caja">Contenido</div>

<!-- class: puede repetirse (para dar estilos a varios) -->
<p class="texto-rojo">Párrafo rojo</p>
<p class="texto-rojo">Otro párrafo rojo</p>
```

> 💡 Usa `id` cuando el elemento es único. Usa `class` cuando varios elementos comparten el mismo estilo.

---

## 3. CSS — estilos

### Cómo escribir CSS

```css
/* selector { propiedad: valor; } */

h1 {
  color: blue;
  font-size: 32px;
}

p {
  color: gray;
  font-family: Arial, sans-serif;
}
```

### Selectores básicos

```css
h1 { }           /* Por etiqueta — afecta a TODOS los h1 */
#mi-caja { }     /* Por id — solo ese elemento */
.texto-rojo { }  /* Por clase — todos los que tengan esa clase */
```

### Propiedades más usadas

```css
/* Texto */
color: red;                   /* Color del texto */
font-size: 16px;              /* Tamaño de fuente */
font-weight: bold;            /* Negrita */
text-align: center;           /* Alineación */

/* Fondo */
background-color: yellow;
background-image: url("foto.jpg");

/* Caja (todo elemento HTML es una caja) */
width: 200px;                 /* Ancho */
height: 100px;                /* Alto */
padding: 10px;                /* Espacio interior */
margin: 20px;                 /* Espacio exterior */
border: 1px solid black;      /* Borde */
border-radius: 8px;           /* Bordes redondeados */

/* Posición y display */
display: flex;                /* Pone los hijos en fila */
justify-content: center;      /* Centra horizontalmente */
align-items: center;          /* Centra verticalmente */
```

### Colores en CSS

```css
color: red;                   /* Nombre */
color: #ff0000;               /* Hexadecimal */
color: rgb(255, 0, 0);        /* RGB */
color: rgba(255, 0, 0, 0.5);  /* RGB con transparencia */
```

### Ejemplo completo

```css
.tarjeta {
  width: 300px;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 20px;
  margin: 10px;
  text-align: center;
}
```

---

## 4. JavaScript — comportamiento

### Lo básico

```javascript
// Variables
let nombre = "Ana";           // let: puede cambiar
const PI = 3.14;              // const: no puede cambiar

// Mostrar en consola (para depurar)
console.log("Hola", nombre);

// Mostrar alerta en pantalla
alert("¡Bienvenido!");

// Pedirle algo al usuario
let respuesta = prompt("¿Cómo te llamas?");
```

### Seleccionar elementos HTML

```javascript
// Por id
let caja = document.getElementById("mi-caja");

// Por clase (devuelve varios)
let botones = document.getElementsByClassName("btn");

// Selector moderno (como CSS)
let titulo = document.querySelector("h1");
let items = document.querySelectorAll(".item");  // todos los que coincidan
```

### Modificar elementos

```javascript
let titulo = document.querySelector("h1");

titulo.textContent = "Nuevo título";       // Cambiar el texto
titulo.style.color = "red";               // Cambiar estilo
titulo.style.fontSize = "40px";
titulo.classList.add("activo");           // Agregar clase
titulo.classList.remove("activo");        // Quitar clase
titulo.classList.toggle("activo");        // Agregar/quitar alternando
```

### Eventos — reaccionar a acciones del usuario

```javascript
let boton = document.querySelector("#mi-boton");

boton.addEventListener("click", function() {
  alert("¡Hiciste clic!");
});

// Otros eventos útiles:
// "click"       → clic del mouse
// "mouseover"   → cuando el mouse pasa encima
// "keydown"     → cuando se presiona una tecla
// "submit"      → cuando se envía un formulario
// "change"      → cuando cambia el valor de un input
```

### Leer el valor de un input

```javascript
let input = document.querySelector("#mi-input");
let valor = input.value;

console.log(valor);
```

### Condicionales, loops, etc.

Los mismos conceptos que en Python, con sintaxis diferente:

```javascript
// if/else
if (edad >= 18) {
  console.log("Mayor de edad");
} else {
  console.log("Menor de edad");
}

// for
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// forEach en arrays (como for in Python)
let frutas = ["manzana", "pera", "banana"];
frutas.forEach(function(fruta) {
  console.log(fruta);
});
```

---

## 5. jQuery — JS más fácil

jQuery hace lo mismo que JavaScript puro, pero con menos código.

### Cómo incluirlo

```html
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
```

> ⚠️ Incluye jQuery **antes** de tu archivo JS.

### Seleccionar elementos

```javascript
// JavaScript puro:
document.querySelector("#mi-caja")

// jQuery:
$("#mi-caja")           // por id
$(".tarjeta")           // por clase
$("h1")                 // por etiqueta
```

### Modificar elementos

```javascript
$("#titulo").text("Nuevo título");         // Cambiar texto
$("#caja").html("<p>Contenido HTML</p>");  // Cambiar HTML interno
$("#caja").css("color", "red");            // Cambiar estilo
$("#caja").addClass("activo");            // Agregar clase
$("#caja").removeClass("activo");         // Quitar clase
$("#caja").toggleClass("activo");         // Alternar clase
```

### Mostrar y ocultar

```javascript
$("#caja").hide();           // Ocultar
$("#caja").show();           // Mostrar
$("#caja").toggle();         // Alternar mostrar/ocultar

// Con animación
$("#caja").fadeOut();
$("#caja").fadeIn();
$("#caja").slideUp();
$("#caja").slideDown();
```

### Eventos

```javascript
// Click
$("#boton").click(function() {
  alert("¡Clic!");
});

// Hover (mouse encima / mouse sale)
$("#caja").hover(
  function() { $(this).css("background", "yellow"); },  // al entrar
  function() { $(this).css("background", "white"); }    // al salir
);

// Leer valor de input
let valor = $("#mi-input").val();
```

### Esperar a que cargue la página

```javascript
$(document).ready(function() {
  // Todo tu código va aquí dentro
  console.log("La página cargó");
});
```

---

## 6. Bootstrap — diseño sin esfuerzo

Bootstrap es un conjunto de clases CSS ya escritas. Solo las agregas a tu HTML y listo.

### Cómo incluirlo

```html
<head>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <!-- Tu contenido -->

  <!-- Bootstrap JS (al final del body) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
```

### Sistema de grillas (grid)

Bootstrap divide la pantalla en **12 columnas**. Tú decides cuántas ocupa cada elemento.

```html
<div class="container">
  <div class="row">
    <div class="col-6">Ocupa la mitad</div>
    <div class="col-6">Ocupa la mitad</div>
  </div>
  <div class="row">
    <div class="col-4">Un tercio</div>
    <div class="col-4">Un tercio</div>
    <div class="col-4">Un tercio</div>
  </div>
</div>
```

### Botones

```html
<button class="btn btn-primary">Azul</button>
<button class="btn btn-secondary">Gris</button>
<button class="btn btn-success">Verde</button>
<button class="btn btn-danger">Rojo</button>
<button class="btn btn-warning">Amarillo</button>
<button class="btn btn-outline-primary">Contorno azul</button>
```

### Alertas

```html
<div class="alert alert-success">¡Operación exitosa!</div>
<div class="alert alert-danger">Hubo un error.</div>
<div class="alert alert-warning">Cuidado con esto.</div>
<div class="alert alert-info">Información útil.</div>
```

### Tarjetas (cards)

```html
<div class="card" style="width: 300px;">
  <img src="foto.jpg" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Título de la tarjeta</h5>
    <p class="card-text">Descripción del contenido.</p>
    <a href="#" class="btn btn-primary">Ver más</a>
  </div>
</div>
```

### Utilidades de espaciado y texto

```html
<!-- Márgenes: m = margin, p = padding -->
<!-- t=top, b=bottom, s=start(izq), e=end(der), x=horizontal, y=vertical -->
<!-- 0 al 5 = cantidad de espacio -->
<div class="mt-3">Margen arriba mediano</div>
<div class="p-4">Padding grande en todos lados</div>
<div class="mx-auto">Centrado horizontalmente</div>

<!-- Texto -->
<p class="text-center">Centrado</p>
<p class="text-end">A la derecha</p>
<p class="fw-bold">Negrita</p>
<p class="text-muted">Texto gris tenue</p>
<p class="text-primary">Azul</p>
<p class="text-danger">Rojo</p>
```

### Navbar (barra de navegación)

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="#">Mi Sitio</a>
    <ul class="navbar-nav ms-auto">
      <li class="nav-item"><a class="nav-link" href="#">Inicio</a></li>
      <li class="nav-item"><a class="nav-link" href="#">Sobre mí</a></li>
      <li class="nav-item"><a class="nav-link" href="#">Contacto</a></li>
    </ul>
  </div>
</nav>
```

---

## 7. Cómo conectar todo

### Estructura de carpetas recomendada

```
mi-proyecto/
├── index.html
└── assets/
    ├── css/
    │   └── styles.css
    ├── js/
    │   └── app.js
    └── img/
        └── foto.jpg
```

### Conectar CSS y JS en el HTML

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <title>Mi proyecto</title>

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Tu CSS (después de Bootstrap para poder sobreescribir) -->
    <link rel="stylesheet" href="assets/css/styles.css">
  </head>
  <body>

    <!-- Tu contenido HTML aquí -->

    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Tu JS (al final, después de jQuery y Bootstrap) -->
    <script src="assets/js/app.js"></script>
  </body>
</html>
```

> 💡 Los `<script>` van al **final del body** para que el HTML cargue primero.

---

## 8. Errores comunes

### El CSS no se aplica
- Revisa que el archivo esté bien enlazado en el `<head>`
- Verifica que el nombre de la clase en CSS coincida exactamente con el del HTML
- Abre las DevTools (F12) → pestaña "Elements" para ver qué estilos se están aplicando

### El JS no funciona
- Abre las DevTools (F12) → pestaña "Console" para ver errores
- Asegúrate de que el `<script>` está al final del body
- Si usas jQuery, verifica que se cargue antes de tu archivo JS

### El elemento no se encuentra
```javascript
// Si esto da null, el id está mal escrito o el elemento no existe
let el = document.getElementById("mi-caja");
console.log(el);  // Si es null, hay un error
```

### La imagen no aparece
```html
<!-- Verifica la ruta -->
<img src="assets/img/foto.jpg" alt="Foto">
<!-- Abre DevTools → Network → recarga para ver si la imagen da 404 -->
```

---

## 9. Resumen rápido

### HTML

| Etiqueta | Para qué sirve |
|----------|---------------|
| `<h1>` a `<h6>` | Títulos |
| `<p>` | Párrafo |
| `<a href="">` | Enlace |
| `<img src="">` | Imagen |
| `<div>` | Contenedor bloque |
| `<span>` | Contenedor en línea |
| `<ul>` / `<li>` | Lista con puntos |
| `<button>` | Botón |
| `<input>` | Campo de texto |

### CSS

| Propiedad | Para qué sirve |
|-----------|---------------|
| `color` | Color del texto |
| `background-color` | Color de fondo |
| `font-size` | Tamaño de texto |
| `padding` | Espacio interior |
| `margin` | Espacio exterior |
| `display: flex` | Pone hijos en fila |
| `border-radius` | Bordes redondeados |

### jQuery

| Código | Para qué sirve |
|--------|---------------|
| `$("#id")` | Seleccionar por id |
| `$(".clase")` | Seleccionar por clase |
| `.text("...")` | Cambiar texto |
| `.css("prop", "val")` | Cambiar estilo |
| `.hide()` / `.show()` | Ocultar / mostrar |
| `.addClass()` | Agregar clase |
| `.click(fn)` | Manejar clic |
| `.val()` | Leer valor de input |

### Bootstrap — clases más usadas

| Clase | Para qué sirve |
|-------|---------------|
| `container` | Centra el contenido con márgenes |
| `row` / `col-N` | Sistema de grilla (N = 1 a 12) |
| `btn btn-primary` | Botón azul |
| `alert alert-success` | Alerta verde |
| `card` | Tarjeta con sombra |
| `text-center` | Texto centrado |
| `mt-3`, `p-4` | Márgenes y padding |
| `navbar` | Barra de navegación |

---

*¡Recuerda abrir las DevTools (F12) siempre que algo no funcione, po!* 🚀
