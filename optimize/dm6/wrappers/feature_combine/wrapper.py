from snakemake import shell
import ntpath
import pandas as pd

# Create lists of dictionaries that will serve as the output.

forest_feature = []
svm_feature = []

# Create DataFrames from input files.

for counts_table in snakemake.input.fingerprint_counts:
    sample_name = os.path.splitext(ntpath.basename(counts_table))[0]
    fingerprint_df = pd.DataFrame.read_table(counts_table)

for counts_table in snakemake.input.qc:
    sample_name = os.path.splitext(ntpath.basename(counts_table))[0]
    qc_df = pd.DataFrame.read_table(counts_table)

spec_df = pd.DataFrame()
for spec_tsv in snakemake.input.spec:
    spec_df = pd.concat([spec_df, pd.DataFrame.from_csv(spec_tsv, sep="\t")])

multiqc_df = pd.DataFrame.from_csv(snakemake.input.multiqc, sep="\t")

cc_df = pd.DataFrame.from_csv(snakemake.input.cross_correlation, sep="\t")

filesize_df = pd.DataFrame.from_csv(snakemake.input.filesize)

# From these DataFrames, add values to the lists of dictionaries.

temp_dict = {}




# Convert the lists of dictionaries to DataFrames

forest_df = pd.DataFrame(forest_feature)
svm_df = pd.DataFrame(svm_feature)

forest_csv = pd.DataFrame.to_csv(forest_df)
svm_csv = pd.DataFrame.to_csv(svm_df)

with open(str(snakemake.output.forest_input), "w") as file:
    file.write(forest_csv)

with open(str(snakemake.output.svm_input), "w") as file:
    file.write(svm_csv)
