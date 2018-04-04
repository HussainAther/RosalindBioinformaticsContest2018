import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"
o = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid9.png"
o2 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid10.png"
o3 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid11.png"
o4 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid12.png"
o5 = "/data/Lei_student/Hussain/ML/dm6/peakerror/facetgrid/facetgrid13.png"
df = pd.DataFrame.from_csv(f)

sns.set(font_scale=1.5)

def errorbar(x, y, low, high, order, color, **kws):
    xnum = [order.index(x_i) for x_i in x]
    plt.errorbar(xnum, y, (y - low, high - y), color=color)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x='q_value', y='mcc', data=df, col='antibody', legend=True, col_order=df.groupby('antibody')['mcc'].agg(np.mean).sort_values().index, hue='celltype')
x.set_ylabels("MCC")
x.savefig(o)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x='slocal', y='mcc', data=df, col='antibody', legend=True, col_order=df.groupby('antibody')['mcc'].agg(np.mean).sort_values().index, hue='celltype')
x.set_ylabels("MCC")
x.savefig(o2)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x='llocal', y='mcc', data=df, col='antibody', legend=True, col_order=df.groupby('antibody')['mcc'].agg(np.mean).sort_values().index, hue='celltype')
x.set_ylabels("MCC")
x.savefig(o3)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x='highmfold', y='mcc', data=df, col='antibody', legend=True, col_order=df.groupby('antibody')['mcc'].agg(np.mean).sort_values().index, hue='celltype')
x.set_ylabels("MCC")
x.savefig(o4)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
x = sns.factorplot(x='lowmfold', y='mcc', data=df, col='antibody', legend=True, col_order=df.groupby('antibody')['mcc'].agg(np.mean).sort_values().index, hue='celltype')
x.set_ylabels("MCC")
x.savefig(o5)
