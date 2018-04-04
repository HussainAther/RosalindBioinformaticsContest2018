
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\t\x00\x00\x00resourcesq\x05csnakemake.io\nResources\nq\x06)\x81q\x07(K\x01K\x01e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x06\x00\x00\x00_coresq\x0bK\x00N\x86q\x0cX\x06\x00\x00\x00_nodesq\rK\x01N\x86q\x0euh\rK\x01h\x0bK\x01ubX\x03\x00\x00\x00logq\x0fcsnakemake.io\nLog\nq\x10)\x81q\x11}q\x12h\t}q\x13sbX\t\x00\x00\x00wildcardsq\x14csnakemake.io\nWildcards\nq\x15)\x81q\x16X\x0f\x00\x00\x00sjl_cl8_shep_R1q\x17a}q\x18(h\t}q\x19X\x06\x00\x00\x00sampleq\x1aK\x00N\x86q\x1bsX\x06\x00\x00\x00sampleq\x1ch\x17ubX\x07\x00\x00\x00threadsq\x1dK\x01X\x04\x00\x00\x00ruleq\x1eX\x05\x00\x00\x00macs2q\x1fX\x05\x00\x00\x00inputq csnakemake.io\nInputFiles\nq!)\x81q"(X\x19\x00\x00\x00dedup/sjl_cl8_shep_R1.bamq#X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq$e}q%(X\x02\x00\x00\x00ipq&h#h\t}q\'(h&K\x00N\x86q(X\x03\x00\x00\x00inpq)K\x01N\x86q*uh)h$ubX\x06\x00\x00\x00paramsq+csnakemake.io\nParams\nq,)\x81q-(X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1q.h\x17e}q/(h\t}q0(X\x06\x00\x00\x00prefixq1K\x00N\x86q2X\x0e\x00\x00\x00wrapper_sampleq3K\x01N\x86q4uh1h.h3h\x17ubX\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(X?\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1_peaks.narrowPeakq8X2\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1.bedq9e}q:(X\n\x00\x00\x00narrowPeakq;h8X\x03\x00\x00\x00bedq<h9h\t}q=(h;K\x00N\x86q>h<K\x01N\x86q?uubub.')
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
