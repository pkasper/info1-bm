# coding: utf-8

# DNA string matching

def get_dna_sequence(file_name):
    dna_sequence = ''
    dna_file = open(file_name, 'r')
    
    for line in dna_file:
        dna_sequence += line

    dna_sequence = dna_sequence.replace(' ', '')
    dna_sequence = dna_sequence.replace('\n', '')
    
    dna_file.close()

    return dna_sequence


yeast_dna = get_dna_sequence('bakers_yeast.txt')

# find some shorter sequences

find_agt = yeast_dna.find('AGT')
print(find_agt)


# this just gave us the first occurrence
# what if there are more?
# let's search in substrings!

matches = []
index = 0
sequence_to_find = 'AGT'

while True:
    new_index = yeast_dna[index:].find(sequence_to_find)
    if new_index is -1:
        break
    else:
        index += new_index + 1
        matches.append(index)

print(matches)


# find a specific genome

genome_dna = get_dna_sequence('AXL2_genomic.txt')

print(yeast_dna.find(genome_dna))

