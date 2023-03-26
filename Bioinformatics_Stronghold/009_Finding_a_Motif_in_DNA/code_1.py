import os
import re

os.chdir('C:\\Users\\User\\github\\Rosalind_scripts\\')

with open("rosalind_subs.txt", "r") as f_in, open("output.txt", 'w') as f_out:
    
    # get variables
    string = f_in.readline().strip()
    # use the lookahead extention to find overlapping substrings
    substring = "(?=" + f_in.readline().strip() + ")"
    # compile Regular expression
    m = re.compile(substring)
    
    # get match iterator
    matches = m.finditer(string)

    pos_string = ""

    for index, match in enumerate(matches):
        # get starting position. The +1 corrects for the 0-based numbering
        pos = str(match.start() + 1) + " "
        
        # add to string
        pos_string += pos

    f_out.write(pos_string[:-1])