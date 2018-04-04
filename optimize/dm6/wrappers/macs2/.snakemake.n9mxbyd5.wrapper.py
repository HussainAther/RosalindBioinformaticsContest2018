
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x03\x00\x00\x00logq\x05csnakemake.io\nLog\nq\x06)\x81q\x07}q\x08X\x06\x00\x00\x00_namesq\t}q\nsbX\t\x00\x00\x00resourcesq\x0bcsnakemake.io\nResources\nq\x0c)\x81q\r(K\x01K\x01e}q\x0e(X\x06\x00\x00\x00_nodesq\x0fK\x01X\x06\x00\x00\x00_coresq\x10K\x01h\t}q\x11(h\x10K\x00N\x86q\x12h\x0fK\x01N\x86q\x13uubX\x07\x00\x00\x00threadsq\x14K\x01X\x06\x00\x00\x00outputq\x15csnakemake.io\nOutputFiles\nq\x16)\x81q\x17(X8\x00\x00\x00peak_out/macs2/lm08_kc_shep-r6_R1/lm08_kc_shep-r6_R1.bedq\x18XE\x00\x00\x00peak_out/macs2/lm08_kc_shep-r6_R1/lm08_kc_shep-r6_R1_peaks.narrowPeakq\x19e}q\x1a(X\n\x00\x00\x00narrowPeakq\x1bh\x19X\x03\x00\x00\x00bedq\x1ch\x18h\t}q\x1d(h\x1cK\x00N\x86q\x1eh\x1bK\x01N\x86q\x1fuubX\x06\x00\x00\x00paramsq csnakemake.io\nParams\nq!)\x81q"(X!\x00\x00\x00peak_out/macs2/lm08_kc_shep-r6_R1q#X\x12\x00\x00\x00lm08_kc_shep-r6_R1q$e}q%(X\x06\x00\x00\x00prefixq&h#X\x0e\x00\x00\x00wrapper_sampleq\'h$h\t}q((h&K\x00N\x86q)h\'K\x01N\x86q*uubX\x05\x00\x00\x00inputq+csnakemake.io\nInputFiles\nq,)\x81q-(X\x1c\x00\x00\x00dedup/lm08_kc_shep-r6_R1.bamq.X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq/e}q0(X\x03\x00\x00\x00inpq1h/X\x02\x00\x00\x00ipq2h.h\t}q3(h2K\x00N\x86q4h1K\x01N\x86q5uubX\x04\x00\x00\x00ruleq6X\x05\x00\x00\x00macs2q7X\t\x00\x00\x00wildcardsq8csnakemake.io\nWildcards\nq9)\x81q:h$a}q;(X\x06\x00\x00\x00sampleq<h$h\t}q=X\x06\x00\x00\x00sampleq>K\x00N\x86q?subub.')
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
