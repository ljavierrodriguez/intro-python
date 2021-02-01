// Tipos de Datos
/*
String = "", '', ``
Number = -1 , 1.1,  1
Boolean = true o false
Undefined = undefined

Object
    Array = array() o []
    Null = null
    object = {}

*/
// var let const
let a = "Luis";
let b = 1;
let c = false;
let d;
let nombres = ["Hugo", "Paco", "Luis"];

let persona = {
    nombre: "",
    apellido: ""
}

console.log(typeof(a));


class Person {
    nombre = "";
    constructor(){

    }

    func(){

    }
}

class Student extends Person {
    nombre = "";
    constructor(){
        super();

    }

    func(){

    }
}

let p = new Person();
p.func()