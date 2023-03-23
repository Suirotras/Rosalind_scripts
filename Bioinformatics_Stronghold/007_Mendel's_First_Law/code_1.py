import os
import random

os.chdir('C:\\Users\\User\\github\\Rosalind_scripts\\')

with open("rosalind_iprb.txt", "r") as f_in, open("output.txt", 'w') as f_out:
    
    line = f_in.read()
    print(line)
    
    # split the line into variables
    k, m, n = line.split()

    k = int(k)
    m = int(m)
    n = int(n)
    # get total individuals
    total = int(k) + int(m) + int(n)
    
    ### now calculate the chances of producing an individual with at least one dominant allele
    # the chance in situations with at least one homozygous dominant parent
    pr_k = (k/total)*((k-1)/(total-1)) + (k/total)*(m/(total-1)) + (k/total)*(n/(total-1)) \
    + (m/total)*(k/(total-1)) + (n/total)*(k/(total-1)) 
    
    # the chance in situations with heterzygous individuals or recessive individuals only
    pr_m = (m/total)*((m-1)/(total-1))*(3/4) + (m/total)*(n/(total-1))*(1/2) \
    + (n/total)*(m/(total-1))*(1/2)

    # total chance
    dom_chance = pr_k + pr_m
    
    # output chance
    f_out.write(str(dom_chance))