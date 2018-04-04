
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_coresq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x07K\x00N\x86q\x0bh\x08K\x01N\x86q\x0cuubX\x05\x00\x00\x00inputq\rcsnakemake.io\nInputFiles\nq\x0e)\x81q\x0f(X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x10X\x19\x00\x00\x00dedup/sjl_cl8_shep_R1.bamq\x11e}q\x12(X\x03\x00\x00\x00inpq\x13h\x10X\x02\x00\x00\x00ipq\x14h\x11h\t}q\x15(h\x13K\x00N\x86q\x16h\x14K\x01N\x86q\x17uubX\t\x00\x00\x00wildcardsq\x18csnakemake.io\nWildcards\nq\x19)\x81q\x1aX\x0f\x00\x00\x00sjl_cl8_shep_R1q\x1ba}q\x1c(X\x06\x00\x00\x00sampleq\x1dh\x1bh\t}q\x1eX\x06\x00\x00\x00sampleq\x1fK\x00N\x86q subX\x06\x00\x00\x00outputq!csnakemake.io\nOutputFiles\nq")\x81q#(X2\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1.bedq$X?\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1_peaks.narrowPeakq%e}q&(X\x03\x00\x00\x00bedq\'h$h\t}q((h\'K\x00N\x86q)X\n\x00\x00\x00narrowPeakq*K\x01N\x86q+uh*h%ubX\x04\x00\x00\x00ruleq,X\x05\x00\x00\x00macs2q-X\x06\x00\x00\x00configq.}q/X\x07\x00\x00\x00threadsq0K\x01X\x03\x00\x00\x00logq1csnakemake.io\nLog\nq2)\x81q3}q4h\t}q5sbX\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8(X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1q9h\x1be}q:(X\x0e\x00\x00\x00wrapper_sampleq;h\x1bX\x06\x00\x00\x00prefixq<h9h\t}q=(h<K\x00N\x86q>h;K\x01N\x86q?uubub.')
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
