
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x04\x00\x00\x00ruleq\x05X\x05\x00\x00\x00macs2q\x06X\x05\x00\x00\x00inputq\x07csnakemake.io\nInputFiles\nq\x08)\x81q\t(X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq\nX\x17\x00\x00\x00dedup/sjl_kc_mod_R1.bamq\x0be}q\x0c(X\x06\x00\x00\x00_namesq\r}q\x0e(X\x03\x00\x00\x00inpq\x0fK\x00N\x86q\x10X\x02\x00\x00\x00ipq\x11K\x01N\x86q\x12uh\x0fh\nh\x11h\x0bubX\x06\x00\x00\x00paramsq\x13csnakemake.io\nParams\nq\x14)\x81q\x15(X\r\x00\x00\x00sjl_kc_mod_R1q\x16X\x1c\x00\x00\x00peak_out/macs2/sjl_kc_mod_R1q\x17e}q\x18(h\r}q\x19(X\x0e\x00\x00\x00wrapper_sampleq\x1aK\x00N\x86q\x1bX\x06\x00\x00\x00prefixq\x1cK\x01N\x86q\x1duh\x1ah\x16h\x1ch\x17ubX\t\x00\x00\x00wildcardsq\x1ecsnakemake.io\nWildcards\nq\x1f)\x81q h\x16a}q!(h\r}q"X\x06\x00\x00\x00sampleq#K\x00N\x86q$sX\x06\x00\x00\x00sampleq%h\x16ubX\x03\x00\x00\x00logq&csnakemake.io\nLog\nq\')\x81q(}q)h\r}q*sbX\t\x00\x00\x00resourcesq+csnakemake.io\nResources\nq,)\x81q-(K\x01K\x01e}q.(h\r}q/(X\x06\x00\x00\x00_nodesq0K\x00N\x86q1X\x06\x00\x00\x00_coresq2K\x01N\x86q3uh0K\x01h2K\x01ubX\x07\x00\x00\x00threadsq4K\x01X\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(X;\x00\x00\x00peak_out/macs2/sjl_kc_mod_R1/sjl_kc_mod_R1_peaks.narrowPeakq8X.\x00\x00\x00peak_out/macs2/sjl_kc_mod_R1/sjl_kc_mod_R1.bedq9e}q:(h\r}q;(X\n\x00\x00\x00narrowPeakq<K\x00N\x86q=X\x03\x00\x00\x00bedq>K\x01N\x86q?uh<h8h>h9ubub.')
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
