//The var statement declares function-scoped or globally-scoped variables, 
//optionally initializing each to a value.

var x = 1;

if(x==1){
    var x = 2;
    //globally changed

    console.log(x);
}
console.log(x);


var name1;
var name1 = value1;
var name1 = value1, name2 = value2;
var name1, name2 = value2;
var name1 = value1, name2, /* …, */ nameN = valueN;
