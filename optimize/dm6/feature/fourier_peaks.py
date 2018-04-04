import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
import numpy as np
import pyBigWig
import sys
import inspect
import re
import os
import ntpath

# Signal processing metrics
# Use plt.specgram to look at the read coverage distributions. That should give us the autocorrelation profiles 
# to use Fourier Transform on. Let's look over the peak regions.

if len(sys.argv) != 3:
    raise ValueError("Usage: python fourier.py coverage.bw optimal_sample.csv output.tsv")
inp = sys.argv[1] # Input bigWig file of the read coverage
opt = sys.argv[2] # csv of optimal parameter combinations by sample
out = sys.argv[3] # Output png of the fourier spectrogram

sample_name = os.path.splitext(ntpath.basename(inp))[0]

def varname(p): # Return a variable name
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            return m.group(1)

# Find optimal bedfile for each sample

opt_df = pd.DataFrame.from_csv(opt)

if len(opt_df.loc[opt_df["sample"] == sample_name]) > 1:
    opt_line = opt_df.loc[opt_df["sample"] == sample_name][0] # Find the optimal parameter combinations for the given sample
else:
    opt_line = opt_df.loc[opt_df["sample"] == sample_name]

slocal = opt_line["slocal"]
llocal = opt_line["llocal"]
nolambda = opt_line["nolambda"]
downsample = opt_line["downsample"]
tolarge = opt_line["tolarge"]
highmfold = opt_line["highmfold"]
lowmfold = opt_line["lowmfold"]
q_value = opt_line["q_value"]

bedfile = "peak_out/macs2/" + sample_name + "/q_value_" + q_value + "/llocal_" + llocal + "/slocal_" + slocal + "/lowmfold_" + lowmfold + "/highmfold_" + highmfold + "/" + nolambda + "/" + downsample + "/" + tolarge + "/" + sample_name + "_peaks.narrowPeak" 

# Find the peaks for that bedfile
chr2L_peaks, chr2R_peaks, chr3L_peaks, chr3R_peaks = [], [], [], [] # Regions of peaks that we'll get from the optimal MCC combination 
# Each value should be a list in which the first value is the peak start and the second is the peak end.

with open(bedfile, "r") as file:
    for line in file:
        token = line.split("\t")
        chr = token[0]
        if chr == "chr2L":
            chr2L_peaks.append(list(token[1], token[2]))
        elif chr == "chr3L":
            chr3L_peaks.append(list(token[1], token[2]))
        elif chr == "chr3R":
            chr3R_peaks.append(list(token[1], token[2]))
        elif chr == "chr2R":
            chr2R_peaks.append(list(token[1], token[2]))

chr_list = ["chr2L", "chr2R", "chr3L", "chr3R"]

# Find the spectrograms at those areas
bw = pyBigWig.open(inp)

fs = 10e3 # Sampling frequency

Sxx = [] # Spectrogram of s
f = [] # Sample frequency values at each point
t = [] # Segment times
sample_list = [] # list of sample name

# Now go through each list of peaks and append the spectrogram values for those peaks
for peak in chr2L_peaks: 
    f.append(signal.spectrogram(np.array(bw.values("chr2L", peak[0], peak[1]), fs))[0])
    t.append(signal.spectrogram(np.array(bw.values("chr2L", peak[0], peak[1]), fs))[1])
    Sxx.append(signal.spectrogram(np.array(bw.values("chr2L", peak[0], peak[1]), fs))[2])
    sample_list.append(sample_name)

for peak in chr2R_peaks: 
    f.append(signal.spectrogram(np.array(bw.values("chr2R", peak[0], peak[1]), fs))[0])
    t.append(signal.spectrogram(np.array(bw.values("chr2R", peak[0], peak[1]), fs))[1])
    Sxx.append(signal.spectrogram(np.array(bw.values("chr2R", peak[0], peak[1]), fs))[2])
    sample_list.append(sample_name)

for peak in chr3L_peaks: 
    f.append(signal.spectrogram(np.array(bw.values("chr3L", peak[0], peak[1]), fs))[0])
    t.append(signal.spectrogram(np.array(bw.values("chr3L", peak[0], peak[1]), fs))[1])
    Sxx.append(signal.spectrogram(np.array(bw.values("chr3L", peak[0], peak[1]), fs))[2])
    sample_list.append(sample_name)

for peak in chr3R_peaks: 
    f.append(signal.spectrogram(np.array(bw.values("chr3R", peak[0], peak[1]), fs))[0])
    t.append(signal.spectrogram(np.array(bw.values("chr3R", peak[0], peak[1]), fs))[1])
    Sxx.append(signal.spectrogram(np.array(bw.values("chr3R", peak[0], peak[1]), fs))[2])
    sample_list.append(sample_name)

labels = ["frequencies", "times", "spectrogram", "sample"]

spec_df = pd.DataFrame.from_records([f, t, Sxx, sample_list], columns=labels)

tsv = pd.DataFrame.to_csv(spec_df, sep="\t")

with open(out, "w") as file:
    file.write(tsv)
