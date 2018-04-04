import matplotlib.pyplot as plt
import pandas as pd
import pybedtools
import ntpath
import sys
import os

if len(sys.argv) != 4:
    raise ValueError("Usage: python PeakError.py peaks.bed labels.bed errors.bed")
peaks = sys.argv[1] # Input peaks bed file
labels = sys.argv[2] # Input labels bed file
output = sys.argv[3] # Output bed file

errors = [] # List of dictionaries that will be the output

label_dict = {} 

chr = os.path.splitext(ntpath.basename(labels))[0][:5] # Get the chromosome from the labels name

peak_bedtool = pybedtools.BedTool(peaks) # Use pybedtools to intersect the peaks and labels
label_bedtool = pybedtools.BedTool(labels) # vice versa

intersecting_labels = label_bedtool.intersect(peak_bedtool, wa=True, u=True)
intersecting_peaks = peak_bedtool.intersect(label_bedtool, wa=True, u=True)
non_intersecting_labels = label_bedtool.intersect(peak_bedtool, wa=True, v=True)

with open(labels, "r") as file: # Create a dictionary of labels with the key = label start and end, value = label
    for line in file:
        token = line.split("\t")
        start = token[1]
        end = token[2] 
        label = token[3].replace("\n", "")
        label_dict[str(start)+"_"+str(end)] = label

prev_label_end = 0

def temp_dict_add(chr, label_start, label_end, status, peak_start, prev_label_end):
    temp_dict = {}
    temp_dict["chr"] = chr
    temp_dict["chromStart"] = label_start
    temp_dict["chromEnd"] = label_end
    if int(peak_start) < int(prev_label_end): # This accounts for the exceptions in which one peak overlaps two different labels
        prev_label = [entry for entry in errors if entry["chromEnd"] == prev_label_end]
        if status == "true positive" and prev_label[0]["status"] == "false positive":
            [entry for entry in errors if entry["chromEnd"] == prev_label_end][0]["status"] = "none"
        elif status == "false positive" and prev_label[0]["status"] == "true positive":
            status = "none"
    temp_dict["status"] = status
    prev_label_end = label_end
    return temp_dict, prev_label_end

def get_status(peak_start, peak_end, label, label_start, label_end):
    if peak_start >= label_start and peak_end <= label_end: # the peak is within the label
        if label_dict[label] == "noPeaks":
            return "false positive"
        elif label_dict[label] == "peaks" or label_dict[label] == "peakStart" or label_dict[label] == "peakEnd":
            return "true positive"
    elif peak_start < label_start and peak_end <= label_end and peak_end > label_start: # the end of the peak overlaps with the label
        if label_dict[label] == "noPeaks" or label_dict[label] == "peakStart":
            return "false positive"
        elif label_dict[label] == "peaks" or label_dict[label] == "peakEnd":
            return "true positive"
    elif peak_start > label_start and peak_end > label_end and peak_start < label_end: # the start of the peak overlaps with the label
        if label_dict[label] == "noPeaks" or label_dict[label] == "peakEnd":
            return "false positive"
        elif label_dict[label] == "peaks" or label_dict[label] == "peakStart":
            return "true positive"
    elif peak_start <= label_start and peak_end >= label_end: # the label is within the peak
        if label_dict[label] == "noPeaks":
            return "false positive"
        elif label_dict[label] == "peaks" or label_dict[label] == "peakStart" or label_dict[label] == "peakEnd":
            return "true positive"
    return "none"

for label in non_intersecting_labels: # Search the non-overlapping labels for true negatives and false negatives
    label_start = label[1]
    label_end = label[2]
    label_key = label_start + "_" + label_end
    if label_dict[label_key] == "noPeaks":
        temp_dict, prev_label_end = temp_dict_add(chr, label_start, label_end, "true negative", label_start, prev_label_end)
    else:
        temp_dict, prev_label_end = temp_dict_add(chr, label_start, label_end, "false negative", label_start, prev_label_end)
    errors.append(temp_dict) 

for label in intersecting_labels: # Search the overlapping labels for true positives and false positives
    label_start = label[1]
    label_end = label[2]
    label_key = label_start + "_" + label_end
    for peak in intersecting_peaks:
        peak_start = peak[1]
        peak_end = peak[2]
        status = get_status(peak_start, peak_end, label_key, label_start, label_end)
        if status != "none":
            temp_dict, prev_label_end = temp_dict_add(chr, label_start, label_end, status, peak_start, prev_label_end)
            errors.append(temp_dict)
            break

result = pd.DataFrame(errors) # Convert the list of dictionaries to a DataFrame

tsv = pd.DataFrame.to_csv(result, sep="\t") # Convert the DataFrame to a tsv

with open(output, "w") as file: # Output the tsv
    file.write(tsv)
