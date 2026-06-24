def to_rna(dna_strand):
    t = ""
    for i in range(len(dna_strand)):
        if dna_strand[i] == "G":
            t += "C"
        if dna_strand[i] == "C":
            t += "G"
        if dna_strand[i] == "T":
            t += "A"
        if dna_strand[i] == "A":
            t += "U"
    return t