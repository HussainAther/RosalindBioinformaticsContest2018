
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\t\x00\x00\x00wildcardsq\x05csnakemake.io\nWildcards\nq\x06)\x81q\x07X\x10\x00\x00\x00sjl_cl8_cp190_R1q\x08a}q\t(X\x06\x00\x00\x00_namesq\n}q\x0bX\x06\x00\x00\x00sampleq\x0cK\x00N\x86q\rsX\x06\x00\x00\x00sampleq\x0eh\x08ubX\x04\x00\x00\x00ruleq\x0fX\x05\x00\x00\x00macs2q\x10X\x06\x00\x00\x00outputq\x11csnakemake.io\nOutputFiles\nq\x12)\x81q\x13(XA\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1_peaks.narrowPeakq\x14X4\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1.bedq\x15e}q\x16(X\n\x00\x00\x00narrowPeakq\x17h\x14h\n}q\x18(h\x17K\x00N\x86q\x19X\x03\x00\x00\x00bedq\x1aK\x01N\x86q\x1buh\x1ah\x15ubX\x07\x00\x00\x00threadsq\x1cK\x01X\t\x00\x00\x00resourcesq\x1dcsnakemake.io\nResources\nq\x1e)\x81q\x1f(K\x01K\x01e}q (h\n}q!(X\x06\x00\x00\x00_coresq"K\x00N\x86q#X\x06\x00\x00\x00_nodesq$K\x01N\x86q%uh"K\x01h$K\x01ubX\x06\x00\x00\x00paramsq&csnakemake.io\nParams\nq\')\x81q((X\x1f\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1q)h\x08e}q*(h\n}q+(X\x06\x00\x00\x00prefixq,K\x00N\x86q-X\x0e\x00\x00\x00wrapper_sampleq.K\x01N\x86q/uh,h)h.h\x08ubX\x05\x00\x00\x00inputq0csnakemake.io\nInputFiles\nq1)\x81q2(X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq3X\x1a\x00\x00\x00dedup/sjl_cl8_cp190_R1.bamq4e}q5(X\x03\x00\x00\x00inpq6h3h\n}q7(h6K\x00N\x86q8X\x02\x00\x00\x00ipq9K\x01N\x86q:uh9h4ubX\x03\x00\x00\x00logq;csnakemake.io\nLog\nq<)\x81q=}q>h\n}q?sbub.')
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
