
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x13\x00\x00\x00lm46_bg3_rm62-rb_R1q\x06a}q\x07(X\x06\x00\x00\x00sampleq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nX\x06\x00\x00\x00sampleq\x0bK\x00N\x86q\x0csubX\x07\x00\x00\x00threadsq\rK\x01X\x06\x00\x00\x00paramsq\x0ecsnakemake.io\nParams\nq\x0f)\x81q\x10X"\x00\x00\x00peak_out/macs2/lm46_bg3_rm62-rb_R1q\x11a}q\x12(X\x06\x00\x00\x00prefixq\x13h\x11h\t}q\x14h\x13K\x00N\x86q\x15subX\x04\x00\x00\x00ruleq\x16X\x05\x00\x00\x00macs2q\x17X\x06\x00\x00\x00configq\x18}q\x19X\x05\x00\x00\x00inputq\x1acsnakemake.io\nInputFiles\nq\x1b)\x81q\x1c(X\x1d\x00\x00\x00dedup/lm46_bg3_rm62-rb_R1.bamq\x1dX\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq\x1ee}q\x1f(X\x02\x00\x00\x00ipq h\x1dh\t}q!(h K\x00N\x86q"X\x03\x00\x00\x00inpq#K\x01N\x86q$uh#h\x1eubX\x06\x00\x00\x00outputq%csnakemake.io\nOutputFiles\nq&)\x81q\'(XG\x00\x00\x00peak_out/macs2/lm46_bg3_rm62-rb_R1/lm46_bg3_rm62-rb_R1_peaks.narrowPeakq(X:\x00\x00\x00peak_out/macs2/lm46_bg3_rm62-rb_R1/lm46_bg3_rm62-rb_R1.bedq)e}q*(h\t}q+(X\n\x00\x00\x00narrowPeakq,K\x00N\x86q-X\x03\x00\x00\x00bedq.K\x01N\x86q/uh,h(h.h)ubX\x03\x00\x00\x00logq0csnakemake.io\nLog\nq1)\x81q2}q3h\t}q4sbX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_coresq9K\x01X\x06\x00\x00\x00_nodesq:K\x01h\t}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubub.')
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
