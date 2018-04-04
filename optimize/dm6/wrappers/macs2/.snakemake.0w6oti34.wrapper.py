
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq\x06X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x02\x00\x00\x00ipq\x0bK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x06\x00\x00\x00configq\x0f}q\x10X\t\x00\x00\x00wildcardsq\x11csnakemake.io\nWildcards\nq\x12)\x81q\x13X\x0e\x00\x00\x00sjl_kc_shep_R1q\x14a}q\x15(h\t}q\x16X\x06\x00\x00\x00sampleq\x17K\x00N\x86q\x18sX\x06\x00\x00\x00sampleq\x19h\x14ubX\x06\x00\x00\x00paramsq\x1acsnakemake.io\nParams\nq\x1b)\x81q\x1c(h\x14X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q\x1de}q\x1e(h\t}q\x1f(X\x0e\x00\x00\x00wrapper_sampleq K\x00N\x86q!X\x06\x00\x00\x00prefixq"K\x01N\x86q#uh h\x14h"h\x1dubX\x07\x00\x00\x00threadsq$K\x01X\x06\x00\x00\x00outputq%csnakemake.io\nOutputFiles\nq&)\x81q\'(X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq(X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq)e}q*(h\t}q+(X\n\x00\x00\x00narrowPeakq,K\x00N\x86q-X\x03\x00\x00\x00bedq.K\x01N\x86q/uh,h(h.h)ubX\x04\x00\x00\x00ruleq0X\x05\x00\x00\x00macs2q1X\t\x00\x00\x00resourcesq2csnakemake.io\nResources\nq3)\x81q4(K\x01K\x01e}q5(h\t}q6(X\x06\x00\x00\x00_coresq7K\x00N\x86q8X\x06\x00\x00\x00_nodesq9K\x01N\x86q:uh7K\x01h9K\x01ubX\x03\x00\x00\x00logq;csnakemake.io\nLog\nq<)\x81q=}q>h\t}q?sbub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.r > {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.pdf')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
