
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00paramsq\x04csnakemake.io\nParams\nq\x05)\x81q\x06X\x1f\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1q\x07a}q\x08(X\x06\x00\x00\x00_namesq\t}q\nX\x06\x00\x00\x00prefixq\x0bK\x00N\x86q\x0csh\x0bh\x07ubX\t\x00\x00\x00resourcesq\rcsnakemake.io\nResources\nq\x0e)\x81q\x0f(K\x01K\x01e}q\x10(h\t}q\x11(X\x06\x00\x00\x00_coresq\x12K\x00N\x86q\x13X\x06\x00\x00\x00_nodesq\x14K\x01N\x86q\x15uh\x12K\x01h\x14K\x01ubX\x03\x00\x00\x00logq\x16csnakemake.io\nLog\nq\x17)\x81q\x18}q\x19h\t}q\x1asbX\x06\x00\x00\x00configq\x1b}q\x1cX\x05\x00\x00\x00inputq\x1dcsnakemake.io\nInputFiles\nq\x1e)\x81q\x1f(X\x1a\x00\x00\x00dedup/sjl_cl8_cp190_R1.bamq X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq!e}q"(h\t}q#(X\x02\x00\x00\x00ipq$K\x00N\x86q%X\x03\x00\x00\x00inpq&K\x01N\x86q\'uh$h h&h!ubX\t\x00\x00\x00wildcardsq(csnakemake.io\nWildcards\nq))\x81q*X\x10\x00\x00\x00sjl_cl8_cp190_R1q+a}q,(h\t}q-X\x06\x00\x00\x00sampleq.K\x00N\x86q/sX\x06\x00\x00\x00sampleq0h+ubX\x04\x00\x00\x00ruleq1X\x05\x00\x00\x00macs2q2X\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X4\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1.bedq6XA\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1_peaks.narrowPeakq7e}q8(h\t}q9(X\n\x00\x00\x00narrowPeakq:K\x01N\x86q;X\x03\x00\x00\x00bedq<K\x00N\x86q=uh:h7h<h6ubub.')
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
