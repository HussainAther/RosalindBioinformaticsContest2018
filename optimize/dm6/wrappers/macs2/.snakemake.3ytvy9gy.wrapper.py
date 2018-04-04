
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x0e\x00\x00\x00sjl_s2_shep_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00sampleq\nK\x00N\x86q\x0bsX\x06\x00\x00\x00sampleq\x0ch\x06ubX\x05\x00\x00\x00inputq\rcsnakemake.io\nInputFiles\nq\x0e)\x81q\x0f(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x10X\x18\x00\x00\x00dedup/sjl_s2_shep_R1.bamq\x11e}q\x12(h\x08}q\x13(X\x03\x00\x00\x00inpq\x14K\x00N\x86q\x15X\x02\x00\x00\x00ipq\x16K\x01N\x86q\x17uh\x14h\x10h\x16h\x11ubX\x03\x00\x00\x00logq\x18csnakemake.io\nLog\nq\x19)\x81q\x1a}q\x1bh\x08}q\x1csbX\x06\x00\x00\x00configq\x1d}q\x1eX\x07\x00\x00\x00threadsq\x1fK\x01X\t\x00\x00\x00resourcesq csnakemake.io\nResources\nq!)\x81q"(K\x01K\x01e}q#(h\x08}q$(X\x06\x00\x00\x00_nodesq%K\x00N\x86q&X\x06\x00\x00\x00_coresq\'K\x01N\x86q(uh%K\x01h\'K\x01ubX\x06\x00\x00\x00paramsq)csnakemake.io\nParams\nq*)\x81q+(X\x1d\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1q,h\x06e}q-(h\x08}q.(X\x06\x00\x00\x00prefixq/K\x00N\x86q0X\x0e\x00\x00\x00wrapper_sampleq1K\x01N\x86q2uh/h,h1h\x06ubX\x04\x00\x00\x00ruleq3X\x05\x00\x00\x00macs2q4X\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(X=\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1_peaks.narrowPeakq8X0\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1.bedq9e}q:(h\x08}q;(X\n\x00\x00\x00narrowPeakq<K\x00N\x86q=X\x03\x00\x00\x00bedq>K\x01N\x86q?uh<h8h>h9ubub.')
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
