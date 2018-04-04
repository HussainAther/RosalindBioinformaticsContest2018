
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00configq\t}q\nX\x07\x00\x00\x00threadsq\x0bK\x01X\x06\x00\x00\x00paramsq\x0ccsnakemake.io\nParams\nq\r)\x81q\x0e(X\x10\x00\x00\x00sjl_cl8_cp190_R1q\x0fX\x1f\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1q\x10e}q\x11(X\x0e\x00\x00\x00wrapper_sampleq\x12h\x0fX\x06\x00\x00\x00prefixq\x13h\x10h\x07}q\x14(h\x12K\x00N\x86q\x15h\x13K\x01N\x86q\x16uubX\t\x00\x00\x00wildcardsq\x17csnakemake.io\nWildcards\nq\x18)\x81q\x19h\x0fa}q\x1a(X\x06\x00\x00\x00sampleq\x1bh\x0fh\x07}q\x1cX\x06\x00\x00\x00sampleq\x1dK\x00N\x86q\x1esubX\t\x00\x00\x00resourcesq\x1fcsnakemake.io\nResources\nq )\x81q!(K\x01K\x01e}q"(X\x06\x00\x00\x00_coresq#K\x01X\x06\x00\x00\x00_nodesq$K\x01h\x07}q%(h$K\x00N\x86q&h#K\x01N\x86q\'uubX\x06\x00\x00\x00outputq(csnakemake.io\nOutputFiles\nq))\x81q*(X4\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1.bedq+XA\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1_peaks.narrowPeakq,e}q-(X\x03\x00\x00\x00bedq.h+X\n\x00\x00\x00narrowPeakq/h,h\x07}q0(h.K\x00N\x86q1h/K\x01N\x86q2uubX\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x1a\x00\x00\x00dedup/sjl_cl8_cp190_R1.bamq6X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq7e}q8(X\x02\x00\x00\x00ipq9h6X\x03\x00\x00\x00inpq:h7h\x07}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubX\x04\x00\x00\x00ruleq>X\x05\x00\x00\x00macs2q?ub.')
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
