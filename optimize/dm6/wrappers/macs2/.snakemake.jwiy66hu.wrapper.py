
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x06\x00\x00\x00paramsq\x05csnakemake.io\nParams\nq\x06)\x81q\x07X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q\x08a}q\t(X\x06\x00\x00\x00prefixq\nh\x08X\x06\x00\x00\x00_namesq\x0b}q\x0ch\nK\x00N\x86q\rsubX\x04\x00\x00\x00ruleq\x0eX\x05\x00\x00\x00macs2q\x0fX\x03\x00\x00\x00logq\x10csnakemake.io\nLog\nq\x11)\x81q\x12}q\x13h\x0b}q\x14sbX\x06\x00\x00\x00outputq\x15csnakemake.io\nOutputFiles\nq\x16)\x81q\x17(X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq\x18X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq\x19e}q\x1a(X\n\x00\x00\x00narrowPeakq\x1bh\x18X\x03\x00\x00\x00bedq\x1ch\x19h\x0b}q\x1d(h\x1bK\x00N\x86q\x1eh\x1cK\x01N\x86q\x1fuubX\x07\x00\x00\x00threadsq K\x01X\x05\x00\x00\x00inputq!csnakemake.io\nInputFiles\nq")\x81q#(X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq$X\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq%e}q&(X\x03\x00\x00\x00inpq\'h$X\x02\x00\x00\x00ipq(h%h\x0b}q)(h\'K\x00N\x86q*h(K\x01N\x86q+uubX\t\x00\x00\x00resourcesq,csnakemake.io\nResources\nq-)\x81q.(K\x01K\x01e}q/(X\x06\x00\x00\x00_coresq0K\x01h\x0b}q1(h0K\x00N\x86q2X\x06\x00\x00\x00_nodesq3K\x01N\x86q4uh3K\x01ubX\t\x00\x00\x00wildcardsq5csnakemake.io\nWildcards\nq6)\x81q7X\x0e\x00\x00\x00sjl_kc_shep_R1q8a}q9(h\x0b}q:X\x06\x00\x00\x00sampleq;K\x00N\x86q<sX\x06\x00\x00\x00sampleq=h8ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.sample}_model.r')
