from snakemake import shell

shell("bedtools intersect -wa -wb \
        -a {snakemake.input.default} \
        -b {snakemake.input.combinations} \
        -sorted -names > {snakemake.output}")
