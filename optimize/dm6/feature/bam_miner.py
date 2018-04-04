import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
import ntpath
import sys
import pysam
import os

# Re-implementing COPAR Miner in python

if len(sys.argv) != 3:
    raise ValueError("Usage: python bam_miner.py mapped_reads.bam output.tsv")
inp = sys.argv[1] # Input bam file of the mapped reads
out = sys.argv[2]

sample_name = os.path.splitext(ntpath.basename(snakemake.input))[0] # Get the sample name from the filename

def bam_to_df(bam, chr = None, start=None, stop = None): # Convert an input bam file to a pandas DataFrame
    sample = []
    seq = []
    qname = []
    pos = []
    flag = []
    mapq = []
    cigar = []
    qual = []
    for read in bam.fetch(chr, start, stop):
        sample.append(sample_name)
        seq.append(read.seq)
        qname.append(read.qname)
        pos.append(read.pos)
        flag.append(read.flag)
        mapq.append(read.mapq)
        cigar.append(read.cigar)
        qual.append(read.qual)
    return pd.DataFrame({'sample': sample, 'seq': seq, 'qname': qname, 'pos': pos, 'flag': flag, 'mapq': mapq, 'cigar': cigar, 'qual':qual})

with pysam.AlignmentFile(inp, 'rb') as myfile:
    df = bam_to_df(myfile)

tsv = pd.DataFrame.to_csv(df, sep="\t")

with open(out, "w") as file:
    file.write(tsv)
