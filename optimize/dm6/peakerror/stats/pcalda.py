import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"
o = "/data/Lei_student/Hussain/ML/dm6/peakerror/pca.png"
# o2 = "/data/Lei_student/Hussain/ML/dm6/peakerror/lda.png"

df = pd.DataFrame.from_csv(f)

X = np.array(df[["q_value", "slocal", "llocal", "lowmfold", "highmfold"]])
y = np.array(df["mcc"])

target_names = df["sample"].unique()

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# lda = LinearDiscriminantAnalysis(n_components=2)
# X_r2 = lda.fit(X, y).transform(X)

print('explained variance ratio (first two components): %s'
    % str(pca.explained_variance_ratio_))

colors = ['navy', 'turquoise', 'darkorange', 'silver', 
    'black', 'red', 'maroon', 'yellow', 
    'olive', 'lime', 'green', 'aqua', 
    'teal', 'blue', 'cyan', 'blue',
    'fuchsia', 'purple', 'salmon', 'lightsalmon']
lw = 2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
for color, i, target_name in zip(colors, range(20), target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=.8, lw=lw,
    label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('Pincipal Component Analysis')

plt.savefig(o)

# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111)
# for color, i, target_name in zip(colors, [0, 1, 2], target_names):
#     plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=.8, color=color,
#     label=target_name)
# plt.legend(loc='best', shadow=False, scatterpoints=1)
# plt.title('Linear Discriminant Analysis')

# plt.savefig(o2)
