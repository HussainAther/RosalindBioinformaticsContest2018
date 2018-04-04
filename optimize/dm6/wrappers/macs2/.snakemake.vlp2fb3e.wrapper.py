
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00paramsq\x04csnakemake.io\nParams\nq\x05)\x81q\x06X\x1c\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1q\x07a}q\x08(X\x06\x00\x00\x00prefixq\th\x07X\x06\x00\x00\x00_namesq\n}q\x0bh\tK\x00N\x86q\x0csubX\x06\x00\x00\x00outputq\rcsnakemake.io\nOutputFiles\nq\x0e)\x81q\x0f(X;\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1_peaks.narrowPeakq\x10X.\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1.bedq\x11e}q\x12(X\n\x00\x00\x00narrowPeakq\x13h\x10X\x03\x00\x00\x00bedq\x14h\x11h\n}q\x15(h\x13K\x00N\x86q\x16h\x14K\x01N\x86q\x17uubX\x04\x00\x00\x00ruleq\x18X\x05\x00\x00\x00macs2q\x19X\x03\x00\x00\x00logq\x1acsnakemake.io\nLog\nq\x1b)\x81q\x1c}q\x1dh\n}q\x1esbX\x06\x00\x00\x00configq\x1f}q X\x05\x00\x00\x00inputq!csnakemake.io\nInputFiles\nq")\x81q#(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq$X\x17\x00\x00\x00dedup/sjl_s2_mod_R1.bamq%e}q&(X\x03\x00\x00\x00inpq\'h$h\n}q((h\'K\x00N\x86q)X\x02\x00\x00\x00ipq*K\x01N\x86q+uh*h%ubX\t\x00\x00\x00wildcardsq,csnakemake.io\nWildcards\nq-)\x81q.X\r\x00\x00\x00sjl_s2_mod_R1q/a}q0(X\x06\x00\x00\x00sampleq1h/h\n}q2X\x06\x00\x00\x00sampleq3K\x00N\x86q4subX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_nodesq9K\x01h\n}q:(X\x06\x00\x00\x00_coresq;K\x00N\x86q<h9K\x01N\x86q=uh;K\x01ubub.')
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
