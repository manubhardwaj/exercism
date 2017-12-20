# This is a stub function to take two strings
# and calculate the hamming distance
hamming <- function(strand1, strand2) {

    s1split <- strsplit(strand1, "")[[1]]
    s2split <- strsplit(strand2, "")[[1]]

    stopifnot(length(s1split) == length(s2split))
    return(sum(s1split != s2split))
}
