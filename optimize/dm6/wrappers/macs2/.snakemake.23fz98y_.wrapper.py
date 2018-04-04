
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x07\x00\x00\x00threadsq\x05K\x01X\x05\x00\x00\x00inputq\x06csnakemake.io\nInputFiles\nq\x07)\x81q\x08(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\tX\x17\x00\x00\x00dedup/sjl_s2_mod_R1.bamq\ne}q\x0b(X\x03\x00\x00\x00inpq\x0ch\tX\x06\x00\x00\x00_namesq\r}q\x0e(h\x0cK\x00N\x86q\x0fX\x02\x00\x00\x00ipq\x10K\x01N\x86q\x11uh\x10h\nubX\x04\x00\x00\x00ruleq\x12X\x05\x00\x00\x00macs2q\x13X\x06\x00\x00\x00outputq\x14csnakemake.io\nOutputFiles\nq\x15)\x81q\x16(X;\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1_peaks.narrowPeakq\x17X.\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1.bedq\x18e}q\x19(h\r}q\x1a(X\n\x00\x00\x00narrowPeakq\x1bK\x00N\x86q\x1cX\x03\x00\x00\x00bedq\x1dK\x01N\x86q\x1euh\x1bh\x17h\x1dh\x18ubX\t\x00\x00\x00wildcardsq\x1fcsnakemake.io\nWildcards\nq )\x81q!X\r\x00\x00\x00sjl_s2_mod_R1q"a}q#(h\r}q$X\x06\x00\x00\x00sampleq%K\x00N\x86q&sX\x06\x00\x00\x00sampleq\'h"ubX\x03\x00\x00\x00logq(csnakemake.io\nLog\nq))\x81q*}q+h\r}q,sbX\t\x00\x00\x00resourcesq-csnakemake.io\nResources\nq.)\x81q/(K\x01K\x01e}q0(h\r}q1(X\x06\x00\x00\x00_coresq2K\x00N\x86q3X\x06\x00\x00\x00_nodesq4K\x01N\x86q5uh2K\x01h4K\x01ubX\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8(h"X\x1c\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1q9e}q:(h\r}q;(X\x0e\x00\x00\x00wrapper_sampleq<K\x00N\x86q=X\x06\x00\x00\x00prefixq>K\x01N\x86q?uh<h"h>h9ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.params.sample}_model.r')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
