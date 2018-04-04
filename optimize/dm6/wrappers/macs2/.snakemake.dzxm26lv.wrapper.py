
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x0f\x00\x00\x00sjl_cl8_shep_R1q\x06a}q\x07(X\x06\x00\x00\x00sampleq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nX\x06\x00\x00\x00sampleq\x0bK\x00N\x86q\x0csubX\x05\x00\x00\x00inputq\rcsnakemake.io\nInputFiles\nq\x0e)\x81q\x0f(X\x19\x00\x00\x00dedup/sjl_cl8_shep_R1.bamq\x10X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x11e}q\x12(X\x02\x00\x00\x00ipq\x13h\x10h\t}q\x14(h\x13K\x00N\x86q\x15X\x03\x00\x00\x00inpq\x16K\x01N\x86q\x17uh\x16h\x11ubX\t\x00\x00\x00resourcesq\x18csnakemake.io\nResources\nq\x19)\x81q\x1a(K\x01K\x01e}q\x1b(X\x06\x00\x00\x00_coresq\x1cK\x01X\x06\x00\x00\x00_nodesq\x1dK\x01h\t}q\x1e(h\x1cK\x00N\x86q\x1fh\x1dK\x01N\x86q uubX\x04\x00\x00\x00ruleq!X\x05\x00\x00\x00macs2q"X\x06\x00\x00\x00outputq#csnakemake.io\nOutputFiles\nq$)\x81q%(X2\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1.bedq&X?\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1_peaks.narrowPeakq\'e}q((h\t}q)(X\x03\x00\x00\x00bedq*K\x00N\x86q+X\n\x00\x00\x00narrowPeakq,K\x01N\x86q-uh*h&h,h\'ubX\x07\x00\x00\x00threadsq.K\x01X\x03\x00\x00\x00logq/csnakemake.io\nLog\nq0)\x81q1}q2h\t}q3sbX\x06\x00\x00\x00configq4}q5X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1q9a}q:(X\x06\x00\x00\x00prefixq;h9h\t}q<h;K\x00N\x86q=subub.')
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
