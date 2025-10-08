package main

import "fmt"

func main() {
	num := 5
	condition := num%2 == 1
	if condition {
		fmt.Println("Number is odd")
	} else {
		fmt.Println("Number is even")
	}
}
