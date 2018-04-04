
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X0\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1.bedq\x06X=\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1_peaks.narrowPeakq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\n\x00\x00\x00narrowPeakq\x0bK\x01N\x86q\x0cX\x03\x00\x00\x00bedq\rK\x00N\x86q\x0euh\x0bh\x07h\rh\x06ubX\t\x00\x00\x00wildcardsq\x0fcsnakemake.io\nWildcards\nq\x10)\x81q\x11X\x0e\x00\x00\x00sjl_s2_shep_R1q\x12a}q\x13(X\x06\x00\x00\x00sampleq\x14h\x12h\t}q\x15X\x06\x00\x00\x00sampleq\x16K\x00N\x86q\x17subX\t\x00\x00\x00resourcesq\x18csnakemake.io\nResources\nq\x19)\x81q\x1a(K\x01K\x01e}q\x1b(X\x06\x00\x00\x00_nodesq\x1cK\x01X\x06\x00\x00\x00_coresq\x1dK\x01h\t}q\x1e(h\x1cK\x00N\x86q\x1fh\x1dK\x01N\x86q uubX\x03\x00\x00\x00logq!csnakemake.io\nLog\nq")\x81q#}q$h\t}q%sbX\x07\x00\x00\x00threadsq&K\x01X\x06\x00\x00\x00configq\'}q(X\x05\x00\x00\x00inputq)csnakemake.io\nInputFiles\nq*)\x81q+(X\x18\x00\x00\x00dedup/sjl_s2_shep_R1.bamq,X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq-e}q.(h\t}q/(X\x02\x00\x00\x00ipq0K\x00N\x86q1X\x03\x00\x00\x00inpq2K\x01N\x86q3uh0h,h2h-ubX\x06\x00\x00\x00paramsq4csnakemake.io\nParams\nq5)\x81q6(h\x12X\x1d\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1q7e}q8(X\x0e\x00\x00\x00wrapper_sampleq9h\x12X\x06\x00\x00\x00prefixq:h7h\t}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubX\x04\x00\x00\x00ruleq>X\x05\x00\x00\x00macs2q?ub.')
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
