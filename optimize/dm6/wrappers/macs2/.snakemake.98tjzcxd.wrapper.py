
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05(X \x00\x00\x00peak_out/macs2/lm37_kc_mod-gp_R1q\x06X\x11\x00\x00\x00lm37_kc_mod-gp_R1q\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x06\x00\x00\x00prefixq\x0bK\x00N\x86q\x0cX\x0e\x00\x00\x00wrapper_sampleq\rK\x01N\x86q\x0euh\rh\x07h\x0bh\x06ubX\t\x00\x00\x00resourcesq\x0fcsnakemake.io\nResources\nq\x10)\x81q\x11(K\x01K\x01e}q\x12(h\t}q\x13(X\x06\x00\x00\x00_nodesq\x14K\x00N\x86q\x15X\x06\x00\x00\x00_coresq\x16K\x01N\x86q\x17uh\x14K\x01h\x16K\x01ubX\x04\x00\x00\x00ruleq\x18X\x05\x00\x00\x00macs2q\x19X\x06\x00\x00\x00outputq\x1acsnakemake.io\nOutputFiles\nq\x1b)\x81q\x1c(XC\x00\x00\x00peak_out/macs2/lm37_kc_mod-gp_R1/lm37_kc_mod-gp_R1_peaks.narrowPeakq\x1dX6\x00\x00\x00peak_out/macs2/lm37_kc_mod-gp_R1/lm37_kc_mod-gp_R1.bedq\x1ee}q\x1f(h\t}q (X\n\x00\x00\x00narrowPeakq!K\x00N\x86q"X\x03\x00\x00\x00bedq#K\x01N\x86q$uh!h\x1dh#h\x1eubX\x07\x00\x00\x00threadsq%K\x01X\t\x00\x00\x00wildcardsq&csnakemake.io\nWildcards\nq\')\x81q(h\x07a}q)(h\t}q*X\x06\x00\x00\x00sampleq+K\x00N\x86q,sX\x06\x00\x00\x00sampleq-h\x07ubX\x03\x00\x00\x00logq.csnakemake.io\nLog\nq/)\x81q0}q1h\t}q2sbX\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq6X\x1b\x00\x00\x00dedup/lm37_kc_mod-gp_R1.bamq7e}q8(h\t}q9(X\x03\x00\x00\x00inpq:K\x00N\x86q;X\x02\x00\x00\x00ipq<K\x01N\x86q=uh:h6h<h7ubX\x06\x00\x00\x00configq>}q?ub.')
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
