import os

os.chdir('C:\\Users\\User\\github\\Rosalind_scripts\\')

with open("rosalind_fibd.txt", "r") as f_in, open("output.txt", 'w') as f_out:
    
    string = f_in.read()
    string = string.strip()

    n = int(string.split(" ")[0])
    m = int(string.split(" ")[1])

    # define k as 1
    k = 1

    # initialize rabbit seq_list
    seq = [1,1]

    for i in range(n):
        if i != 0 and i != 1:
            if len(seq) < m:
                Fn = seq[i-1] + seq[i-2]*k
            else:
                Fn = seq[i-1] + seq[i-2]*k - seq[i-(m)]
            # add to list
            seq.append(Fn)

    # return number rabbits
    f_out.write(str(seq[::-1][0]))