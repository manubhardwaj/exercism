// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package acronym should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
package acronym

import "strings"
import "unicode"

// Abbreviate should have a comment documenting it.
func Abbreviate(s string) string {

    f := func(c rune) bool {
		return unicode.IsSpace(c) || (c=='-')
	}

    words := strings.FieldsFunc(s,f)

    var retval string
    for _, value := range words {    
       retval += strings.ToUpper(string(value[0]))
   }
    return retval
}
