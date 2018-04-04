from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import sys
import pysam
import os
import numpy as np
import matplotlib.pyplot as plt

# bam = {snakemake.input.bam}
bam = "/data/Lei_student/Hussain/ML/dm6/peakerror/bam/SRR567586.bam"

if len(sys.argv) != 3:
    raise ValueError("Usage: python randomforestclassifier.py mapped_reads.bam output.tsv")
inp = sys.argv[1] # Input bam file of the mapped reads
out = sys.argv[2]

X, y = make_classification(n_samples=1000, n_features=4,
                            n_informative=2, n_redundant=0,
                            random_state=0, shuffle=False)
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)
forest = ExtraTreesClassifier(n_estimate=250, random_state=0)

forest.fit(X, y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
                     axis=0)
indices = np.argsort(importances)[::-1]
