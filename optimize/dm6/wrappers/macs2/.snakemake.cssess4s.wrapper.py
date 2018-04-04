
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\x06\x00\x00\x00paramsq\x05csnakemake.io\nParams\nq\x06)\x81q\x07X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1q\x08a}q\t(X\x06\x00\x00\x00prefixq\nh\x08X\x06\x00\x00\x00_namesq\x0b}q\x0ch\nK\x00N\x86q\rsubX\t\x00\x00\x00resourcesq\x0ecsnakemake.io\nResources\nq\x0f)\x81q\x10(K\x01K\x01e}q\x11(X\x06\x00\x00\x00_nodesq\x12K\x01X\x06\x00\x00\x00_coresq\x13K\x01h\x0b}q\x14(h\x12K\x01N\x86q\x15h\x13K\x00N\x86q\x16uubX\x05\x00\x00\x00inputq\x17csnakemake.io\nInputFiles\nq\x18)\x81q\x19(X\x1a\x00\x00\x00dedup/sjl_mbn2_shep_R1.bamq\x1aX\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x1be}q\x1c(X\x02\x00\x00\x00ipq\x1dh\x1ah\x0b}q\x1e(h\x1dK\x00N\x86q\x1fX\x03\x00\x00\x00inpq K\x01N\x86q!uh h\x1bubX\x07\x00\x00\x00threadsq"K\x01X\t\x00\x00\x00wildcardsq#csnakemake.io\nWildcards\nq$)\x81q%X\x10\x00\x00\x00sjl_mbn2_shep_R1q&a}q\'(X\x06\x00\x00\x00sampleq(h&h\x0b}q)X\x06\x00\x00\x00sampleq*K\x00N\x86q+subX\x06\x00\x00\x00outputq,csnakemake.io\nOutputFiles\nq-)\x81q.(XA\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1_peaks.narrowPeakq/X4\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1.bedq0e}q1(X\n\x00\x00\x00narrowPeakq2h/X\x03\x00\x00\x00bedq3h0h\x0b}q4(h2K\x00N\x86q5h3K\x01N\x86q6uubX\x06\x00\x00\x00configq7}q8X\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x0b}q=sbub.')
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
