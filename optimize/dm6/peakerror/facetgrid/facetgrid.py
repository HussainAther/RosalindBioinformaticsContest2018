import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"
o1 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid1.png"
o2 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid2.png"
o3 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid3.png"
o4 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid4.png"
o5 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid5.png"
o6 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid6.png"
o7 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid7.png"
o8 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid8.png"
d = pd.DataFrame.from_csv(f)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x="q_value", y="mcc", data=d, col="antibody", row="slocal", hue="downsample", legend=True)
x.set_xticklabels([".0135", ".0271", ".0406"])
x.savefig(o1)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x="q_value", y="mcc", data=d, col="antibody", row="llocal", hue="downsample", legend=True)
x.set_xticklabels([".0135", ".0271", ".0406"])
x.savefig(o2)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x="q_value", y="mcc", data=d, col="highmfold", row="lowmfold", hue="downsample", legend=True)
x.set_xticklabels([".0135", ".0271", ".0406"])
x.savefig(o3)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x="q_value", y="mcc", data=d, col="antibody", row="highmfold", hue="downsample", legend=True)
x.set_xticklabels([".0135", ".0271", ".0406"])
x.savefig(o4)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x="q_value", y="mcc", data=d, col="antibody", row="celltype", hue="downsample", legend=True)
x.set_xticklabels([".0135", ".0271", ".0406"])
x.savefig(o5)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x="highmfold", y="mcc", data=d, col="antibody", row="lowmfold", hue="downsample", legend=True)
x.savefig(o6)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x="highmfold", y="mcc", data=d, col="antibody", row="celltype", hue="downsample", legend=True)
x.savefig(o7)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x="lowmfold", y="mcc", data=d, col="antibody", row="q_value", hue="downsample", legend=True)
x.savefig(o8)

