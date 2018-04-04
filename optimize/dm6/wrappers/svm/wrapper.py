from snakemake import shell
from sklearn import svm
import numpy as np
import pandas as pd

X = [[0,0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)

X = [[0,0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)

