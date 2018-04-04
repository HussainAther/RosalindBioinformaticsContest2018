
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05(X\x0e\x00\x00\x00sjl_kc_shep_R1q\x06X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x0e\x00\x00\x00wrapper_sampleq\x0bK\x00N\x86q\x0cX\x06\x00\x00\x00prefixq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\t\x00\x00\x00wildcardsq\x0fcsnakemake.io\nWildcards\nq\x10)\x81q\x11h\x06a}q\x12(h\t}q\x13X\x06\x00\x00\x00sampleq\x14K\x00N\x86q\x15sX\x06\x00\x00\x00sampleq\x16h\x06ubX\x05\x00\x00\x00inputq\x17csnakemake.io\nInputFiles\nq\x18)\x81q\x19(X\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq\x1aX\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq\x1be}q\x1c(h\t}q\x1d(X\x02\x00\x00\x00ipq\x1eK\x00N\x86q\x1fX\x03\x00\x00\x00inpq K\x01N\x86q!uh\x1eh\x1ah h\x1bubX\x03\x00\x00\x00logq"csnakemake.io\nLog\nq#)\x81q$}q%h\t}q&sbX\x06\x00\x00\x00configq\'}q(X\x06\x00\x00\x00outputq)csnakemake.io\nOutputFiles\nq*)\x81q+(X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq,X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq-e}q.(h\t}q/(X\n\x00\x00\x00narrowPeakq0K\x01N\x86q1X\x03\x00\x00\x00bedq2K\x00N\x86q3uh0h-h2h,ubX\t\x00\x00\x00resourcesq4csnakemake.io\nResources\nq5)\x81q6(K\x01K\x01e}q7(h\t}q8(X\x06\x00\x00\x00_coresq9K\x00N\x86q:X\x06\x00\x00\x00_nodesq;K\x01N\x86q<uh;K\x01h9K\x01ubX\x04\x00\x00\x00ruleq=X\x05\x00\x00\x00macs2q>X\x07\x00\x00\x00threadsq?K\x01ub.')
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
