
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1q\x06a}q\x07(X\x06\x00\x00\x00prefixq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nh\x08K\x00N\x86q\x0bsubX\x05\x00\x00\x00inputq\x0ccsnakemake.io\nInputFiles\nq\r)\x81q\x0e(X\x1a\x00\x00\x00dedup/sjl_mbn2_shep_R1.bamq\x0fX\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x10e}q\x11(h\t}q\x12(X\x02\x00\x00\x00ipq\x13K\x00N\x86q\x14X\x03\x00\x00\x00inpq\x15K\x01N\x86q\x16uh\x13h\x0fh\x15h\x10ubX\t\x00\x00\x00wildcardsq\x17csnakemake.io\nWildcards\nq\x18)\x81q\x19X\x10\x00\x00\x00sjl_mbn2_shep_R1q\x1aa}q\x1b(X\x06\x00\x00\x00sampleq\x1ch\x1ah\t}q\x1dX\x06\x00\x00\x00sampleq\x1eK\x00N\x86q\x1fsubX\x04\x00\x00\x00ruleq X\x05\x00\x00\x00macs2q!X\x06\x00\x00\x00configq"}q#X\x06\x00\x00\x00outputq$csnakemake.io\nOutputFiles\nq%)\x81q&(XA\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1_peaks.narrowPeakq\'X4\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1.bedq(e}q)(X\n\x00\x00\x00narrowPeakq*h\'h\t}q+(h*K\x00N\x86q,X\x03\x00\x00\x00bedq-K\x01N\x86q.uh-h(ubX\x07\x00\x00\x00threadsq/K\x01X\x03\x00\x00\x00logq0csnakemake.io\nLog\nq1)\x81q2}q3h\t}q4sbX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_coresq9K\x01X\x06\x00\x00\x00_nodesq:K\x01h\t}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.input.ip}_model.r')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
