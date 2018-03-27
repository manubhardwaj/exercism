# Thanks @iainsgillis
to_rna <- function(dna) {
  if(grepl("[^ACGT]", dna)) {
    stop("incomplete dna")
  } else {
    chartr("ACGT", "UGCA", dna)
  }
}
