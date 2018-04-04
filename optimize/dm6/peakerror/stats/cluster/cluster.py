import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"
o = "/data/Lei_student/Hussain/ML/dm6/peakerror/qvalue_maxmcc.png"

df = pd.read_csv(f)

def CompareVecs(target,vecs):
    """Returns the differences between the targets and the vectors"""
    diffs=abs(target-vecs)
    scores=diffs.sum(1)
    return scores

def AssignMembership(clusts,data):
    """Returns the cluster membership for each data point"""
    NC = len(clusts)
    mmb = []
    for i in range(NC):
        sc=np.zeros(NC)
        for j in range(NC):
            sc[j] = np.sqrt(((clusts[j]-data[i])**2).sum())
        mn = sc.argmin()
        mmb[mn].append(i)
    return mmb

def ClusterAverage(mmb, data):
    """Returns the average from the data"""
    K = len(mmb)
    N = len(data[0])
    clusts = np.zeros((K,N),float)
    for i in range(K):
        vecs = data.take(mmb[i],0)
        clusts[i] = vecs.mean(0)
    return clusts

data = df[["mcc", "q_value"]]

scores = CompareVecs(df["mcc"].max(),data)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("Distance to max mcc of q_value")
plt.scatter(range(45000), scores)
#ax.set_xlabel("order")
ax.set_ylabel("scores")
plt.savefig(o)
