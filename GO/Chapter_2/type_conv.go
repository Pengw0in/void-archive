package main

import (
	"fmt"
	"strconv"
)

func type_conv() {
	var age string
	fmt.Print("Please enter your age: ")
	fmt.Scanf("%s" , &age)

	// strconv - for string conversion!

	rAge, err := strconv.Atoi(age)		// Atoi = ASCII to Interger , similarily Itoa exists

	if err !=nil {
		fmt.Println(err)		// prints out error
	} else {
		fmt.Printf("Your age: %d" ,rAge)
	}



	b, err := strconv.ParseBool("t")
	fmt.Println(b)		// true
	fmt.Println(err)	// <nil>

	f, err := strconv.ParseFloat("1.732", 64)
	fmt.Println(f)		
	fmt.Println(err)

	k, err := strconv.ParseInt("-13.53", 10, 64)
	fmt.Println(k)			// 0
	fmt.Println(err)		// strconv.ParseInt: parsing  "-18.56": invalid syntax

	// like wise we have, ParseUint

	// for interconversion between numbers
	num1 := 5
	num2 := float32(num1)
	num3 := float64(num2)
	num4 := int(num3)

	fmt.Printf("%T\n", num1) // int
	fmt.Printf("%T\n", num2) // float32
	fmt.Printf("%T\n", num3) // float64
	fmt.Printf("%T\n", num4) // int

}