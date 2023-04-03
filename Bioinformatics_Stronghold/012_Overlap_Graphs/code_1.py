import os
from itertools import combinations

os.chdir('C:\\Users\\User\\github\\Rosalind_scripts\\')

with open("rosalind_grph.txt", "r") as f_in, open("output.txt", 'w') as f_out:
    
    string = f_in.read()
    string_list = string.split(">")

    string_list = list(filter(lambda x: x != "", string_list))

    string_dict = {}

    # get dict
    for seq in string_list:
        
        x_name = seq.split(maxsplit=1)[0]
        x_seq = seq.split(maxsplit=1)[1].strip()
        string_dict[x_name] = x_seq

    # get iterator of sequence combinations
    seq_comb = combinations(string_dict.keys(), 2)
    #list(seq_comb)

    for comb in seq_comb:
        suffix_list = [string_dict[seq][-3:] for seq in comb]
        prefix_list = [string_dict[seq][:3] for seq in comb]
        
        suffix_to_prefix = suffix_list[0] == prefix_list[1]
        prefix_to_suffix = prefix_list[0] == suffix_list[1]

        if suffix_to_prefix:
            f_out.write(f"{comb[0]} {comb[1]}\n")
        elif prefix_to_suffix:
            f_out.write(f"{comb[1]} {comb[0]}\n")