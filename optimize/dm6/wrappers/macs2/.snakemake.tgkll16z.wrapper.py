
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05(X \x00\x00\x00peak_out/macs2/lm38_kc_mod-rb_R1q\x06X\x11\x00\x00\x00lm38_kc_mod-rb_R1q\x07e}q\x08(X\x06\x00\x00\x00prefixq\th\x06X\x0e\x00\x00\x00wrapper_sampleq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\t\x00\x00\x00wildcardsq\x0fcsnakemake.io\nWildcards\nq\x10)\x81q\x11h\x07a}q\x12(X\x06\x00\x00\x00sampleq\x13h\x07h\x0b}q\x14X\x06\x00\x00\x00sampleq\x15K\x00N\x86q\x16subX\x04\x00\x00\x00ruleq\x17X\x05\x00\x00\x00macs2q\x18X\x06\x00\x00\x00outputq\x19csnakemake.io\nOutputFiles\nq\x1a)\x81q\x1b(XC\x00\x00\x00peak_out/macs2/lm38_kc_mod-rb_R1/lm38_kc_mod-rb_R1_peaks.narrowPeakq\x1cX6\x00\x00\x00peak_out/macs2/lm38_kc_mod-rb_R1/lm38_kc_mod-rb_R1.bedq\x1de}q\x1e(h\x0b}q\x1f(X\n\x00\x00\x00narrowPeakq K\x00N\x86q!X\x03\x00\x00\x00bedq"K\x01N\x86q#uh"h\x1dh h\x1cubX\x06\x00\x00\x00configq$}q%X\x05\x00\x00\x00inputq&csnakemake.io\nInputFiles\nq\')\x81q((X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq)X\x1b\x00\x00\x00dedup/lm38_kc_mod-rb_R1.bamq*e}q+(X\x03\x00\x00\x00inpq,h)h\x0b}q-(h,K\x00N\x86q.X\x02\x00\x00\x00ipq/K\x01N\x86q0uh/h*ubX\x03\x00\x00\x00logq1csnakemake.io\nLog\nq2)\x81q3}q4h\x0b}q5sbX\t\x00\x00\x00resourcesq6csnakemake.io\nResources\nq7)\x81q8(K\x01K\x01e}q9(X\x06\x00\x00\x00_coresq:K\x01X\x06\x00\x00\x00_nodesq;K\x01h\x0b}q<(h:K\x00N\x86q=h;K\x01N\x86q>uubX\x07\x00\x00\x00threadsq?K\x01ub.')
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
