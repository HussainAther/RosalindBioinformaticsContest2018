
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X?\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1_peaks.narrowPeakq\x06X2\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1.bedq\x07e}q\x08(X\n\x00\x00\x00narrowPeakq\th\x06X\x03\x00\x00\x00bedq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x07\x00\x00\x00threadsq\x0fK\x01X\t\x00\x00\x00wildcardsq\x10csnakemake.io\nWildcards\nq\x11)\x81q\x12X\x0f\x00\x00\x00sjl_mbn2_mod_R1q\x13a}q\x14(h\x0b}q\x15X\x06\x00\x00\x00sampleq\x16K\x00N\x86q\x17sX\x06\x00\x00\x00sampleq\x18h\x13ubX\x04\x00\x00\x00ruleq\x19X\x05\x00\x00\x00macs2q\x1aX\x03\x00\x00\x00logq\x1bcsnakemake.io\nLog\nq\x1c)\x81q\x1d}q\x1eh\x0b}q\x1fsbX\x06\x00\x00\x00configq }q!X\x06\x00\x00\x00paramsq"csnakemake.io\nParams\nq#)\x81q$X\x1e\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1q%a}q&(h\x0b}q\'X\x06\x00\x00\x00prefixq(K\x00N\x86q)sh(h%ubX\t\x00\x00\x00resourcesq*csnakemake.io\nResources\nq+)\x81q,(K\x01K\x01e}q-(h\x0b}q.(X\x06\x00\x00\x00_coresq/K\x00N\x86q0X\x06\x00\x00\x00_nodesq1K\x01N\x86q2uh/K\x01h1K\x01ubX\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq6X\x19\x00\x00\x00dedup/sjl_mbn2_mod_R1.bamq7e}q8(X\x03\x00\x00\x00inpq9h6X\x02\x00\x00\x00ipq:h7h\x0b}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubub.')
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
