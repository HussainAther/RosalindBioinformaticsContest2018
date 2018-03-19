from difflib import *
import itertools
from difflib import SequenceMatcher, Differ

file = open("/Users/syedather/Downloads/tests/test3.fasta", "r")

solutions = []

seq = "TTTGTGGCTCGTGCGTCTCACTAATGTCGCGTATAGCCCGGCCAAGCGCGGTGAGCAGACGACTCGTGTGGAAAGAATAAATCGCGCAACGAAGCCATCTCCGCGTTCGTACGGGATGCCGTCACTTCATTCAGACTGCTAACCCAGTCTGACGTAGAATCGAGTAGTCCACTCGAGGACGATCCCGTGGGCTGGCAGGCCCGGACTTGCCTAGAACGCTGAATTACTTAAACTACGTGAGCCACTTAAACTAATCACTGATGCCGAGTAGGCAGTGCATTTACGATATCATTTGAGTCAGAAATaTTatatctctaTAATAAACAAtagatgcttttgtctttcgagcgggaaaacgctacgattatagtcacgcgggctgaccggctgggtcctgactggcCTGGGCAGTGGCGGTTGGCTGATGACATGGAAAATGCGGTGCAAAGGATATCTGGGCTTTGGTCACGCGGGAtgccctcttagcggcagatgctagattctggCCTCACCAACAGATCAGGTTCTTtaccggccccaggggcagAAGACAAGCAAAGATAGCGATTGCacgtaaaacaccttctcaacgaggataagctgcggtgaagctagtctggcactgtagagtcaacattgcatcggtcacattagccgttactaaggaaaccggtgaaaacgaaatgggcgtgtggaatcttgttGACAATACTTGCCATCGCTTGATTcgctgagcataaattatCCACTCATGAGAATATACGTTTatggcTCGTGCGTCTCACTAATGTCGCGTATAGCCCGGCCAAGCGCGGTGAGCAGACGACTCGTGTGGAAAGAATAAATCGCGCAACGAAGCCATCTCCGCGTTCGTACGGGATGCCGTCACTTCATTCAGACTGCTAACCCAGTCTGACGTAGAATCGAGTAGTCCACTCGAGGACGATCCCGTGGGCTGGCAGGCCCGGACTTGCCTAGAACGCTGAATTACTTAAACTACGTGAGCCACTTAAACTAATCACTGATGCCGAGTAGGCAGTGCATCTACGATATCATTTGAGGCAGAAATC"

def get_substrings(x):
    for i, j in itertools.combinations(xrange(len(x)+1), 2):
        yield x[i:j]

def similar_check(s1, s2):
    penalty = 0
    for i, j in enumerate(s1):
        if s2[i] != j:
            penalty += 1
        if penalty == 5:
            return False
    return True


def tandem(string): # Check for tandem repeats that exactly match
    max_string = SequenceMatcher(None, "A", "A", autojunk=False).find_longest_match(0, len("A"), 0, len("A"))
    for position in range(len(string)):
        string1 = string[:position]
        string2 = string[position:]
        match = SequenceMatcher(None, string1, string2, autojunk=False).find_longest_match(0, len(string1), 0, len(string2))
        if match.size > max_string.size:
            max_string = match
    print(max_string)
    print(string[int(max_string.a):int(max_string.a+max_string.size)])

tandem(seq)

#for line in file.readlines():
#    if not line.startswith(">")
#        s = line.replace("\n","").replace("\r","")
#        tandem(s)
#
#for item in solutions:
#    print(item)

