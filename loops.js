// loops

// for, for in, for of, while, do while, 

let nombres = ["Hugo", "Paco", "Luis"];

for(let i=0; i < nombres.length; i ++){
    if (i == 2) break;
    console.log(nombres[i]);
}

for(let i in nombres){
    console.log(nombres[i]);
}

for(let nombre of nombres){
    console.log(nombre);
}

let i = 0;
while(i < nombres.length){
    console.log(nombres[i]);
    i++;
}