// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package bob should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
package bob

// Hey should have a comment documenting it.
func Hey(remark string) string {

    if(remark == "")
        return "Fine. Be that way!"

    if(remark.Contains("?") && remark == remark.ToUpper())
        return "Calm down, I know what I'm doing!"

    if(remark == remark.ToUpper())
        return "Whoa, chill out!"
    
    if(remark.Contains("?"))
        return "Sure."
    
    return "Whatever."
}
