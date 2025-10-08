package main

import "fmt"

func do_something() (int, bool) {
	// ...
	// some random code
	return 5, false
}

func init() {
	/*
		if some variables are only used once in control flow statements
		then we directly initialize the variables in statement itself
		also, these varibles are limites to scope of statement only.
		They cannot be accessed outside of statement
	*/

	if v, err := do_something(); err {
		fmt.Println(err)
	} else {
		fmt.Println(v)
	}

	switch_state() // don't mind me *////*
}

// and there is no terenaru operators in Go, like "parity := num % 2 ? even : odd"

