
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x1d\x00\x00\x00dedup/lm35_bg3_shep-r5_R1.bamq\x06X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x02\x00\x00\x00ipq\x0bK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\t\x00\x00\x00resourcesq\x0fcsnakemake.io\nResources\nq\x10)\x81q\x11(K\x01K\x01e}q\x12(h\t}q\x13(X\x06\x00\x00\x00_coresq\x14K\x00N\x86q\x15X\x06\x00\x00\x00_nodesq\x16K\x01N\x86q\x17uh\x14K\x01h\x16K\x01ubX\x07\x00\x00\x00threadsq\x18K\x01X\x06\x00\x00\x00configq\x19}q\x1aX\x06\x00\x00\x00outputq\x1bcsnakemake.io\nOutputFiles\nq\x1c)\x81q\x1d(XG\x00\x00\x00peak_out/macs2/lm35_bg3_shep-r5_R1/lm35_bg3_shep-r5_R1_peaks.narrowPeakq\x1eX:\x00\x00\x00peak_out/macs2/lm35_bg3_shep-r5_R1/lm35_bg3_shep-r5_R1.bedq\x1fe}q (h\t}q!(X\n\x00\x00\x00narrowPeakq"K\x00N\x86q#X\x03\x00\x00\x00bedq$K\x01N\x86q%uh"h\x1eh$h\x1fubX\x03\x00\x00\x00logq&csnakemake.io\nLog\nq\')\x81q(}q)h\t}q*sbX\x04\x00\x00\x00ruleq+X\x05\x00\x00\x00macs2q,X\t\x00\x00\x00wildcardsq-csnakemake.io\nWildcards\nq.)\x81q/X\x13\x00\x00\x00lm35_bg3_shep-r5_R1q0a}q1(h\t}q2X\x06\x00\x00\x00sampleq3K\x00N\x86q4sX\x06\x00\x00\x00sampleq5h0ubX\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8(X"\x00\x00\x00peak_out/macs2/lm35_bg3_shep-r5_R1q9h0e}q:(h\t}q;(X\x06\x00\x00\x00prefixq<K\x00N\x86q=X\x0e\x00\x00\x00wrapper_sampleq>K\x01N\x86q?uh<h9h>h0ubub.')
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
