from scipy.stats import norm
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

np.seterr(divide='ignore', invalid='ignore')

# Plot the frequency (or number of occurances) 
# of each MCC to get an idea of how wide/narrow the distribution is.

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"

df = pd.DataFrame.from_csv(f)

sample_list = df["sample"].unique()
df["ca"] = df["celltype"] + df["antibody"]
ca_list = df["ca"].unique()

def hist(sample, values, output, vline):
    plt.figure()
    # best fit of data
    (mu, sigma) = norm.fit(values)

    # the histogram of the data
    n, bins, patches = plt.hist(values, 60, normed=1, facecolor='green', alpha=0.75)
    # add a 'best fit' line
#    y = mlab.normpdf(bins, mu, sigma)
#    l = plt.plot(bins, y, 'r--', linewidth=2)

    if vline:
        default = df.loc[(df["params"] == "no-ds50100005no-nl0.051000") & (df["sample"] == sample)]["mcc"].values[0]
        plt.axvline(x=default, linewidth=4, color="r")

    # plot
    plt.xlabel('MCC')
    plt.ylabel('Frequency')
    plt.title("Histogram of MCC for %s:"%(sample) + r'$\mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
    plt.grid(True)
    plt.savefig(output)
    plt.close()

for sample in sample_list:
    mcc = df.loc[df["sample"] == sample]["mcc"]
    o = "/data/Lei_student/Hussain/ML/dm6/peakerror/frequency/mcc_frequency_" + str(sample) + ".png"
    hist(sample, mcc, o, True)

for ca in ca_list:
    mcc = df.loc[df["ca"] == ca]["mcc"]
    o = "/data/Lei_student/Hussain/ML/dm6/peakerror/frequency/mcc_frequency_" + str(ca) + ".png"
    hist(ca, mcc, o, False)

mcc = df["mcc"]
o = "/data/Lei_student/Hussain/ML/dm6/peakerror/frequency/mcc_frequency.png"
hist("all samples", mcc, o, False)
