//Package isogram checks if a given word contains repeated letters or not
package isogram

import (
    "strings"
    "unicode"
)

func IsIsogram(word string) bool {

    m := make(map[rune]bool)

    wordrune := []rune(strings.ToLower(word))

    for _, i := range wordrune {
        
        if(m[i] && unicode.IsLetter(i)) {
            return false
        }

        m[i] = true
    }

    return true

}

