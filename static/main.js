'use strict'

var boton = document.querySelector(".btn");

boton.addEventListener('mouseover', function(ev){
    ev.stopPropagation();
    boton.style.transform = "scale(1.05,1.05)";
});


var titulo = document.querySelector("#title");

titulo.addEventListener('focus', function(){
    titulo.style.background = "rgb(0,0,0,0.2)";
});

titulo.addEventListener('blur', function(){
    titulo.style.background = "white";
});



var description = document.querySelector("#description");

description.addEventListener('focus', function(){
    description.style.background = "rgb(0,0,0,0.2)";
});

description.addEventListener('blur', function(){
    description.style.background = "white";
});



var location = document.querySelector("#location");

location.addEventListener('focus', function(){
    location.style.background = "rgb(0,0,0,0.2)";
});

location.addEventListener('focus', function(){
    location.style.background = "white";
});