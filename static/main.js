
var desc =  document.getElementById("description");

desc.addEventListener('focus', function(ev){
    desc.style.background = "rgba(0,0,0,0.2)";
});

desc.addEventListener('blur', function(ev){
    desc.style.background = "white";
});



var title = document.getElementById("title"); 

title.addEventListener('focus', function(ev){
    title.style.background = "rgba(0,0,0,0.2)";
});

title.addEventListener('blur', function(ev){
    title.style.background = "white";
});


var location = document.getElementById("location"); 

location.addEventListener('focus', function(ev){
    location.style.background = "rgba(0,0,0,0.2)";
});

location.addEventListener('blur', function(ev){
    location.style.background = "white";
});