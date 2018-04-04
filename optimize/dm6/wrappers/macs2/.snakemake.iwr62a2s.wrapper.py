
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x03\x00\x00\x00logq\x04csnakemake.io\nLog\nq\x05)\x81q\x06}q\x07X\x06\x00\x00\x00_namesq\x08}q\tsbX\t\x00\x00\x00resourcesq\ncsnakemake.io\nResources\nq\x0b)\x81q\x0c(K\x01K\x01e}q\r(h\x08}q\x0e(X\x06\x00\x00\x00_coresq\x0fK\x00N\x86q\x10X\x06\x00\x00\x00_nodesq\x11K\x01N\x86q\x12uh\x11K\x01h\x0fK\x01ubX\x05\x00\x00\x00inputq\x13csnakemake.io\nInputFiles\nq\x14)\x81q\x15(X\x1c\x00\x00\x00dedup/lm10_kc_shep-gp_R1.bamq\x16X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq\x17e}q\x18(X\x02\x00\x00\x00ipq\x19h\x16h\x08}q\x1a(h\x19K\x00N\x86q\x1bX\x03\x00\x00\x00inpq\x1cK\x01N\x86q\x1duh\x1ch\x17ubX\x06\x00\x00\x00configq\x1e}q\x1fX\t\x00\x00\x00wildcardsq csnakemake.io\nWildcards\nq!)\x81q"X\x12\x00\x00\x00lm10_kc_shep-gp_R1q#a}q$(h\x08}q%X\x06\x00\x00\x00sampleq&K\x00N\x86q\'sX\x06\x00\x00\x00sampleq(h#ubX\x04\x00\x00\x00ruleq)X\x05\x00\x00\x00macs2q*X\x06\x00\x00\x00paramsq+csnakemake.io\nParams\nq,)\x81q-X!\x00\x00\x00peak_out/macs2/lm10_kc_shep-gp_R1q.a}q/(X\x06\x00\x00\x00prefixq0h.h\x08}q1h0K\x00N\x86q2subX\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(XE\x00\x00\x00peak_out/macs2/lm10_kc_shep-gp_R1/lm10_kc_shep-gp_R1_peaks.narrowPeakq6X8\x00\x00\x00peak_out/macs2/lm10_kc_shep-gp_R1/lm10_kc_shep-gp_R1.bedq7e}q8(X\n\x00\x00\x00narrowPeakq9h6h\x08}q:(h9K\x00N\x86q;X\x03\x00\x00\x00bedq<K\x01N\x86q=uh<h7ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.sample}_model.r')
