
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\t\x00\x00\x00resourcesq\x05csnakemake.io\nResources\nq\x06)\x81q\x07(K\x01K\x01e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x06\x00\x00\x00_nodesq\x0bK\x00N\x86q\x0cX\x06\x00\x00\x00_coresq\rK\x01N\x86q\x0euh\x0bK\x01h\rK\x01ubX\x07\x00\x00\x00threadsq\x0fK\x01X\x05\x00\x00\x00inputq\x10csnakemake.io\nInputFiles\nq\x11)\x81q\x12(X\x1c\x00\x00\x00dedup/lm07_kc_shep-r5_R1.bamq\x13X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq\x14e}q\x15(h\t}q\x16(X\x02\x00\x00\x00ipq\x17K\x00N\x86q\x18X\x03\x00\x00\x00inpq\x19K\x01N\x86q\x1auh\x19h\x14h\x17h\x13ubX\x06\x00\x00\x00outputq\x1bcsnakemake.io\nOutputFiles\nq\x1c)\x81q\x1d(X8\x00\x00\x00peak_out/macs2/lm07_kc_shep-r5_R1/lm07_kc_shep-r5_R1.bedq\x1eXE\x00\x00\x00peak_out/macs2/lm07_kc_shep-r5_R1/lm07_kc_shep-r5_R1_peaks.narrowPeakq\x1fe}q (h\t}q!(X\x03\x00\x00\x00bedq"K\x00N\x86q#X\n\x00\x00\x00narrowPeakq$K\x01N\x86q%uh$h\x1fh"h\x1eubX\x03\x00\x00\x00logq&csnakemake.io\nLog\nq\')\x81q(}q)h\t}q*sbX\t\x00\x00\x00wildcardsq+csnakemake.io\nWildcards\nq,)\x81q-X\x12\x00\x00\x00lm07_kc_shep-r5_R1q.a}q/(h\t}q0X\x06\x00\x00\x00sampleq1K\x00N\x86q2sX\x06\x00\x00\x00sampleq3h.ubX\x06\x00\x00\x00configq4}q5X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X!\x00\x00\x00peak_out/macs2/lm07_kc_shep-r5_R1q9a}q:(h\t}q;X\x06\x00\x00\x00prefixq<K\x00N\x86q=sh<h9ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.sample}_model.r')
