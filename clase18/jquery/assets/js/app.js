/*
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

$("#idasignatura").text(nombreAsignatura);
$("#idnota1").text(nota1);
$("#idnota2").text(nota2);
$("#idnota3").text(nota3);
$("#idpromedio").text(promedio);


*/

$("#enviarCorreo").on( "click", function() {
  alert("EL CORREO SE ESTÁ ENVIANDO...");
} );


$("h1").on( "dblclick", function() {
  $(this).css( "color", "red" );
} );

$(".titulo-card").on( "click", function() {
  $(".contenido-card").toggle()
} );
