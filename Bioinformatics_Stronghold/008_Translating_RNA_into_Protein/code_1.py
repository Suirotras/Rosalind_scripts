import os
import itertools

os.chdir('C:\\Users\\User\\github\\Rosalind_scripts\\')

with open("rosalind_prot.txt", "r") as f_in, open("output.txt", 'w') as f_out:
    
    line = f_in.read().upper()

    # generate the codon combinations
    nucl_list = ["U", "C", "A", "G"]

    def generate_codon_list(nucl_list):
        x = itertools.product(nucl_list, repeat=3)
        codon_list = list(map(''.join, x))
        return codon_list
    
    codons = generate_codon_list(nucl_list)

    # get corresponding amino acid list
    aa = ["F"]*2 + ["L"]*2 + ["S"]*4 + ["Y"]*2 + ["Stop"]*2 + ["C"]*2 + ["Stop"] \
    + ["W"] + ["L"]*4 + ["P"]*4 + ["H"]*2 + ["Q"]*2 + ["R"]*4 + ["I"]*3 + ["M"] \
    + ["T"]*4 + ["N"]*2 + ["K"]*2 + ["S"]*2 + ["R"]*2 + ["V"]*4 + ["A"]*4 + ["D"]*2 \
    + ["E"]*2 + ["G"]*4

    # find the start of the translated region
    start_id = line.find("AUG")

    # check if AUG was found
    if start_id != -1:

        # create empty aa string
        aa_string = ""

        # loop through the codons in the right reading frame
        for i in range(start_id, len(line), 3):
            codon = line[i:i+3]

            # check if stopcodon
            if codon in ["UAA", "UAG", "UGA"]:
                break

            # translate codon to aa
            codon_index = codons.index(codon)
            aa_string += aa[codon_index]

    else:
        print("ERROR, no start codon found!")

    f_out.write(aa_string)