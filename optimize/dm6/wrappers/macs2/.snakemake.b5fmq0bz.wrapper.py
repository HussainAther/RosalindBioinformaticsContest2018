
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq\x06X\x1c\x00\x00\x00dedup/lm40_kc_rm62-rb_R1.bamq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x03\x00\x00\x00inpq\x0bK\x00N\x86q\x0cX\x02\x00\x00\x00ipq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x07\x00\x00\x00threadsq\x0fK\x01X\x06\x00\x00\x00outputq\x10csnakemake.io\nOutputFiles\nq\x11)\x81q\x12(X8\x00\x00\x00peak_out/macs2/lm40_kc_rm62-rb_R1/lm40_kc_rm62-rb_R1.bedq\x13XE\x00\x00\x00peak_out/macs2/lm40_kc_rm62-rb_R1/lm40_kc_rm62-rb_R1_peaks.narrowPeakq\x14e}q\x15(X\x03\x00\x00\x00bedq\x16h\x13h\t}q\x17(h\x16K\x00N\x86q\x18X\n\x00\x00\x00narrowPeakq\x19K\x01N\x86q\x1auh\x19h\x14ubX\x04\x00\x00\x00ruleq\x1bX\x05\x00\x00\x00macs2q\x1cX\t\x00\x00\x00resourcesq\x1dcsnakemake.io\nResources\nq\x1e)\x81q\x1f(K\x01K\x01e}q (h\t}q!(X\x06\x00\x00\x00_nodesq"K\x01N\x86q#X\x06\x00\x00\x00_coresq$K\x00N\x86q%uh"K\x01h$K\x01ubX\t\x00\x00\x00wildcardsq&csnakemake.io\nWildcards\nq\')\x81q(X\x12\x00\x00\x00lm40_kc_rm62-rb_R1q)a}q*(h\t}q+X\x06\x00\x00\x00sampleq,K\x00N\x86q-sX\x06\x00\x00\x00sampleq.h)ubX\x03\x00\x00\x00logq/csnakemake.io\nLog\nq0)\x81q1}q2h\t}q3sbX\x06\x00\x00\x00configq4}q5X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X!\x00\x00\x00peak_out/macs2/lm40_kc_rm62-rb_R1q9a}q:(h\t}q;X\x06\x00\x00\x00prefixq<K\x00N\x86q=sh<h9ubub.')
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
shell('touch {snakemake.output.bed}')
shell('Rscript peak_out/macs2/{snakemake.params.prefix}_model.r')
