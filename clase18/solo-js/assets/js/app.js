// mostrar alertas en la parte arriba de la página
alert("Bienvenido a la calculadora de promedio")
alert("Por favor introduce la siguiente información para calcular tu promedio")

// pediamos la información al usuario
let nombreAsignatura = prompt("Ingresa el nombre de la asignatura")
let nota1 = parseFloat(prompt("Ingresa la nota 1"))
let nota2 = parseFloat(prompt("Ingresa la nota 2"))
let nota3 = parseFloat(prompt("Ingresa la nota 3"))

// calculo del promedio
let promedio = (nota1 + nota2 + nota3)/3 

// escribir en la consola
console.log(nombreAsignatura)
console.log(nota1)
console.log(nota2)
console.log(nota3)
console.log(promedio)


// traer el elemento
let spanAsignatura = document.getElementById("idasignatura")
let spanNota1 = document.getElementById("idnota1")
let spanNota2 = document.getElementById("idnota2")
let spanNota3 = document.getElementById("idnota3")
let spanPromedio = document.getElementById("idpromedio")

// cambiar la información de cada elemento
spanAsignatura.innerText = nombreAsignatura
spanNota1.innerText = nota1
spanNota2.innerText = nota2
spanNota3.innerText = nota3
spanPromedio.innerText = promedio.toPrecision(3)



