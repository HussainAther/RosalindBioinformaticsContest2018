
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x18\x00\x00\x00dedup/sjl_cl8_mod_R1.bamq\x06X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x07e}q\x08(X\x02\x00\x00\x00ipq\th\x06X\x03\x00\x00\x00inpq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x03\x00\x00\x00logq\x0fcsnakemake.io\nLog\nq\x10)\x81q\x11}q\x12h\x0b}q\x13sbX\t\x00\x00\x00wildcardsq\x14csnakemake.io\nWildcards\nq\x15)\x81q\x16X\x0e\x00\x00\x00sjl_cl8_mod_R1q\x17a}q\x18(X\x06\x00\x00\x00sampleq\x19h\x17h\x0b}q\x1aX\x06\x00\x00\x00sampleq\x1bK\x00N\x86q\x1csubX\t\x00\x00\x00resourcesq\x1dcsnakemake.io\nResources\nq\x1e)\x81q\x1f(K\x01K\x01e}q (X\x06\x00\x00\x00_nodesq!K\x01X\x06\x00\x00\x00_coresq"K\x01h\x0b}q#(h!K\x00N\x86q$h"K\x01N\x86q%uubX\x06\x00\x00\x00paramsq&csnakemake.io\nParams\nq\')\x81q(X\x1d\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1q)a}q*(X\x06\x00\x00\x00prefixq+h)h\x0b}q,h+K\x00N\x86q-subX\x04\x00\x00\x00ruleq.X\x05\x00\x00\x00macs2q/X\x06\x00\x00\x00configq0}q1X\x07\x00\x00\x00threadsq2K\x01X\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X=\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1/sjl_cl8_mod_R1_peaks.narrowPeakq6X0\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1/sjl_cl8_mod_R1.bedq7e}q8(X\n\x00\x00\x00narrowPeakq9h6X\x03\x00\x00\x00bedq:h7h\x0b}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubub.')
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
