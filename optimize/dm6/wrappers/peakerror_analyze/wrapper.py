from matplotlib.colors import LogNorm
from matplotlib.mlab import bivariate_normal
from snakemake.shell import shell
import matplotlib
matplotlib.use('Agg')
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import math
import pylab

# This file will look at the output 
# from the peak error results and create a dataframe
# that can be used to figure out optimal values by sample

metadata=pd.read_csv('config/metadata.tsv',header=0,sep='\t')
metadata=metadata+"_R1"
temp_dict=pd.DataFrame.to_dict(metadata,orient='list')
d=dict(zip(temp_dict['ip'],temp_dict['input']))
d["SRR567586"]="SRR567585"
d["dc92_bg3_ctcf-56"] = "dc91_bg3_input"
d["dc94_bg3_ctcf-59"] = "dc93_bg3_input"

sample_id = []
celltype = []
antibody = []

for sample in d:
    sample_id.append(sample)

def mcc(tp, tn, fp, fn): #calculate the matthews correlation coefficient, measures the quality of binary classifications
    num = tp*tn - fp*fn # tp = true positive, tn = true negative, fp = false positive, fn = false negative
    dem = math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
    if dem == 0:
        dem = 1
    return num/dem

# iterate through each peakerror output file and keep track of the tp, tn, fp, fn, and mcc for each parameter
# I need to re-write this using pandas to create a dataframe that can be easily converted to a .tsv

# Create a list of dictionaries with each key as the parameter (header row of output table) 
# and each value as the list of mcc values (each column of the table). then output that list
# to a dataframe and convert the dataframe to a .tsv

#stats = {
#    "sample" : ["sample"],
#    "celltype": ["celltype"],
#    "antibody": ["antibody"],
#    "q_value" : ["q_value"], 
#    "llocal" : ["llocal"],
#    "slocal" : ["slocal"],
#    "lowmfold" : ["lowmfold"],
#    "highmfold" : ["highmfold"],
#    "downsample" : ["downsample"],
#    "nolambda" : ["nolambda"],
#    "mcc" : ["mcc"]
#    }

stats = []

# use python glob for debugging

for file in snakemake.input:
    temp_dict = {}
    f = open(file, "r")
    if "cp190" in file:
        temp_dict["antibody"] = "cp190"
    elif "ctcf" in file:
        temp_dict["antibody"] = "ctcf"
    elif "mod" in file:
        temp_dict["antibody"] = "mod"
    elif "rm62" in file:
        temp_dict["antibody"] = "rm62"
    elif "rump" in file:
        temp_dict["antibody"] = "rump"
    elif "shep" in file:
        temp_dict["antibody"] = "shep"
    elif "suhw" in file:
        temp_dict["antibody"] = "suhw"
    elif "SRR" in file:
        temp_dict["antibody"] = "suhw" 
    sample = file.split("/")[2]
    temp_dict["sample"] = sample
    if sample != "SRR567586":
        temp_dict["celltype"] = sample.split("_")[1]
    else: 
        temp_dict["celltype"] = "bg3"
    temp_dict["q_value"] = file.split("/")[3].split("_")[2]
    temp_dict["llocal"] = file.split("/")[4].split("_")[1]
    temp_dict["slocal"] = file.split("/")[5].split("_")[1]
    temp_dict["lowmfold"] = file.split("/")[6].split("_")[1]
    temp_dict["highmfold"] = file.split("/")[7].split("_")[1]
    temp_dict["nolambda"] = file.split("/")[8]
    temp_dict["downsample"] = file.split("/")[9]
    fp = 0
    fn = 0 
    tp = 0
    tn = 0
    none = 0
    for lineno, line in enumerate(f):
        toks = line.strip().split("\t")
        if toks[0] in ("chr2R", "chr2L", "chr3R", "chr3L"):
            if "true positive" in line:
                tp += 1
            elif "false negative" in line:
                fn += 1
            elif "false positive" in line:
                fp += 1
            elif "true negative" in line or ("noPeaks" in line and "correct" in line):
                tn +=1
            elif "none" in line:
                none += 1
    temp_dict["tp"] = tp
    temp_dict["tn"] = tn
    temp_dict["fp"] = fp
    temp_dict["fn"] = fn
    temp_dict["none"] = none
    temp_dict["mcc"] = mcc(tp, tn, fp, fn)
    temp_dict["accuracy"] = (tp + tn) / (tp + tn + fp + fn)
    temp_dict["mcc"] = mcc(tp, tn, fp, fn)
    temp_dict["params"]=(str(ds+highmfold+llocal+lowmfold+nolambda+qvalue+slocal))
    stats.append(temp_dict)

dataframe = pd.DataFrame(stats)

tsv = pd.DataFrame.to_csv(dataframe, sep="\t")

with open(str(snakemake.output), "w") as file:
    file.write(tsv)
