package main

import "fmt"

const language = "GO"

func contant() {
	fmt.Println(language)

	var num1 = 6 // complier throw an error if not used but,
	_ = num1 	 // _ operator can be used keep the compiler happy!
}