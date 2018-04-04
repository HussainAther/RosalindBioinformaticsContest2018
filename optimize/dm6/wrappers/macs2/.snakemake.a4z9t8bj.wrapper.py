
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00paramsq\tcsnakemake.io\nParams\nq\n)\x81q\x0b(X \x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1q\x0cX\x11\x00\x00\x00sjl_mbn2_cp190_R1q\re}q\x0e(h\x07}q\x0f(X\x06\x00\x00\x00prefixq\x10K\x00N\x86q\x11X\x0e\x00\x00\x00wrapper_sampleq\x12K\x01N\x86q\x13uh\x10h\x0ch\x12h\rubX\t\x00\x00\x00resourcesq\x14csnakemake.io\nResources\nq\x15)\x81q\x16(K\x01K\x01e}q\x17(h\x07}q\x18(X\x06\x00\x00\x00_nodesq\x19K\x00N\x86q\x1aX\x06\x00\x00\x00_coresq\x1bK\x01N\x86q\x1cuh\x19K\x01h\x1bK\x01ubX\x07\x00\x00\x00threadsq\x1dK\x01X\x05\x00\x00\x00inputq\x1ecsnakemake.io\nInputFiles\nq\x1f)\x81q (X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq!X\x1b\x00\x00\x00dedup/sjl_mbn2_cp190_R1.bamq"e}q#(h\x07}q$(X\x03\x00\x00\x00inpq%K\x00N\x86q&X\x02\x00\x00\x00ipq\'K\x01N\x86q(uh%h!h\'h"ubX\t\x00\x00\x00wildcardsq)csnakemake.io\nWildcards\nq*)\x81q+h\ra}q,(h\x07}q-X\x06\x00\x00\x00sampleq.K\x00N\x86q/sX\x06\x00\x00\x00sampleq0h\rubX\x06\x00\x00\x00configq1}q2X\x04\x00\x00\x00ruleq3X\x05\x00\x00\x00macs2q4X\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(XC\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1_peaks.narrowPeakq8X6\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1.bedq9e}q:(h\x07}q;(X\n\x00\x00\x00narrowPeakq<K\x00N\x86q=X\x03\x00\x00\x00bedq>K\x01N\x86q?uh<h8h>h9ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.r > {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.pdf')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
