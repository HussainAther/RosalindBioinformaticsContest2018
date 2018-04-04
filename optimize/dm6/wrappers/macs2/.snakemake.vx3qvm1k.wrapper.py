
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\t\x00\x00\x00wildcardsq\x05csnakemake.io\nWildcards\nq\x06)\x81q\x07X\x0f\x00\x00\x00sjl_s2_cp190_R1q\x08a}q\t(X\x06\x00\x00\x00sampleq\nh\x08X\x06\x00\x00\x00_namesq\x0b}q\x0cX\x06\x00\x00\x00sampleq\rK\x00N\x86q\x0esubX\x04\x00\x00\x00ruleq\x0fX\x05\x00\x00\x00macs2q\x10X\t\x00\x00\x00resourcesq\x11csnakemake.io\nResources\nq\x12)\x81q\x13(K\x01K\x01e}q\x14(X\x06\x00\x00\x00_coresq\x15K\x01X\x06\x00\x00\x00_nodesq\x16K\x01h\x0b}q\x17(h\x15K\x00N\x86q\x18h\x16K\x01N\x86q\x19uubX\x06\x00\x00\x00paramsq\x1acsnakemake.io\nParams\nq\x1b)\x81q\x1cX\x1e\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1q\x1da}q\x1e(X\x06\x00\x00\x00prefixq\x1fh\x1dh\x0b}q h\x1fK\x00N\x86q!subX\x05\x00\x00\x00inputq"csnakemake.io\nInputFiles\nq#)\x81q$(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq%X\x19\x00\x00\x00dedup/sjl_s2_cp190_R1.bamq&e}q\'(X\x02\x00\x00\x00ipq(h&X\x03\x00\x00\x00inpq)h%h\x0b}q*(h)K\x00N\x86q+h(K\x01N\x86q,uubX\x03\x00\x00\x00logq-csnakemake.io\nLog\nq.)\x81q/}q0h\x0b}q1sbX\x07\x00\x00\x00threadsq2K\x01X\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X?\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1_peaks.narrowPeakq6X2\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1.bedq7e}q8(X\x03\x00\x00\x00bedq9h7X\n\x00\x00\x00narrowPeakq:h6h\x0b}q;(h:K\x00N\x86q<h9K\x01N\x86q=uubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.wildcards.sample}_model.r')
#shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
shell("cd {snakemake.params.prefix} && ln -sf $(basename {snakemake.output.narrowPeak}) $(basename {snakemake.output.bed})")
