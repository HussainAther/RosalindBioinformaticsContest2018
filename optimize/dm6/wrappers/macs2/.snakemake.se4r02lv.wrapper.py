
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\x06\x00\x00\x00outputq\x05csnakemake.io\nOutputFiles\nq\x06)\x81q\x07(X;\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1_peaks.narrowPeakq\x08X.\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1.bedq\te}q\n(X\n\x00\x00\x00narrowPeakq\x0bh\x08X\x06\x00\x00\x00_namesq\x0c}q\r(h\x0bK\x00N\x86q\x0eX\x03\x00\x00\x00bedq\x0fK\x01N\x86q\x10uh\x0fh\tubX\t\x00\x00\x00resourcesq\x11csnakemake.io\nResources\nq\x12)\x81q\x13(K\x01K\x01e}q\x14(X\x06\x00\x00\x00_coresq\x15K\x01X\x06\x00\x00\x00_nodesq\x16K\x01h\x0c}q\x17(h\x16K\x00N\x86q\x18h\x15K\x01N\x86q\x19uubX\x03\x00\x00\x00logq\x1acsnakemake.io\nLog\nq\x1b)\x81q\x1c}q\x1dh\x0c}q\x1esbX\x05\x00\x00\x00inputq\x1fcsnakemake.io\nInputFiles\nq )\x81q!(X\x17\x00\x00\x00dedup/sjl_s2_mod_R1.bamq"X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq#e}q$(X\x02\x00\x00\x00ipq%h"h\x0c}q&(h%K\x00N\x86q\'X\x03\x00\x00\x00inpq(K\x01N\x86q)uh(h#ubX\t\x00\x00\x00wildcardsq*csnakemake.io\nWildcards\nq+)\x81q,X\r\x00\x00\x00sjl_s2_mod_R1q-a}q.(X\x06\x00\x00\x00sampleq/h-h\x0c}q0X\x06\x00\x00\x00sampleq1K\x00N\x86q2subX\x06\x00\x00\x00configq3}q4X\x07\x00\x00\x00threadsq5K\x01X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8(h-X\x1c\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1q9e}q:(X\x0e\x00\x00\x00wrapper_sampleq;h-X\x06\x00\x00\x00prefixq<h9h\x0c}q=(h;K\x00N\x86q>h<K\x01N\x86q?uubub.')
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
