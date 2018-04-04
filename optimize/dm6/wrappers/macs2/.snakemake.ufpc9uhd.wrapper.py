
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x14\x00\x00\x00el42_kc_rump-10c3_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00sampleq\nK\x00N\x86q\x0bsX\x06\x00\x00\x00sampleq\x0ch\x06ubX\t\x00\x00\x00resourcesq\rcsnakemake.io\nResources\nq\x0e)\x81q\x0f(K\x01K\x01e}q\x10(h\x08}q\x11(X\x06\x00\x00\x00_nodesq\x12K\x00N\x86q\x13X\x06\x00\x00\x00_coresq\x14K\x01N\x86q\x15uh\x12K\x01h\x14K\x01ubX\x05\x00\x00\x00inputq\x16csnakemake.io\nInputFiles\nq\x17)\x81q\x18(X\x1a\x00\x00\x00dedup/el38_kc_input_R1.bamq\x19X\x1e\x00\x00\x00dedup/el42_kc_rump-10c3_R1.bamq\x1ae}q\x1b(X\x03\x00\x00\x00inpq\x1ch\x19X\x02\x00\x00\x00ipq\x1dh\x1ah\x08}q\x1e(h\x1cK\x00N\x86q\x1fh\x1dK\x01N\x86q uubX\x06\x00\x00\x00paramsq!csnakemake.io\nParams\nq")\x81q#(h\x06X#\x00\x00\x00peak_out/macs2/el42_kc_rump-10c3_R1q$e}q%(h\x08}q&(X\x0e\x00\x00\x00wrapper_sampleq\'K\x00N\x86q(X\x06\x00\x00\x00prefixq)K\x01N\x86q*uh)h$h\'h\x06ubX\x04\x00\x00\x00ruleq+X\x05\x00\x00\x00macs2q,X\x06\x00\x00\x00outputq-csnakemake.io\nOutputFiles\nq.)\x81q/(XI\x00\x00\x00peak_out/macs2/el42_kc_rump-10c3_R1/el42_kc_rump-10c3_R1_peaks.narrowPeakq0X<\x00\x00\x00peak_out/macs2/el42_kc_rump-10c3_R1/el42_kc_rump-10c3_R1.bedq1e}q2(X\n\x00\x00\x00narrowPeakq3h0h\x08}q4(h3K\x00N\x86q5X\x03\x00\x00\x00bedq6K\x01N\x86q7uh6h1ubX\x07\x00\x00\x00threadsq8K\x01X\x06\x00\x00\x00configq9}q:X\x03\x00\x00\x00logq;csnakemake.io\nLog\nq<)\x81q=}q>h\x08}q?sbub.')
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
