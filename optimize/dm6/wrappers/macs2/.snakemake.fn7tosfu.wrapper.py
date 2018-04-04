
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x04\x00\x00\x00ruleq\x04X\x05\x00\x00\x00macs2q\x05X\x05\x00\x00\x00inputq\x06csnakemake.io\nInputFiles\nq\x07)\x81q\x08(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq\tX\x17\x00\x00\x00dedup/sjl_s3_mod_R1.bamq\ne}q\x0b(X\x03\x00\x00\x00inpq\x0ch\tX\x02\x00\x00\x00ipq\rh\nX\x06\x00\x00\x00_namesq\x0e}q\x0f(h\x0cK\x00N\x86q\x10h\rK\x01N\x86q\x11uubX\x03\x00\x00\x00logq\x12csnakemake.io\nLog\nq\x13)\x81q\x14}q\x15h\x0e}q\x16sbX\t\x00\x00\x00resourcesq\x17csnakemake.io\nResources\nq\x18)\x81q\x19(K\x01K\x01e}q\x1a(X\x06\x00\x00\x00_nodesq\x1bK\x01h\x0e}q\x1c(h\x1bK\x00N\x86q\x1dX\x06\x00\x00\x00_coresq\x1eK\x01N\x86q\x1fuh\x1eK\x01ubX\x06\x00\x00\x00outputq csnakemake.io\nOutputFiles\nq!)\x81q"(X;\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1/sjl_s3_mod_R1_peaks.narrowPeakq#X.\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1/sjl_s3_mod_R1.bedq$e}q%(X\n\x00\x00\x00narrowPeakq&h#X\x03\x00\x00\x00bedq\'h$h\x0e}q((h&K\x00N\x86q)h\'K\x01N\x86q*uubX\x06\x00\x00\x00configq+}q,X\x06\x00\x00\x00paramsq-csnakemake.io\nParams\nq.)\x81q/(X\r\x00\x00\x00sjl_s3_mod_R1q0X\x1c\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1q1e}q2(X\x06\x00\x00\x00prefixq3h1X\x0e\x00\x00\x00wrapper_sampleq4h0h\x0e}q5(h4K\x00N\x86q6h3K\x01N\x86q7uubX\t\x00\x00\x00wildcardsq8csnakemake.io\nWildcards\nq9)\x81q:h0a}q;(X\x06\x00\x00\x00sampleq<h0h\x0e}q=X\x06\x00\x00\x00sampleq>K\x00N\x86q?subub.')
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
