package main

import (
	"fmt"
	"strconv"
)

func string_inter() {
	queue, name := 5, "Zendex"
	// s := name + " your number is: " + queue || THIS IS NOT POSSIBLE AS "queue" IS NOT STRING
	s := name + ", your queue number is:" + strconv.Itoa(queue)
	fmt.Println(s)

	// or a beter solution is
	x := fmt.Sprintf("%s, your queue num is id %d", name, queue)
	fmt.Println(x)

}