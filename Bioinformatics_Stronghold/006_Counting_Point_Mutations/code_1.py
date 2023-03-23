import os

os.chdir('C:/Users/User/Desktop/Rosalind_scripts')

with open("rosalind_hamm.txt", "r") as f_in, open("output.txt", 'w') as f_out:
    
    ### get max_line count
    for line_number, line in enumerate(f_in):
        pass

    max_line_number = line_number

    # reset file index
    f_in.seek(0)

    # create sequence list
    seq_list = []

    ### get sequences
    for line in f_in:
        line = line.strip()

        seq_list.append(line)

    ### check if sequences have the same length using the all() method
    seq_length = len(seq_list[0])
    result = all(len(element) == seq_length for element in seq_list)

    ### run if sequences are same length
    if result == True:

        # start distance counter
        hamming_dist = int(0)

        for base_index in range(int(seq_length)):
            if seq_list[0][base_index] != seq_list[1][base_index]:
                hamming_dist += int(1)

    ### output hamming distance
    f_out.write(str(hamming_dist))