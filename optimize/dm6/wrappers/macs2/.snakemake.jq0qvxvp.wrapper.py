
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X4\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1.bedq\x06XA\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1_peaks.narrowPeakq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x03\x00\x00\x00bedq\x0bK\x00N\x86q\x0cX\n\x00\x00\x00narrowPeakq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1q\x12a}q\x13(X\x06\x00\x00\x00prefixq\x14h\x12h\t}q\x15h\x14K\x00N\x86q\x16subX\x03\x00\x00\x00logq\x17csnakemake.io\nLog\nq\x18)\x81q\x19}q\x1ah\t}q\x1bsbX\t\x00\x00\x00resourcesq\x1ccsnakemake.io\nResources\nq\x1d)\x81q\x1e(K\x01K\x01e}q\x1f(X\x06\x00\x00\x00_nodesq K\x01h\t}q!(h K\x00N\x86q"X\x06\x00\x00\x00_coresq#K\x01N\x86q$uh#K\x01ubX\x05\x00\x00\x00inputq%csnakemake.io\nInputFiles\nq&)\x81q\'(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq(X\x1a\x00\x00\x00dedup/sjl_mbn2_shep_R1.bamq)e}q*(h\t}q+(X\x03\x00\x00\x00inpq,K\x00N\x86q-X\x02\x00\x00\x00ipq.K\x01N\x86q/uh,h(h.h)ubX\x04\x00\x00\x00ruleq0X\x05\x00\x00\x00macs2q1X\x07\x00\x00\x00threadsq2K\x01X\x06\x00\x00\x00configq3}q4X\t\x00\x00\x00wildcardsq5csnakemake.io\nWildcards\nq6)\x81q7X\x10\x00\x00\x00sjl_mbn2_shep_R1q8a}q9(h\t}q:X\x06\x00\x00\x00sampleq;K\x00N\x86q<sX\x06\x00\x00\x00sampleq=h8ubub.')
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
