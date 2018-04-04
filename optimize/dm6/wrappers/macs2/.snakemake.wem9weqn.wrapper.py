
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X8\x00\x00\x00peak_out/macs2/lm06_kc_shep-gp_R1/lm06_kc_shep-gp_R1.bedq\x06XE\x00\x00\x00peak_out/macs2/lm06_kc_shep-gp_R1/lm06_kc_shep-gp_R1_peaks.narrowPeakq\x07e}q\x08(X\x03\x00\x00\x00bedq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\n\x00\x00\x00narrowPeakq\rK\x01N\x86q\x0euh\rh\x07ubX\x06\x00\x00\x00configq\x0f}q\x10X\x07\x00\x00\x00threadsq\x11K\x01X\x06\x00\x00\x00paramsq\x12csnakemake.io\nParams\nq\x13)\x81q\x14(X!\x00\x00\x00peak_out/macs2/lm06_kc_shep-gp_R1q\x15X\x12\x00\x00\x00lm06_kc_shep-gp_R1q\x16e}q\x17(X\x06\x00\x00\x00prefixq\x18h\x15h\n}q\x19(X\x0e\x00\x00\x00wrapper_sampleq\x1aK\x01N\x86q\x1bh\x18K\x00N\x86q\x1cuh\x1ah\x16ubX\t\x00\x00\x00wildcardsq\x1dcsnakemake.io\nWildcards\nq\x1e)\x81q\x1fh\x16a}q (h\n}q!X\x06\x00\x00\x00sampleq"K\x00N\x86q#sX\x06\x00\x00\x00sampleq$h\x16ubX\t\x00\x00\x00resourcesq%csnakemake.io\nResources\nq&)\x81q\'(K\x01K\x01e}q((X\x06\x00\x00\x00_nodesq)K\x01h\n}q*(X\x06\x00\x00\x00_coresq+K\x00N\x86q,h)K\x01N\x86q-uh+K\x01ubX\x05\x00\x00\x00inputq.csnakemake.io\nInputFiles\nq/)\x81q0(X\x1c\x00\x00\x00dedup/lm06_kc_shep-gp_R1.bamq1X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq2e}q3(X\x02\x00\x00\x00ipq4h1X\x03\x00\x00\x00inpq5h2h\n}q6(h4K\x00N\x86q7h5K\x01N\x86q8uubX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\n}q=sbX\x04\x00\x00\x00ruleq>X\x05\x00\x00\x00macs2q?ub.')
######## Original script #########
from snakemake.shell import shell

shell(
    'macs2 '
    'callpeak '
    '-c {snakemake.input.inp} '
    '-t {snakemake.input.ip} '
    '--bdg --SPMR '
    '-n {snakemake.wildcards.sample} '
    '--outdir {snakemake.params.prefix}'
)
shell('Rscript {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.r')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
