package main

import (
	"fmt"
	"time"
	"reflect"
)

func var_type() {
	start := time.Now()
	fmt.Printf("%T\n", start)			    // time.Time
	fmt.Println(reflect.TypeOf(start))  // time.Time
	fmt.Println(reflect.ValueOf(start).Kind()) // struct
}
