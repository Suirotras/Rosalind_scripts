import os

os.chdir('C:\\Users\\User\\github\\Rosalind_scripts\\')

### define functions
# check equal length
def check_length(seq_dict):
    ### check if all sequences have the same length
    
    # get length of first item is dictionary
    seq_length = len(next(iter(seq_dict.values())))
    # check if this length corresponds with all other lengths
    length_check = all(len(value) == seq_length for value in seq_dict.values())
    # return length_check
    return length_check

# get consensus sequence
def get_consensus(seq_dict):
    consensus = ""
    
    for index in range(len(next(iter(seq_dict.values())))):

        counts = list(map(lambda x: x[index], seq_dict.values()))
        most_common = max(set(counts), key = counts.count)
        consensus += most_common
    
    return consensus

# get dictionary with site specific counts for all nucleotides
def get_site_count(seq_dict):
    site_counts = {}
    
    nucl_counts_list = ["", "", "", ""]

    for index in range(len(next(iter(seq_dict.values())))):
        
        site = list(map(lambda x: x[index], seq_dict.values()))
        
        # generate a list giving site specific nucl counts for A,C,G,T
        nucl_counts = [str(site.count(nucl)) for nucl in "ACGT"]
        nucl_counts_list = [old_pos + new_pos + " " for new_pos, old_pos in zip(nucl_counts, nucl_counts_list)]
    
    #remove whitespace at string ends
    nucl_counts_list = map(lambda x: x[:-1], nucl_counts_list)

    # add to dictionary
    for key, value in zip(["A","C","G","T"], nucl_counts_list):
        site_counts[key] = value

    return site_counts


with open("rosalind_cons.txt", "r") as f_in, open("output.txt", 'w') as f_out:
    
    # read fasta file
    string = f_in.read()
    # split string
    seq_list = string.split(">")

    # remove empty strings from list
    seq_list = list(filter(lambda x: x != '', seq_list))
    # create list with just sequence names
    seq_list_name = [seq.split(maxsplit=1)[0].strip() for seq in seq_list]
    # create list with just the sequences
    seq_list_sequence = [seq.split(maxsplit=1)[1].strip() for seq in seq_list]
    # remove endline characters from the string
    seq_list_sequence = [seq.replace("\n","") for seq in seq_list_sequence]

    # create sequence dictionary from lists
    seq_dict = {}
    for seq_name, seq_sequence in zip(seq_list_name, seq_list_sequence):
        seq_dict[seq_name] = seq_sequence

    if check_length(seq_dict):
        # get consensus sequence
        consensus = get_consensus(seq_dict)
        
        # get counts per site dictionary
        counts_dict = get_site_count(seq_dict)

        f_out.write(f'{consensus}\nA: {counts_dict.get("A")}\nC: {counts_dict.get("C")}\nG: {counts_dict.get("G")}\nT: {counts_dict.get("T")}')
    else:
        print("Length of sequences not identical")
            