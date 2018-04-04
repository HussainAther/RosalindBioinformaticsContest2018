
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\x06\x00\x00\x00outputq\x05csnakemake.io\nOutputFiles\nq\x06)\x81q\x07(XC\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1_peaks.narrowPeakq\x08X6\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1.bedq\te}q\n(X\n\x00\x00\x00narrowPeakq\x0bh\x08X\x06\x00\x00\x00_namesq\x0c}q\r(h\x0bK\x00N\x86q\x0eX\x03\x00\x00\x00bedq\x0fK\x01N\x86q\x10uh\x0fh\tubX\x03\x00\x00\x00logq\x11csnakemake.io\nLog\nq\x12)\x81q\x13}q\x14h\x0c}q\x15sbX\x07\x00\x00\x00threadsq\x16K\x01X\x06\x00\x00\x00paramsq\x17csnakemake.io\nParams\nq\x18)\x81q\x19X \x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1q\x1aa}q\x1b(h\x0c}q\x1cX\x06\x00\x00\x00prefixq\x1dK\x00N\x86q\x1esh\x1dh\x1aubX\x05\x00\x00\x00inputq\x1fcsnakemake.io\nInputFiles\nq )\x81q!(X\x1b\x00\x00\x00dedup/sjl_mbn2_cp190_R1.bamq"X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq#e}q$(X\x03\x00\x00\x00inpq%h#X\x02\x00\x00\x00ipq&h"h\x0c}q\'(h&K\x00N\x86q(h%K\x01N\x86q)uubX\t\x00\x00\x00resourcesq*csnakemake.io\nResources\nq+)\x81q,(K\x01K\x01e}q-(h\x0c}q.(X\x06\x00\x00\x00_nodesq/K\x00N\x86q0X\x06\x00\x00\x00_coresq1K\x01N\x86q2uh/K\x01h1K\x01ubX\t\x00\x00\x00wildcardsq3csnakemake.io\nWildcards\nq4)\x81q5X\x11\x00\x00\x00sjl_mbn2_cp190_R1q6a}q7(h\x0c}q8X\x06\x00\x00\x00sampleq9K\x00N\x86q:sX\x06\x00\x00\x00sampleq;h6ubX\x06\x00\x00\x00configq<}q=ub.')
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
