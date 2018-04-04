from snakemake import shell

shell('source activate peakerror; '
       'Rscript peakerror/PeakError_summarize.R '
       '{snakemake.output.macs2_q} &> {snakemake.output.summary}')
