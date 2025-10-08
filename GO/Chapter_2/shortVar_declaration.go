package main

import "fmt"

// ide := "VScode" 		*** NOT_ALLOWED, non-declarative statement outside function body
//						:= operator only used in fucntion for init and declaring

func shorVar(){
	firstName := "Zendex"		// shorter version of type-inferred
	langauge, magicNumber, PI := "Go", 69, 3.14 // declare and initialize multiple variables (of different types) 
	
	/* var keyword also supports multiple declation(of same type only in single line inits)
	 var github, planet string = "Pengw0in", "earth" 		*ALLOWED
	 var name string, age int = "NAME", 20        		*NOT_ALLOWED 

	 But you can do this,
	 var name, age = "NAME", 20
	 or also this (multi line declartion supoorts multiple data types inits)
	 var (
	 	firstName string = "Zendex"
		lastName string = "I dont have a last name!"
		age int = 20 (not real)
	 ) 
	 */

	fmt.Println(firstName)
	fmt.Println(langauge)
	fmt.Println(magicNumber)
	fmt.Println(PI)				// *declared as float64
}