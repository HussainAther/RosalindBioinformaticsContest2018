
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x1a\x00\x00\x00dedup/sjl_mbn2_shep_R1.bamq\x06X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x02\x00\x00\x00ipq\x0bK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1q\x12a}q\x13(h\t}q\x14X\x06\x00\x00\x00prefixq\x15K\x00N\x86q\x16sh\x15h\x12ubX\x07\x00\x00\x00threadsq\x17K\x01X\x03\x00\x00\x00logq\x18csnakemake.io\nLog\nq\x19)\x81q\x1a}q\x1bh\t}q\x1csbX\x06\x00\x00\x00outputq\x1dcsnakemake.io\nOutputFiles\nq\x1e)\x81q\x1f(XA\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1_peaks.narrowPeakq X4\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1.bedq!e}q"(h\t}q#(X\n\x00\x00\x00narrowPeakq$K\x00N\x86q%X\x03\x00\x00\x00bedq&K\x01N\x86q\'uh$h h&h!ubX\t\x00\x00\x00resourcesq(csnakemake.io\nResources\nq))\x81q*(K\x01K\x01e}q+(h\t}q,(X\x06\x00\x00\x00_coresq-K\x00N\x86q.X\x06\x00\x00\x00_nodesq/K\x01N\x86q0uh-K\x01h/K\x01ubX\t\x00\x00\x00wildcardsq1csnakemake.io\nWildcards\nq2)\x81q3X\x10\x00\x00\x00sjl_mbn2_shep_R1q4a}q5(X\x06\x00\x00\x00sampleq6h4h\t}q7X\x06\x00\x00\x00sampleq8K\x00N\x86q9subX\x04\x00\x00\x00ruleq:X\x05\x00\x00\x00macs2q;X\x06\x00\x00\x00configq<}q=ub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.wildcards.sample}_model.r')
#shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
shell("cd {snakemake.params.prefix} && ln -sf $(basename {snakemake.output.narrowPeak}) $(basename {snakemake.output.bed})")
