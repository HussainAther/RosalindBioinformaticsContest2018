
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\t\x00\x00\x00resourcesq\x04csnakemake.io\nResources\nq\x05)\x81q\x06(K\x01K\x01e}q\x07(X\x06\x00\x00\x00_namesq\x08}q\t(X\x06\x00\x00\x00_coresq\nK\x00N\x86q\x0bX\x06\x00\x00\x00_nodesq\x0cK\x01N\x86q\ruh\x0cK\x01h\nK\x01ubX\x04\x00\x00\x00ruleq\x0eX\x05\x00\x00\x00macs2q\x0fX\x06\x00\x00\x00paramsq\x10csnakemake.io\nParams\nq\x11)\x81q\x12X\x1e\x00\x00\x00peak_out/macs2/lm32_kc_suhw_R1q\x13a}q\x14(h\x08}q\x15X\x06\x00\x00\x00prefixq\x16K\x00N\x86q\x17sh\x16h\x13ubX\x03\x00\x00\x00logq\x18csnakemake.io\nLog\nq\x19)\x81q\x1a}q\x1bh\x08}q\x1csbX\t\x00\x00\x00wildcardsq\x1dcsnakemake.io\nWildcards\nq\x1e)\x81q\x1fX\x0f\x00\x00\x00lm32_kc_suhw_R1q a}q!(h\x08}q"X\x06\x00\x00\x00sampleq#K\x00N\x86q$sX\x06\x00\x00\x00sampleq%h ubX\x06\x00\x00\x00configq&}q\'X\x06\x00\x00\x00outputq(csnakemake.io\nOutputFiles\nq))\x81q*(X2\x00\x00\x00peak_out/macs2/lm32_kc_suhw_R1/lm32_kc_suhw_R1.bedq+X?\x00\x00\x00peak_out/macs2/lm32_kc_suhw_R1/lm32_kc_suhw_R1_peaks.narrowPeakq,e}q-(h\x08}q.(X\x03\x00\x00\x00bedq/K\x00N\x86q0X\n\x00\x00\x00narrowPeakq1K\x01N\x86q2uh/h+h1h,ubX\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x19\x00\x00\x00dedup/lm32_kc_suhw_R1.bamq6X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq7e}q8(h\x08}q9(X\x02\x00\x00\x00ipq:K\x00N\x86q;X\x03\x00\x00\x00inpq<K\x01N\x86q=uh:h6h<h7ubub.')
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
