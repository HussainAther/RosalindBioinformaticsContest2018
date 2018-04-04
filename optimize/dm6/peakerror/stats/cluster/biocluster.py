import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import Bio.Cluster as bc

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"
o = "/data/Lei_student/Hussain/ML/dm6/peakerror/cluster_out.png"

df = pd.read_csv(f)
data = df[["mcc", "q_value"]]

matrix = bc.distancematrix(data)
cdata, cmask = bc.clustercentroids(data)
distance = bc.clusterdistance(data)
tree = bc.treecluster(data)

print(matrix)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC distance matrix")
plt.scatter(range(45000), matrix)
plt.savefig(o)
