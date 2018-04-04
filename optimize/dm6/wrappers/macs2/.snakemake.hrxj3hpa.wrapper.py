
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_namesq\x08}q\t(h\x07K\x00N\x86q\nX\x06\x00\x00\x00_coresq\x0bK\x01N\x86q\x0cuh\x0bK\x01ubX\x04\x00\x00\x00ruleq\rX\x05\x00\x00\x00macs2q\x0eX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11X \x00\x00\x00peak_out/macs2/lm37_kc_mod-gp_R1q\x12a}q\x13(X\x06\x00\x00\x00prefixq\x14h\x12h\x08}q\x15h\x14K\x00N\x86q\x16subX\x07\x00\x00\x00threadsq\x17K\x01X\x03\x00\x00\x00logq\x18csnakemake.io\nLog\nq\x19)\x81q\x1a}q\x1bh\x08}q\x1csbX\x05\x00\x00\x00inputq\x1dcsnakemake.io\nInputFiles\nq\x1e)\x81q\x1f(X\x1b\x00\x00\x00dedup/lm37_kc_mod-gp_R1.bamq X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq!e}q"(X\x02\x00\x00\x00ipq#h h\x08}q$(h#K\x00N\x86q%X\x03\x00\x00\x00inpq&K\x01N\x86q\'uh&h!ubX\x06\x00\x00\x00configq(}q)X\t\x00\x00\x00wildcardsq*csnakemake.io\nWildcards\nq+)\x81q,X\x11\x00\x00\x00lm37_kc_mod-gp_R1q-a}q.(X\x06\x00\x00\x00sampleq/h-h\x08}q0X\x06\x00\x00\x00sampleq1K\x00N\x86q2subX\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(XC\x00\x00\x00peak_out/macs2/lm37_kc_mod-gp_R1/lm37_kc_mod-gp_R1_peaks.narrowPeakq6X6\x00\x00\x00peak_out/macs2/lm37_kc_mod-gp_R1/lm37_kc_mod-gp_R1.bedq7e}q8(X\n\x00\x00\x00narrowPeakq9h6h\x08}q:(h9K\x00N\x86q;X\x03\x00\x00\x00bedq<K\x01N\x86q=uh<h7ubub.')
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
