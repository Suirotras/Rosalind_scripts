def rev_complement(string):
        #Reverse string
    string = string.upper()[::-1]
    #get nucleotide pairs
    
    for pos in range(len(string)):
        if string[pos] == "A":
            string = string[:pos] + "T" + string[pos+1:]
        elif string[pos] == "T":
            string = string[:pos] + "A" + string[pos+1:]
        elif string[pos] == "C":
            string = string[:pos] + "G" + string[pos+1:]
        elif string[pos] == "G":
            string = string[:pos] + "C" + string[pos+1:]

    return string