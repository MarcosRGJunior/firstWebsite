const nav = document.querySelectorAll(".nav-link");
const chec = document.querySelectorAll(".btn-danger");
const limpar = document.querySelectorAll(".limpar");
const entradas = document.querySelectorAll(".form-control");

for (let teste of nav){
    teste.addEventListener("mouseover", function(){
        console.log("Mouse em cima do h1");
        teste.style.color = "#F2C42C" ;
    });
}

for (let teste of nav){
  teste.addEventListener("mouseout", function(){
      console.log("Mouse em cima do h1");
      teste.style.color = "#50BFD4" ;
  });
}

for (let teste of chec){
    teste.addEventListener("click", function(event){
        
        console.log("Mouse em cima do nav");
        validacao = confirm("Certeza?")
        if(validacao){
            console.log("Você clicou em ok");
            event.confir ;
        }
        else{
            console.log("Você clicou em cancelar");
            event.preventDefault();
        }
    });
  }
  

  for (let teste of limpar){
    teste.addEventListener("click", function(){
        console.log('Está passando aqui');
        for ( let ent of entradas){
            console.log('Apagando '+ ent)
            ent.value = ""
        }
    });
  }
  