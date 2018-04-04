
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x05\x00\x00\x00inputq\x04csnakemake.io\nInputFiles\nq\x05)\x81q\x06(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x07X\x18\x00\x00\x00dedup/sjl_s2_shep_R1.bamq\x08e}q\t(X\x03\x00\x00\x00inpq\nh\x07X\x02\x00\x00\x00ipq\x0bh\x08X\x06\x00\x00\x00_namesq\x0c}q\r(h\nK\x00N\x86q\x0eh\x0bK\x01N\x86q\x0fuubX\t\x00\x00\x00wildcardsq\x10csnakemake.io\nWildcards\nq\x11)\x81q\x12X\x0e\x00\x00\x00sjl_s2_shep_R1q\x13a}q\x14(X\x06\x00\x00\x00sampleq\x15h\x13h\x0c}q\x16X\x06\x00\x00\x00sampleq\x17K\x00N\x86q\x18subX\x06\x00\x00\x00configq\x19}q\x1aX\x03\x00\x00\x00logq\x1bcsnakemake.io\nLog\nq\x1c)\x81q\x1d}q\x1eh\x0c}q\x1fsbX\x06\x00\x00\x00outputq csnakemake.io\nOutputFiles\nq!)\x81q"(X=\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1_peaks.narrowPeakq#X0\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1.bedq$e}q%(X\n\x00\x00\x00narrowPeakq&h#X\x03\x00\x00\x00bedq\'h$h\x0c}q((h&K\x00N\x86q)h\'K\x01N\x86q*uubX\x04\x00\x00\x00ruleq+X\x05\x00\x00\x00macs2q,X\x06\x00\x00\x00paramsq-csnakemake.io\nParams\nq.)\x81q/X\x1d\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1q0a}q1(X\x06\x00\x00\x00prefixq2h0h\x0c}q3h2K\x00N\x86q4subX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_nodesq9K\x01X\x06\x00\x00\x00_coresq:K\x01h\x0c}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubub.')
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
shell('touch {snakemake.output.bed}')
shell('Rscript peak_out/macs2/{snakemake.params.prefix}_model.r')
