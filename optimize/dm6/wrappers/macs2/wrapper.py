from snakemake.shell import shell

downsample = {"ds" : "--down-sample", "no-ds" : ""}

if snakemake.params.downsample == "ds":
    downsample_value = "--down-sample"
elif snakemake.params.downsample == "no-ds":
    downsample_value = ""
else:
    raise ValueError("downsample error")

if snakemake.params.nolambda == "nl":
    nolambda_value = "--down-sample"
elif snakemake.params.nolambda == "no-nl":
    nolambda_value = ""
else:
    raise ValueError("nolambda error")

if snakemake.params.tolarge == "tl":
    tolarge_value = "--to-large"
elif snakemake.params.tolarge == "no-tl":
    tolarge_value = ""
else:
    raise ValueError("tolarge error")

shell(
    'macs2 '
    'callpeak '
    '-c {snakemake.input.inp} '
    '-t {snakemake.input.ip} '
    '-q {snakemake.params.q_val} '
    '--llocal {snakemake.params.llocal} '
    '--slocal {snakemake.params.slocal} '
    '-m {snakemake.params.lowmfold} {snakemake.params.highmfold} '
    '{downsample_value} '
    '{nolambda_value} '
    '{tolarge_value} '
    '-n {snakemake.wildcards.sample} '
    '--outdir {snakemake.params.outdir_prefix}'
)
#shell('Rscript {snakemake.params.sample_prefix}_model.r')
#shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
#shell("cd {snakemake.params.qval_prefix} && ln -sf $(basename {snakemake.output.narrowPeak}) $(basename {snakemake.output.bed})")

