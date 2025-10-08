package main

import "fmt"

func switch_state() {
	// 1. normal use
	num := 5
	dayofWeek := ""
	switch num {
	case 1:
		dayofWeek = "Monday"
	case 2:
		dayofWeek = "Tuesday"
	case 3:
		dayofWeek = "Wednesday"
	case 4:
		dayofWeek = "Thrusday"

	case 5: dayofWeek = "Friday"
		
	case 6: dayofWeek = "Saturday"
		
	case 7: dayofWeek = "Sunday"

	default:
		dayofWeek = "__error__"
	}
	fmt.Println(dayofWeek)

	// using fallthrough
	grade := "C"
	switch grade {
	case "A":
		fallthrough
	case "B": 
		fallthrough
	case "C":
		fallthrough
	case "D":
		fmt.Println("Passed")
	case "F":
		fmt.Println("Failed")
	default:
		fmt.Println("Absent")
	}

	// matching multiple cases
	Grade := "c"
	switch Grade{
	case "A", "B", "C", "D":
		fmt.Println("Passed")
	case "F":
		fmt.Println("failed")
	default:
		fmt.Println("Absent")
	}

	// conditonal checks within switch
	score := 79
	GRade := ""
	switch {
	case score < 50: GRade = "F"
	case score < 60: GRade = "D"
	case score < 70: GRade = "C"
	case score < 80: GRade = "B"
	default: GRade = "A"
	}
	fmt.Println(GRade)
	// in c, java, the case expresiion must be constants
	
}