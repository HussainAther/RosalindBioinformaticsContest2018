
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X4\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1.bedq\x06XA\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1_peaks.narrowPeakq\x07e}q\x08(X\x03\x00\x00\x00bedq\th\x06X\n\x00\x00\x00narrowPeakq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x03\x00\x00\x00logq\x0fcsnakemake.io\nLog\nq\x10)\x81q\x11}q\x12h\x0b}q\x13sbX\x05\x00\x00\x00inputq\x14csnakemake.io\nInputFiles\nq\x15)\x81q\x16(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x17X\x1a\x00\x00\x00dedup/sjl_mbn2_shep_R1.bamq\x18e}q\x19(X\x03\x00\x00\x00inpq\x1ah\x17h\x0b}q\x1b(h\x1aK\x00N\x86q\x1cX\x02\x00\x00\x00ipq\x1dK\x01N\x86q\x1euh\x1dh\x18ubX\t\x00\x00\x00wildcardsq\x1fcsnakemake.io\nWildcards\nq )\x81q!X\x10\x00\x00\x00sjl_mbn2_shep_R1q"a}q#(h\x0b}q$X\x06\x00\x00\x00sampleq%K\x00N\x86q&sX\x06\x00\x00\x00sampleq\'h"ubX\t\x00\x00\x00resourcesq(csnakemake.io\nResources\nq))\x81q*(K\x01K\x01e}q+(X\x06\x00\x00\x00_nodesq,K\x01h\x0b}q-(X\x06\x00\x00\x00_coresq.K\x00N\x86q/h,K\x01N\x86q0uh.K\x01ubX\x06\x00\x00\x00configq1}q2X\x06\x00\x00\x00paramsq3csnakemake.io\nParams\nq4)\x81q5X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1q6a}q7(h\x0b}q8X\x06\x00\x00\x00prefixq9K\x00N\x86q:sh9h6ubX\x07\x00\x00\x00threadsq;K\x01X\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=ub.')
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
