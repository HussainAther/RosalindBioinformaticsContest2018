
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x05\x00\x00\x00inputq\x04csnakemake.io\nInputFiles\nq\x05)\x81q\x06(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq\x07X\x18\x00\x00\x00dedup/sjl_s3_suhw_R1.bamq\x08e}q\t(X\x03\x00\x00\x00inpq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\nK\x00N\x86q\rX\x02\x00\x00\x00ipq\x0eK\x01N\x86q\x0fuh\x0eh\x08ubX\x04\x00\x00\x00ruleq\x10X\x05\x00\x00\x00macs2q\x11X\x06\x00\x00\x00outputq\x12csnakemake.io\nOutputFiles\nq\x13)\x81q\x14(X0\x00\x00\x00peak_out/macs2/sjl_s3_suhw_R1/sjl_s3_suhw_R1.bedq\x15X=\x00\x00\x00peak_out/macs2/sjl_s3_suhw_R1/sjl_s3_suhw_R1_peaks.narrowPeakq\x16e}q\x17(h\x0b}q\x18(X\x03\x00\x00\x00bedq\x19K\x00N\x86q\x1aX\n\x00\x00\x00narrowPeakq\x1bK\x01N\x86q\x1cuh\x19h\x15h\x1bh\x16ubX\t\x00\x00\x00wildcardsq\x1dcsnakemake.io\nWildcards\nq\x1e)\x81q\x1fX\x0e\x00\x00\x00sjl_s3_suhw_R1q a}q!(h\x0b}q"X\x06\x00\x00\x00sampleq#K\x00N\x86q$sX\x06\x00\x00\x00sampleq%h ubX\x03\x00\x00\x00logq&csnakemake.io\nLog\nq\')\x81q(}q)h\x0b}q*sbX\t\x00\x00\x00resourcesq+csnakemake.io\nResources\nq,)\x81q-(K\x01K\x01e}q.(h\x0b}q/(X\x06\x00\x00\x00_nodesq0K\x00N\x86q1X\x06\x00\x00\x00_coresq2K\x01N\x86q3uh0K\x01h2K\x01ubX\x06\x00\x00\x00configq4}q5X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8(h X\x1d\x00\x00\x00peak_out/macs2/sjl_s3_suhw_R1q9e}q:(h\x0b}q;(X\x0e\x00\x00\x00wrapper_sampleq<K\x00N\x86q=X\x06\x00\x00\x00prefixq>K\x01N\x86q?uh<h h>h9ubub.')
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
