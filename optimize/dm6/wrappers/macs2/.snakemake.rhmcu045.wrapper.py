
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_namesq\x08}q\t(X\x06\x00\x00\x00_coresq\nK\x00N\x86q\x0bh\x07K\x01N\x86q\x0cuh\nK\x01ubX\t\x00\x00\x00wildcardsq\rcsnakemake.io\nWildcards\nq\x0e)\x81q\x0fX\x12\x00\x00\x00lm10_kc_shep-gp_R1q\x10a}q\x11(X\x06\x00\x00\x00sampleq\x12h\x10h\x08}q\x13X\x06\x00\x00\x00sampleq\x14K\x00N\x86q\x15subX\x06\x00\x00\x00paramsq\x16csnakemake.io\nParams\nq\x17)\x81q\x18(h\x10X!\x00\x00\x00peak_out/macs2/lm10_kc_shep-gp_R1q\x19e}q\x1a(h\x08}q\x1b(X\x0e\x00\x00\x00wrapper_sampleq\x1cK\x00N\x86q\x1dX\x06\x00\x00\x00prefixq\x1eK\x01N\x86q\x1fuh\x1eh\x19h\x1ch\x10ubX\x03\x00\x00\x00logq csnakemake.io\nLog\nq!)\x81q"}q#h\x08}q$sbX\x04\x00\x00\x00ruleq%X\x05\x00\x00\x00macs2q&X\x05\x00\x00\x00inputq\'csnakemake.io\nInputFiles\nq()\x81q)(X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq*X\x1c\x00\x00\x00dedup/lm10_kc_shep-gp_R1.bamq+e}q,(X\x03\x00\x00\x00inpq-h*h\x08}q.(h-K\x00N\x86q/X\x02\x00\x00\x00ipq0K\x01N\x86q1uh0h+ubX\x06\x00\x00\x00configq2}q3X\x07\x00\x00\x00threadsq4K\x01X\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(X8\x00\x00\x00peak_out/macs2/lm10_kc_shep-gp_R1/lm10_kc_shep-gp_R1.bedq8XE\x00\x00\x00peak_out/macs2/lm10_kc_shep-gp_R1/lm10_kc_shep-gp_R1_peaks.narrowPeakq9e}q:(h\x08}q;(X\n\x00\x00\x00narrowPeakq<K\x01N\x86q=X\x03\x00\x00\x00bedq>K\x00N\x86q?uh<h9h>h8ubub.')
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
