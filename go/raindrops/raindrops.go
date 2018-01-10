package raindrops

import "strconv"

//Convert says Pling, Plang or Plong depending on whether the input number is divisible by 3, 5, 7 or not
func Convert(input int) string {
	result := ""
	if input%3 == 0 {
		result += "Pling"
	}
	if input%5 == 0 {
		result += "Plang"
	}
	if input%7 == 0 {
		result += "Plong"
	}
	if len(result) == 0 {
		return strconv.Itoa(input)
	}
	return result
}
