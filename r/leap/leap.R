leap <- function(year) {

    if(!year%%400)
        return(TRUE)
    if(!year%%100)
        return(FALSE)
    if(year%%4)
        return(FALSE)
    return(TRUE)
}
