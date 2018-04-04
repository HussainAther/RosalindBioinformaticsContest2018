
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05X"\x00\x00\x00peak_out/macs2/lm35_bg3_shep-r5_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00prefixq\nK\x00N\x86q\x0bsh\nh\x06ubX\x03\x00\x00\x00logq\x0ccsnakemake.io\nLog\nq\r)\x81q\x0e}q\x0fh\x08}q\x10sbX\x07\x00\x00\x00threadsq\x11K\x01X\t\x00\x00\x00wildcardsq\x12csnakemake.io\nWildcards\nq\x13)\x81q\x14X\x13\x00\x00\x00lm35_bg3_shep-r5_R1q\x15a}q\x16(h\x08}q\x17X\x06\x00\x00\x00sampleq\x18K\x00N\x86q\x19sX\x06\x00\x00\x00sampleq\x1ah\x15ubX\x06\x00\x00\x00outputq\x1bcsnakemake.io\nOutputFiles\nq\x1c)\x81q\x1d(XG\x00\x00\x00peak_out/macs2/lm35_bg3_shep-r5_R1/lm35_bg3_shep-r5_R1_peaks.narrowPeakq\x1eX:\x00\x00\x00peak_out/macs2/lm35_bg3_shep-r5_R1/lm35_bg3_shep-r5_R1.bedq\x1fe}q (h\x08}q!(X\n\x00\x00\x00narrowPeakq"K\x00N\x86q#X\x03\x00\x00\x00bedq$K\x01N\x86q%uh"h\x1eh$h\x1fubX\x04\x00\x00\x00ruleq&X\x05\x00\x00\x00macs2q\'X\x05\x00\x00\x00inputq(csnakemake.io\nInputFiles\nq))\x81q*(X\x1d\x00\x00\x00dedup/lm35_bg3_shep-r5_R1.bamq+X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq,e}q-(h\x08}q.(X\x02\x00\x00\x00ipq/K\x00N\x86q0X\x03\x00\x00\x00inpq1K\x01N\x86q2uh/h+h1h,ubX\t\x00\x00\x00resourcesq3csnakemake.io\nResources\nq4)\x81q5(K\x01K\x01e}q6(h\x08}q7(X\x06\x00\x00\x00_coresq8K\x00N\x86q9X\x06\x00\x00\x00_nodesq:K\x01N\x86q;uh8K\x01h:K\x01ubX\x06\x00\x00\x00configq<}q=ub.')
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
