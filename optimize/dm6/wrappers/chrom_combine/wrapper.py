from snakemake import shell

shell('cat {snakemake.input} > {snakemake.output}')
