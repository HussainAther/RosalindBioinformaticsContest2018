
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x0f\x00\x00\x00sjl_cl8_shep_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00sampleq\nK\x00N\x86q\x0bsX\x06\x00\x00\x00sampleq\x0ch\x06ubX\x06\x00\x00\x00paramsq\rcsnakemake.io\nParams\nq\x0e)\x81q\x0fX\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1q\x10a}q\x11(h\x08}q\x12X\x06\x00\x00\x00prefixq\x13K\x00N\x86q\x14sh\x13h\x10ubX\x05\x00\x00\x00inputq\x15csnakemake.io\nInputFiles\nq\x16)\x81q\x17(X\x19\x00\x00\x00dedup/sjl_cl8_shep_R1.bamq\x18X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x19e}q\x1a(X\x03\x00\x00\x00inpq\x1bh\x19X\x02\x00\x00\x00ipq\x1ch\x18h\x08}q\x1d(h\x1cK\x00N\x86q\x1eh\x1bK\x01N\x86q\x1fuubX\x07\x00\x00\x00threadsq K\x01X\x06\x00\x00\x00outputq!csnakemake.io\nOutputFiles\nq")\x81q#(X?\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1_peaks.narrowPeakq$X2\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1.bedq%e}q&(X\n\x00\x00\x00narrowPeakq\'h$X\x03\x00\x00\x00bedq(h%h\x08}q)(h\'K\x00N\x86q*h(K\x01N\x86q+uubX\x04\x00\x00\x00ruleq,X\x05\x00\x00\x00macs2q-X\t\x00\x00\x00resourcesq.csnakemake.io\nResources\nq/)\x81q0(K\x01K\x01e}q1(h\x08}q2(X\x06\x00\x00\x00_nodesq3K\x00N\x86q4X\x06\x00\x00\x00_coresq5K\x01N\x86q6uh3K\x01h5K\x01ubX\x03\x00\x00\x00logq7csnakemake.io\nLog\nq8)\x81q9}q:h\x08}q;sbX\x06\x00\x00\x00configq<}q=ub.')
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
