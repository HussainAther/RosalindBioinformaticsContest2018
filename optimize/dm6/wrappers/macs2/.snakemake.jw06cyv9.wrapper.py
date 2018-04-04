
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00outputq\x04csnakemake.io\nOutputFiles\nq\x05)\x81q\x06(X0\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1.bedq\x07X=\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1_peaks.narrowPeakq\x08e}q\t(X\x03\x00\x00\x00bedq\nh\x07X\n\x00\x00\x00narrowPeakq\x0bh\x08X\x06\x00\x00\x00_namesq\x0c}q\r(h\nK\x00N\x86q\x0eh\x0bK\x01N\x86q\x0fuubX\t\x00\x00\x00wildcardsq\x10csnakemake.io\nWildcards\nq\x11)\x81q\x12X\x0e\x00\x00\x00sjl_s2_shep_R1q\x13a}q\x14(h\x0c}q\x15X\x06\x00\x00\x00sampleq\x16K\x00N\x86q\x17sX\x06\x00\x00\x00sampleq\x18h\x13ubX\t\x00\x00\x00resourcesq\x19csnakemake.io\nResources\nq\x1a)\x81q\x1b(K\x01K\x01e}q\x1c(h\x0c}q\x1d(X\x06\x00\x00\x00_coresq\x1eK\x00N\x86q\x1fX\x06\x00\x00\x00_nodesq K\x01N\x86q!uh\x1eK\x01h K\x01ubX\x04\x00\x00\x00ruleq"X\x05\x00\x00\x00macs2q#X\x05\x00\x00\x00inputq$csnakemake.io\nInputFiles\nq%)\x81q&(X\x18\x00\x00\x00dedup/sjl_s2_shep_R1.bamq\'X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq(e}q)(X\x03\x00\x00\x00inpq*h(X\x02\x00\x00\x00ipq+h\'h\x0c}q,(h+K\x00N\x86q-h*K\x01N\x86q.uubX\x06\x00\x00\x00paramsq/csnakemake.io\nParams\nq0)\x81q1X\x1d\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1q2a}q3(h\x0c}q4X\x06\x00\x00\x00prefixq5K\x00N\x86q6sh5h2ubX\x06\x00\x00\x00configq7}q8X\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x0c}q=sbub.')
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
