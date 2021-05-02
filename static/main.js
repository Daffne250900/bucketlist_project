'use strict'

var boton =  document.querySelector(".btn");

boton.addEventListener('mouseover', function(){
    boton.style.transform = "scale(1.05,1.05)";
});

boton.addEventListener('mouseout', function(){
    boton.style.transform = "scale(1,1)";
});

