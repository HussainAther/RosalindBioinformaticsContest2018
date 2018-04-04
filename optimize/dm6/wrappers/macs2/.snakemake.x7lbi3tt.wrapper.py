
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_coresq\x07K\x01X\x06\x00\x00\x00_namesq\x08}q\t(h\x07K\x00N\x86q\nX\x06\x00\x00\x00_nodesq\x0bK\x01N\x86q\x0cuh\x0bK\x01ubX\x03\x00\x00\x00logq\rcsnakemake.io\nLog\nq\x0e)\x81q\x0f}q\x10h\x08}q\x11sbX\x06\x00\x00\x00paramsq\x12csnakemake.io\nParams\nq\x13)\x81q\x14(X\x0f\x00\x00\x00sjl_mbn2_mod_R1q\x15X\x1e\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1q\x16e}q\x17(X\x0e\x00\x00\x00wrapper_sampleq\x18h\x15h\x08}q\x19(h\x18K\x00N\x86q\x1aX\x06\x00\x00\x00prefixq\x1bK\x01N\x86q\x1cuh\x1bh\x16ubX\x07\x00\x00\x00threadsq\x1dK\x01X\x04\x00\x00\x00ruleq\x1eX\x05\x00\x00\x00macs2q\x1fX\x06\x00\x00\x00configq }q!X\x06\x00\x00\x00outputq"csnakemake.io\nOutputFiles\nq#)\x81q$(X?\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1_peaks.narrowPeakq%X2\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1.bedq&e}q\'(X\n\x00\x00\x00narrowPeakq(h%X\x03\x00\x00\x00bedq)h&h\x08}q*(h(K\x00N\x86q+h)K\x01N\x86q,uubX\t\x00\x00\x00wildcardsq-csnakemake.io\nWildcards\nq.)\x81q/h\x15a}q0(X\x06\x00\x00\x00sampleq1h\x15h\x08}q2X\x06\x00\x00\x00sampleq3K\x00N\x86q4subX\x05\x00\x00\x00inputq5csnakemake.io\nInputFiles\nq6)\x81q7(X\x19\x00\x00\x00dedup/sjl_mbn2_mod_R1.bamq8X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq9e}q:(X\x02\x00\x00\x00ipq;h8X\x03\x00\x00\x00inpq<h9h\x08}q=(h;K\x00N\x86q>h<K\x01N\x86q?uubub.')
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
