
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x04\x00\x00\x00ruleq\x05X\x05\x00\x00\x00macs2q\x06X\x05\x00\x00\x00inputq\x07csnakemake.io\nInputFiles\nq\x08)\x81q\t(X\x17\x00\x00\x00dedup/sjl_s2_mod_R1.bamq\nX\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x0be}q\x0c(X\x06\x00\x00\x00_namesq\r}q\x0e(X\x02\x00\x00\x00ipq\x0fK\x00N\x86q\x10X\x03\x00\x00\x00inpq\x11K\x01N\x86q\x12uh\x0fh\nh\x11h\x0bubX\x07\x00\x00\x00threadsq\x13K\x01X\t\x00\x00\x00wildcardsq\x14csnakemake.io\nWildcards\nq\x15)\x81q\x16X\r\x00\x00\x00sjl_s2_mod_R1q\x17a}q\x18(X\x06\x00\x00\x00sampleq\x19h\x17h\r}q\x1aX\x06\x00\x00\x00sampleq\x1bK\x00N\x86q\x1csubX\x06\x00\x00\x00paramsq\x1dcsnakemake.io\nParams\nq\x1e)\x81q\x1f(h\x17X\x1c\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1q e}q!(X\x06\x00\x00\x00prefixq"h X\x0e\x00\x00\x00wrapper_sampleq#h\x17h\r}q$(h#K\x00N\x86q%h"K\x01N\x86q&uubX\t\x00\x00\x00resourcesq\'csnakemake.io\nResources\nq()\x81q)(K\x01K\x01e}q*(X\x06\x00\x00\x00_coresq+K\x01X\x06\x00\x00\x00_nodesq,K\x01h\r}q-(h,K\x00N\x86q.h+K\x01N\x86q/uubX\x03\x00\x00\x00logq0csnakemake.io\nLog\nq1)\x81q2}q3h\r}q4sbX\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(X;\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1_peaks.narrowPeakq8X.\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1.bedq9e}q:(X\n\x00\x00\x00narrowPeakq;h8h\r}q<(h;K\x00N\x86q=X\x03\x00\x00\x00bedq>K\x01N\x86q?uh>h9ubub.')
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
