
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05(X\r\x00\x00\x00sjl_s2_mod_R1q\x06X\x1c\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1q\x07e}q\x08(X\x0e\x00\x00\x00wrapper_sampleq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\x06\x00\x00\x00prefixq\rK\x01N\x86q\x0euh\rh\x07ubX\x06\x00\x00\x00configq\x0f}q\x10X\x03\x00\x00\x00logq\x11csnakemake.io\nLog\nq\x12)\x81q\x13}q\x14h\n}q\x15sbX\x04\x00\x00\x00ruleq\x16X\x05\x00\x00\x00macs2q\x17X\x06\x00\x00\x00outputq\x18csnakemake.io\nOutputFiles\nq\x19)\x81q\x1a(X;\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1_peaks.narrowPeakq\x1bX.\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1.bedq\x1ce}q\x1d(X\n\x00\x00\x00narrowPeakq\x1eh\x1bh\n}q\x1f(h\x1eK\x00N\x86q X\x03\x00\x00\x00bedq!K\x01N\x86q"uh!h\x1cubX\x07\x00\x00\x00threadsq#K\x01X\x05\x00\x00\x00inputq$csnakemake.io\nInputFiles\nq%)\x81q&(X\x17\x00\x00\x00dedup/sjl_s2_mod_R1.bamq\'X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq(e}q)(X\x02\x00\x00\x00ipq*h\'h\n}q+(h*K\x00N\x86q,X\x03\x00\x00\x00inpq-K\x01N\x86q.uh-h(ubX\t\x00\x00\x00wildcardsq/csnakemake.io\nWildcards\nq0)\x81q1h\x06a}q2(h\n}q3X\x06\x00\x00\x00sampleq4K\x00N\x86q5sX\x06\x00\x00\x00sampleq6h\x06ubX\t\x00\x00\x00resourcesq7csnakemake.io\nResources\nq8)\x81q9(K\x01K\x01e}q:(h\n}q;(X\x06\x00\x00\x00_coresq<K\x00N\x86q=X\x06\x00\x00\x00_nodesq>K\x01N\x86q?uh<K\x01h>K\x01ubub.')
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
