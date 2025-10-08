package main

import "fmt"

func explicitly_inferred(){
	var num1 int 			// explicitly inferred
	var num6 float32 = 4.23
	var num2 = 6			// type inferred
	fmt.Println(num1)		// uninitialized integer is given value 0
	fmt.Println(num2)
	fmt.Println(num6)

	// some other data types default value
	var num3 float32
	var num4 string
	var sunny bool

	fmt.Println(num3) // 0
	fmt.Println(num4) // "" (empty string)
	fmt.Println(sunny) // flase
}