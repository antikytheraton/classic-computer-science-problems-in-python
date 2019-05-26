from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A','C','G','T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "AGCTACGTCGTAGCTATCATCGATCACGATCGATCTTCTTTGAGAAAGCCTCTAGCTAGCATACTA"

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):   # don't run off end!
            return gene
        # Initialize codon out of three nucleotides
        codon: Codon = (
            Nucleotide[s[i]],
            Nucleotide[s[i+1]],
            Nucleotide[s[i+2]]
        )
        gene.append(codon)  # add codon to gene
    return gene


my_gene: Gene = string_to_gene(gene_str)
acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)


''' Linear Search '''

print('------Linear Search------')
print(acg in my_gene) # False
print(gat in my_gene) # True


''' Binary Search '''

def binary_contains(gene: Gene, codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < codon:
            low = mid + 1
        elif gene[mid] > codon:
            high = mid - 1
        else:
            return True
    return False

my_sorted_gene: Gene = sorted(my_gene)

print('------Binary Search------')
print(binary_contains(my_sorted_gene, acg)) # False
print(binary_contains(my_sorted_gene, gat)) # True

