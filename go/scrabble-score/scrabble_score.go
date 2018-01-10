// Package scrabble provides utility functions for Scrabble.
package scrabble

import (
	"fmt"
	"unicode"
)

// getScore returns the Scrabble score of a given rune.
func getScore(r rune) int {
	switch r {
	case 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T':
		return 1
	case 'D', 'G':
		return 2
	case 'B', 'C', 'M', 'P':
		return 3
	case 'F', 'H', 'V', 'W', 'Y':
		return 4
	case 'K':
		return 5
	case 'J', 'X':
		return 8
	case 'Q', 'Z':
		return 10
	default:
        panic(fmt.Sprintf("Invalid: %c!", r))
	}
}

// Score calcualtes the Scrabble score of the input word.
func Score(word string) (score int) {
	for _, c := range word {
		score += getScore(unicode.ToUpper(c))
	}
	return
}

