file = open("/Users/syedather/Downloads/input2.txt", "r")

solutions = []

rna = ["A", "C", "G", "U"]
numbers = "1234567890"

aa_bank = {
    "UUU":"Phe",
    "UUC":"Phe",
    "UUA":"Leu",
    "UUG":"Leu",
    "UCU":"Ser",
    "UCC":"Ser",
    "UCA":"Ser",
    "UCG":"Ser",
    "UAU":"Tyr",
    "UAC":"Tyr",
    "UAA":" *",
    "UAG":" *",
    "UGU":"Cys",
    "UGC":"Cys",
    "UGA":" *" ,
    "UGG":"Trp",
    "CUU":"Leu",
    "CUC":"Leu",
    "CUA":"Leu",
    "CUG":"Leu",
    "CCU":"Pro",
    "CCC":"Pro",
    "CCA":"Pro",
    "CCG":"Pro",
    "CAU":"His",
    "CAC":"His",
    "CAA":"Gln",
    "CAG":"Gln",
    "CGU":"Arg",
    "CGC":"Arg",
    "CGA":"Arg",
    "CGG":"Arg",
    "AUU":"Ile",
    "AUC":"Ile",
    "AUA":"Ile",
    "AUG":"Met",
    "ACU":"Thr",
    "ACC":"Thr",
    "ACA":"Thr",
    "ACG":"Thr",
    "AAU":"Asn",
    "AAC":"Asn",
    "AAA":"Lys",
    "AAG":"Lys",
    "AGU":"Ser",
    "AGC":"Ser",
    "AGA":"Arg",
    "AGG":"Arg",
    "GUU":"Val",
    "GUC":"Val",
    "GUA":"Val",
    "GUG":"Val",
    "GCU":"Ala",
    "GCC":"Ala",
    "GCA":"Ala",
    "GCG":"Ala",
    "GAU":"Asp",
    "GAC":"Asp" ,
    "GAA":"Glu",
    "GAG":"Glu",
    "GGU":"Gly",
    "GGC":"Gly",
    "GGA":"Gly",
    "GGG":"Gly"}

def change(rna_string, intervals):
    for interval in intervals:
        start = interval[0]
        end = interval[1]
        aa = []
        rna_substring = ""
        for i in range(start, end):
            rna_substring += rna_string[i]
            if rna_substring in aa_bank:
                aa.append(aa_bank[rna_substring])
                rna_substring = ""
    print(aa)

count = 0
for line in file.readlines():
    if line[0] in rna and intervals != []:
        change(rna_string,intervals)
        rna_string = line.replace("\n", "").replace("\r","")
        intervals = []
    if count > 0 and line[0] in numbers and len(line.split()) > 1:
        token = line.split(" ")
        intervals.append(list((token[0], token[1])))
    count += 1

for item in solutions:
    print(item)

