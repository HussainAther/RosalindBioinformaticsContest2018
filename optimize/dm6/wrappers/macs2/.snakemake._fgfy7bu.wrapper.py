
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00outputq\tcsnakemake.io\nOutputFiles\nq\n)\x81q\x0b(XE\x00\x00\x00peak_out/macs2/lm07_kc_shep-r5_R1/lm07_kc_shep-r5_R1_peaks.narrowPeakq\x0cX8\x00\x00\x00peak_out/macs2/lm07_kc_shep-r5_R1/lm07_kc_shep-r5_R1.bedq\re}q\x0e(h\x07}q\x0f(X\n\x00\x00\x00narrowPeakq\x10K\x00N\x86q\x11X\x03\x00\x00\x00bedq\x12K\x01N\x86q\x13uh\x10h\x0ch\x12h\rubX\t\x00\x00\x00resourcesq\x14csnakemake.io\nResources\nq\x15)\x81q\x16(K\x01K\x01e}q\x17(h\x07}q\x18(X\x06\x00\x00\x00_nodesq\x19K\x00N\x86q\x1aX\x06\x00\x00\x00_coresq\x1bK\x01N\x86q\x1cuh\x1bK\x01h\x19K\x01ubX\x07\x00\x00\x00threadsq\x1dK\x01X\x04\x00\x00\x00ruleq\x1eX\x05\x00\x00\x00macs2q\x1fX\x05\x00\x00\x00inputq csnakemake.io\nInputFiles\nq!)\x81q"(X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq#X\x1c\x00\x00\x00dedup/lm07_kc_shep-r5_R1.bamq$e}q%(h\x07}q&(X\x03\x00\x00\x00inpq\'K\x00N\x86q(X\x02\x00\x00\x00ipq)K\x01N\x86q*uh\'h#h)h$ubX\t\x00\x00\x00wildcardsq+csnakemake.io\nWildcards\nq,)\x81q-X\x12\x00\x00\x00lm07_kc_shep-r5_R1q.a}q/(h\x07}q0X\x06\x00\x00\x00sampleq1K\x00N\x86q2sX\x06\x00\x00\x00sampleq3h.ubX\x06\x00\x00\x00configq4}q5X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X!\x00\x00\x00peak_out/macs2/lm07_kc_shep-r5_R1q9a}q:(h\x07}q;X\x06\x00\x00\x00prefixq<K\x00N\x86q=sh<h9ubub.')
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
