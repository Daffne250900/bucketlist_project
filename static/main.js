'use strict'

var boton =  document.querySelector(".btn");

boton.addEventListener('mouseover', function(ev){
    ev.stopPropagation();
    boton.style.transform = "scale(1.05,1.05)";
});

