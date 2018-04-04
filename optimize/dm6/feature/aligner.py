import matplotlib.pyplot as plt
import pandas as pd
import pybedtools
import ntpath
import sys
import os

# Re-implementing COPAR Aligner in python
# All copar.Aligner does is that it aligns the 
# input bam file to a reference genome. I don't need to write a python script to do that.

if len(sys.argv) != 6:
    raise ValueError("Usage: python aligner.py input.bed reference_genome windows_size p-value_threshold output")
bf = sys.argv[1] # Input bed file that is the ChIP-Seq input
rg = sys.argv[2] # reference genome (e.g., mm9, dm6, hg18, hg19, etc.)
ws = str(sys.argv[3]) # windows size (e.g., 100, 150, 200, etc.)
pv = str(sys.argv[4]) # p-value threshold (e.g., 0.951, 0.954, etc.)
otf = sys.argv[5] # output file 



