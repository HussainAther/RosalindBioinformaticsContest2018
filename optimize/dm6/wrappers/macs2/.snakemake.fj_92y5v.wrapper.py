
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X6\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1.bedq\x06XC\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1_peaks.narrowPeakq\x07e}q\x08(X\x03\x00\x00\x00bedq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\n\x00\x00\x00narrowPeakq\rK\x01N\x86q\x0euh\rh\x07ubX\t\x00\x00\x00wildcardsq\x0fcsnakemake.io\nWildcards\nq\x10)\x81q\x11X\x11\x00\x00\x00sjl_mbn2_cp190_R1q\x12a}q\x13(X\x06\x00\x00\x00sampleq\x14h\x12h\n}q\x15X\x06\x00\x00\x00sampleq\x16K\x00N\x86q\x17subX\x03\x00\x00\x00logq\x18csnakemake.io\nLog\nq\x19)\x81q\x1a}q\x1bh\n}q\x1csbX\t\x00\x00\x00resourcesq\x1dcsnakemake.io\nResources\nq\x1e)\x81q\x1f(K\x01K\x01e}q (X\x06\x00\x00\x00_nodesq!K\x01X\x06\x00\x00\x00_coresq"K\x01h\n}q#(h!K\x00N\x86q$h"K\x01N\x86q%uubX\x06\x00\x00\x00paramsq&csnakemake.io\nParams\nq\')\x81q((h\x12X \x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1q)e}q*(X\x06\x00\x00\x00prefixq+h)X\x0e\x00\x00\x00wrapper_sampleq,h\x12h\n}q-(h,K\x00N\x86q.h+K\x01N\x86q/uubX\x06\x00\x00\x00configq0}q1X\x04\x00\x00\x00ruleq2X\x05\x00\x00\x00macs2q3X\x05\x00\x00\x00inputq4csnakemake.io\nInputFiles\nq5)\x81q6(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq7X\x1b\x00\x00\x00dedup/sjl_mbn2_cp190_R1.bamq8e}q9(X\x03\x00\x00\x00inpq:h7X\x02\x00\x00\x00ipq;h8h\n}q<(h:K\x00N\x86q=h;K\x01N\x86q>uubX\x07\x00\x00\x00threadsq?K\x01ub.')
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
