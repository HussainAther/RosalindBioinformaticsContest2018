
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00configq\x04}q\x05X\t\x00\x00\x00resourcesq\x06csnakemake.io\nResources\nq\x07)\x81q\x08(K\x01K\x01e}q\t(X\x06\x00\x00\x00_namesq\n}q\x0b(X\x06\x00\x00\x00_nodesq\x0cK\x00N\x86q\rX\x06\x00\x00\x00_coresq\x0eK\x01N\x86q\x0fuh\x0cK\x01h\x0eK\x01ubX\x03\x00\x00\x00logq\x10csnakemake.io\nLog\nq\x11)\x81q\x12}q\x13h\n}q\x14sbX\x06\x00\x00\x00paramsq\x15csnakemake.io\nParams\nq\x16)\x81q\x17(X\x1d\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1q\x18X\x0e\x00\x00\x00sjl_cl8_mod_R1q\x19e}q\x1a(h\n}q\x1b(X\x06\x00\x00\x00prefixq\x1cK\x00N\x86q\x1dX\x0e\x00\x00\x00wrapper_sampleq\x1eK\x01N\x86q\x1fuh\x1eh\x19h\x1ch\x18ubX\x04\x00\x00\x00ruleq X\x05\x00\x00\x00macs2q!X\x05\x00\x00\x00inputq"csnakemake.io\nInputFiles\nq#)\x81q$(X\x18\x00\x00\x00dedup/sjl_cl8_mod_R1.bamq%X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq&e}q\'(h\n}q((X\x02\x00\x00\x00ipq)K\x00N\x86q*X\x03\x00\x00\x00inpq+K\x01N\x86q,uh)h%h+h&ubX\t\x00\x00\x00wildcardsq-csnakemake.io\nWildcards\nq.)\x81q/h\x19a}q0(h\n}q1X\x06\x00\x00\x00sampleq2K\x00N\x86q3sX\x06\x00\x00\x00sampleq4h\x19ubX\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(X0\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1/sjl_cl8_mod_R1.bedq8X=\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1/sjl_cl8_mod_R1_peaks.narrowPeakq9e}q:(h\n}q;(X\x03\x00\x00\x00bedq<K\x00N\x86q=X\n\x00\x00\x00narrowPeakq>K\x01N\x86q?uh<h8h>h9ubub.')
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
