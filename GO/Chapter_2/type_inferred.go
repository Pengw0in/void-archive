package main

import "fmt"

var num0 = 2 // no error - package level variable (global level)

func type_inferred() {
	var num1 = 5			// type inferred - ie, data type is deduced by its value
	fmt.Println(num1)		// 5
}