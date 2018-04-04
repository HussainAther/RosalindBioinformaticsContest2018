
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x0f\x00\x00\x00sjl_cl8_suhw_R1q\x06a}q\x07(X\x06\x00\x00\x00sampleq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nX\x06\x00\x00\x00sampleq\x0bK\x00N\x86q\x0csubX\t\x00\x00\x00resourcesq\rcsnakemake.io\nResources\nq\x0e)\x81q\x0f(K\x01K\x01e}q\x10(X\x06\x00\x00\x00_coresq\x11K\x01h\t}q\x12(X\x06\x00\x00\x00_nodesq\x13K\x00N\x86q\x14h\x11K\x01N\x86q\x15uh\x13K\x01ubX\x05\x00\x00\x00inputq\x16csnakemake.io\nInputFiles\nq\x17)\x81q\x18(X\x19\x00\x00\x00dedup/sjl_cl8_suhw_R1.bamq\x19X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x1ae}q\x1b(X\x02\x00\x00\x00ipq\x1ch\x19X\x03\x00\x00\x00inpq\x1dh\x1ah\t}q\x1e(h\x1cK\x00N\x86q\x1fh\x1dK\x01N\x86q uubX\x03\x00\x00\x00logq!csnakemake.io\nLog\nq")\x81q#}q$h\t}q%sbX\x06\x00\x00\x00paramsq&csnakemake.io\nParams\nq\')\x81q((h\x06X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1q)e}q*(X\x0e\x00\x00\x00wrapper_sampleq+h\x06h\t}q,(h+K\x00N\x86q-X\x06\x00\x00\x00prefixq.K\x01N\x86q/uh.h)ubX\x06\x00\x00\x00configq0}q1X\x07\x00\x00\x00threadsq2K\x01X\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X2\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1/sjl_cl8_suhw_R1.bedq6X?\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1/sjl_cl8_suhw_R1_peaks.narrowPeakq7e}q8(X\x03\x00\x00\x00bedq9h6h\t}q:(h9K\x00N\x86q;X\n\x00\x00\x00narrowPeakq<K\x01N\x86q=uh<h7ubX\x04\x00\x00\x00ruleq>X\x05\x00\x00\x00macs2q?ub.')
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
