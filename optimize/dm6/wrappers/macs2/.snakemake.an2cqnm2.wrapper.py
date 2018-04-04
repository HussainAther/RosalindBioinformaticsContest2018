
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x04\x00\x00\x00ruleq\x05X\x05\x00\x00\x00macs2q\x06X\x06\x00\x00\x00paramsq\x07csnakemake.io\nParams\nq\x08)\x81q\tX\x1c\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1q\na}q\x0b(X\x06\x00\x00\x00prefixq\x0ch\nX\x06\x00\x00\x00_namesq\r}q\x0eh\x0cK\x00N\x86q\x0fsubX\x03\x00\x00\x00logq\x10csnakemake.io\nLog\nq\x11)\x81q\x12}q\x13h\r}q\x14sbX\t\x00\x00\x00wildcardsq\x15csnakemake.io\nWildcards\nq\x16)\x81q\x17X\r\x00\x00\x00sjl_s2_mod_R1q\x18a}q\x19(X\x06\x00\x00\x00sampleq\x1ah\x18h\r}q\x1bX\x06\x00\x00\x00sampleq\x1cK\x00N\x86q\x1dsubX\x07\x00\x00\x00threadsq\x1eK\x01X\t\x00\x00\x00resourcesq\x1fcsnakemake.io\nResources\nq )\x81q!(K\x01K\x01e}q"(X\x06\x00\x00\x00_nodesq#K\x01X\x06\x00\x00\x00_coresq$K\x01h\r}q%(h#K\x00N\x86q&h$K\x01N\x86q\'uubX\x05\x00\x00\x00inputq(csnakemake.io\nInputFiles\nq))\x81q*(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq+X\x17\x00\x00\x00dedup/sjl_s2_mod_R1.bamq,e}q-(X\x02\x00\x00\x00ipq.h,X\x03\x00\x00\x00inpq/h+h\r}q0(h/K\x00N\x86q1h.K\x01N\x86q2uubX\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X.\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1.bedq6X;\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1_peaks.narrowPeakq7e}q8(h\r}q9(X\x03\x00\x00\x00bedq:K\x00N\x86q;X\n\x00\x00\x00narrowPeakq<K\x01N\x86q=uh:h6h<h7ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.input.ip}_model.r')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
