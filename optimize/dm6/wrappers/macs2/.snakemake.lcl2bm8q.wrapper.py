
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_coresq\x07K\x01X\x06\x00\x00\x00_namesq\x08}q\t(X\x06\x00\x00\x00_nodesq\nK\x00N\x86q\x0bh\x07K\x01N\x86q\x0cuh\nK\x01ubX\x06\x00\x00\x00configq\r}q\x0eX\x06\x00\x00\x00outputq\x0fcsnakemake.io\nOutputFiles\nq\x10)\x81q\x11(XG\x00\x00\x00peak_out/macs2/lm34_bg3_shep-gp_R1/lm34_bg3_shep-gp_R1_peaks.narrowPeakq\x12X:\x00\x00\x00peak_out/macs2/lm34_bg3_shep-gp_R1/lm34_bg3_shep-gp_R1.bedq\x13e}q\x14(X\n\x00\x00\x00narrowPeakq\x15h\x12X\x03\x00\x00\x00bedq\x16h\x13h\x08}q\x17(h\x15K\x00N\x86q\x18h\x16K\x01N\x86q\x19uubX\x03\x00\x00\x00logq\x1acsnakemake.io\nLog\nq\x1b)\x81q\x1c}q\x1dh\x08}q\x1esbX\x06\x00\x00\x00paramsq\x1fcsnakemake.io\nParams\nq )\x81q!X"\x00\x00\x00peak_out/macs2/lm34_bg3_shep-gp_R1q"a}q#(X\x06\x00\x00\x00prefixq$h"h\x08}q%h$K\x00N\x86q&subX\x04\x00\x00\x00ruleq\'X\x05\x00\x00\x00macs2q(X\x05\x00\x00\x00inputq)csnakemake.io\nInputFiles\nq*)\x81q+(X\x1d\x00\x00\x00dedup/lm34_bg3_shep-gp_R1.bamq,X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq-e}q.(X\x02\x00\x00\x00ipq/h,h\x08}q0(h/K\x00N\x86q1X\x03\x00\x00\x00inpq2K\x01N\x86q3uh2h-ubX\t\x00\x00\x00wildcardsq4csnakemake.io\nWildcards\nq5)\x81q6X\x13\x00\x00\x00lm34_bg3_shep-gp_R1q7a}q8(X\x06\x00\x00\x00sampleq9h7h\x08}q:X\x06\x00\x00\x00sampleq;K\x00N\x86q<subX\x07\x00\x00\x00threadsq=K\x01ub.')
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
