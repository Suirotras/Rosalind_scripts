import os
from random import choice
from itertools import repeat
from collections import Counter
from statistics import mean

os.chdir('C:\\Users\\User\\github\\Rosalind_scripts\\')

with open("rosalind_iev.txt", "r") as f_in, open("output.txt", 'w') as f_out:
    # get string of genotype occurences
    string = f_in.read().strip()
    # split into list
    freq = string.split()
    # get corresponding genotypes
    genotype = ["AA-AA", "AA-Aa", "AA-aa", "Aa-Aa", "Aa-aa", "aa-aa"]
    # create list with all occurences in a row
    freq_genotype = []
    for index in range(len(freq)):
        # get frequencies
        occurence = int(freq[index])
        # repeat genotype
        genotype_rep = repeat(genotype[index], occurence)
        # add to freq_genotype
        freq_genotype += list(genotype_rep)
    
    dom_prop_list = []

    # calculate dominant frequency multiple times for accuracy, than take the mean
    for cycle in range(30):
        # draw 10000000 times a random individual from this pool of genotypes
        random_draws = iter([choice(freq_genotype) for i in range(1000000)])

        c = Counter(random_draws)
        print(c)
        # get total number
        total = sum(c.values())
        
        # get proportion of dominant phenotype picks
        dom_freq = float(0)
        for allele in genotype:
            # check if freq is None, meaning no individual of this genotype was picked
            if (f := c.get(allele)) != None and allele not in ["aa-aa"]:
                
                if allele == "Aa-Aa":
                    dom_freq += float(f)*float(3/4)
                elif allele == "Aa-aa":
                    dom_freq += float(f)*float(1/2)
                else:
                    dom_freq += float(f)

        dom_prop_list.append(dom_freq/total)
    
    dom_prop = mean(dom_prop_list)
    
    # use proportion to get mean number of dominant individuals in next generation
    mean_dom = (len(freq_genotype)*(number_of_offspring := 2))*dom_prop

    ### if I used the generation methods answer

    # round number
    #f_out.write(str(round(mean_dom, ndigits=1)))
    # do not round number
    #f_out.write(str(mean_dom))

    ### as the generation method is not accurate enough for the rosalind answer, I calculate the true value here.
    ### THe generation method might not be efficient, but I wanted to try it for practice
    freq = list(map(float, freq))
    first, second, thirth, fourth, fifth, sixth = freq
    expected_number = ((first*2)+(second*2)+(thirth*2)+(fourth*2*float(3/4))+(fifth*2*float(1/2)))
    f_out.write(str(expected_number))