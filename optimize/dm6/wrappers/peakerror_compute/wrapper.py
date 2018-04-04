from snakemake import shell

for sample in snakemake.input:
    if "kc_cp190" in sample:
        shell("Rscript peakerror/PeakError_compute.R {snakemake.params.sample} {snakemake.params.kc_cp190labels} > {snakemake.output}")
    if "kc_suhw" in sample:
        shell("Rscript peakerror/PeakError_compute.R {snakemake.params.sample} {snakemake.params.kc_suhwlabels} > {snakemake.output}")
    if "kc_shep" in sample:
        shell("Rscript peakerror/PeakError_compute.R {snakemake.params.sample} {snakemake.params.kc_sheplabels} > {snakemake.output}")
    if "bg3_shep" in sample:
        shell("Rscript peakerror/PeakError_compute.R {snakemake.params.sample} {snakemake.params.bg3_sheplabels} > {snakemake.output}")
    if "bg3_mod" in sample:
        shell("Rscript peakerror/PeakError_compute.R {snakemake.params.sample} {snakemake.params.bg3_modlabels} > {snakemake.output}")
    if "kc_mod" in sample:
        shell("Rscript peakerror/PeakError_compute.R {snakemake.params.sample} {snakemake.params.kc_modlabels} > {snakemake.output}")
    if "bg3_ctcf" in sample:
        shell("Rscript peakerror/PeakError_compute.R {snakemake.params.sample} {snakemake.params.bg3_ctcflabels} > {snakemake.output}")
    if "bg3_suhw" in sample:
        shell("Rscript peakerror/PeakError_compute.R {snakemake.params.sample} {snakemake.params.bg3_suhwlabels} > {snakemake.output}")
