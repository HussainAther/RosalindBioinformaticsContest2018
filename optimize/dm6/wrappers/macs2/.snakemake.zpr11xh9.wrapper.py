
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x10\x00\x00\x00sjl_mbn2_suhw_R1q\x06a}q\x07(X\x06\x00\x00\x00sampleq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nX\x06\x00\x00\x00sampleq\x0bK\x00N\x86q\x0csubX\x06\x00\x00\x00outputq\rcsnakemake.io\nOutputFiles\nq\x0e)\x81q\x0f(X4\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1.bedq\x10XA\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1_peaks.narrowPeakq\x11e}q\x12(X\x03\x00\x00\x00bedq\x13h\x10X\n\x00\x00\x00narrowPeakq\x14h\x11h\t}q\x15(h\x13K\x00N\x86q\x16h\x14K\x01N\x86q\x17uubX\x03\x00\x00\x00logq\x18csnakemake.io\nLog\nq\x19)\x81q\x1a}q\x1bh\t}q\x1csbX\t\x00\x00\x00resourcesq\x1dcsnakemake.io\nResources\nq\x1e)\x81q\x1f(K\x01K\x01e}q (X\x06\x00\x00\x00_nodesq!K\x01h\t}q"(h!K\x00N\x86q#X\x06\x00\x00\x00_coresq$K\x01N\x86q%uh$K\x01ubX\x04\x00\x00\x00ruleq&X\x05\x00\x00\x00macs2q\'X\x06\x00\x00\x00configq(}q)X\x07\x00\x00\x00threadsq*K\x01X\x06\x00\x00\x00paramsq+csnakemake.io\nParams\nq,)\x81q-X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1q.a}q/(X\x06\x00\x00\x00prefixq0h.h\t}q1h0K\x00N\x86q2subX\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x1a\x00\x00\x00dedup/sjl_mbn2_suhw_R1.bamq6X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq7e}q8(X\x02\x00\x00\x00ipq9h6X\x03\x00\x00\x00inpq:h7h\t}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubub.')
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
