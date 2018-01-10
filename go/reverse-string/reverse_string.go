package reverse

func Reverse(word string) string {

    l := len(word)
    wordrune := []rune(word)

    for i := range wordrune {
        wordrune[i], wordrune[l-1-i] = wordrune[l-1-i], wordrune[i]
    }

    return string(wordrune)
}

