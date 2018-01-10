// Package calculates the hamming hamlength between two DNA strings
package hamming

import "errors"

// Distance between two DNA strings, as an integer.
func Distance(a, b string) (int, error) {
    
    var hamlength int
    var err error

    // Trivial statement: unequal strand length
	if len(a) != len(b) {
		return -1, errors.New("strand lengths must be identical")
	}

	// Equal strand length
    for i := range a {
		if a[i] != b[i] {
			hamlength++
		}
	}

	return hamlength, err


}
