

dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'A': 'U',
        'T': 'A'
}

def to_rna(dna_strand):
    rna = ""
    for c in dna_strand:
        x = dna_to_rna.get(c)
        if ( x == None ):
            raise ValueError("Wrong input!")
        rna = rna + x
    return rna
