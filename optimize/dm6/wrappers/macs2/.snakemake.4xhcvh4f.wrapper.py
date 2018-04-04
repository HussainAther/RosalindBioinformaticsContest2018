
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X6\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1.bedq\x06XC\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1_peaks.narrowPeakq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x03\x00\x00\x00bedq\x0bK\x00N\x86q\x0cX\n\x00\x00\x00narrowPeakq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\t\x00\x00\x00wildcardsq\x0fcsnakemake.io\nWildcards\nq\x10)\x81q\x11X\x11\x00\x00\x00sjl_mbn2_cp190_R1q\x12a}q\x13(h\t}q\x14X\x06\x00\x00\x00sampleq\x15K\x00N\x86q\x16sX\x06\x00\x00\x00sampleq\x17h\x12ubX\x06\x00\x00\x00paramsq\x18csnakemake.io\nParams\nq\x19)\x81q\x1aX \x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1q\x1ba}q\x1c(X\x06\x00\x00\x00prefixq\x1dh\x1bh\t}q\x1eh\x1dK\x00N\x86q\x1fsubX\t\x00\x00\x00resourcesq csnakemake.io\nResources\nq!)\x81q"(K\x01K\x01e}q#(X\x06\x00\x00\x00_nodesq$K\x01h\t}q%(h$K\x00N\x86q&X\x06\x00\x00\x00_coresq\'K\x01N\x86q(uh\'K\x01ubX\x03\x00\x00\x00logq)csnakemake.io\nLog\nq*)\x81q+}q,h\t}q-sbX\x07\x00\x00\x00threadsq.K\x01X\x05\x00\x00\x00inputq/csnakemake.io\nInputFiles\nq0)\x81q1(X\x1b\x00\x00\x00dedup/sjl_mbn2_cp190_R1.bamq2X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq3e}q4(h\t}q5(X\x02\x00\x00\x00ipq6K\x00N\x86q7X\x03\x00\x00\x00inpq8K\x01N\x86q9uh6h2h8h3ubX\x06\x00\x00\x00configq:}q;X\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=ub.')
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
