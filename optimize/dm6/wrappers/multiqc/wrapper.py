from snakemake import shell

# MultiQC uses Click, which in turn complains if C.UTF-8 is not set
# with utils.temp_env(dict(LC_ALL='en_US.UTF-8', LC_LANG='en_US.UTF-8')) as env:
shell(
    'multiqc '
    '{snakemake.input.fastqc} '
    '{snakemake.input.markduplicates} '
    '--quiet '
    '--outdir {snakemake.output} '
    '--force '
)


