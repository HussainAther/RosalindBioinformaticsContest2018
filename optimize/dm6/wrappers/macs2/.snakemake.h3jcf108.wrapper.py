
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x17\x00\x00\x00dedup/sjl_s3_mod_R1.bamq\x06X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq\x07e}q\x08(X\x02\x00\x00\x00ipq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\rh\x07ubX\x06\x00\x00\x00outputq\x0fcsnakemake.io\nOutputFiles\nq\x10)\x81q\x11(X;\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1/sjl_s3_mod_R1_peaks.narrowPeakq\x12X.\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1/sjl_s3_mod_R1.bedq\x13e}q\x14(X\n\x00\x00\x00narrowPeakq\x15h\x12X\x03\x00\x00\x00bedq\x16h\x13h\n}q\x17(h\x15K\x00N\x86q\x18h\x16K\x01N\x86q\x19uubX\x04\x00\x00\x00ruleq\x1aX\x05\x00\x00\x00macs2q\x1bX\t\x00\x00\x00wildcardsq\x1ccsnakemake.io\nWildcards\nq\x1d)\x81q\x1eX\r\x00\x00\x00sjl_s3_mod_R1q\x1fa}q (h\n}q!X\x06\x00\x00\x00sampleq"K\x00N\x86q#sX\x06\x00\x00\x00sampleq$h\x1fubX\x06\x00\x00\x00configq%}q&X\x03\x00\x00\x00logq\'csnakemake.io\nLog\nq()\x81q)}q*h\n}q+sbX\x06\x00\x00\x00paramsq,csnakemake.io\nParams\nq-)\x81q.X\x1c\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1q/a}q0(h\n}q1X\x06\x00\x00\x00prefixq2K\x00N\x86q3sh2h/ubX\t\x00\x00\x00resourcesq4csnakemake.io\nResources\nq5)\x81q6(K\x01K\x01e}q7(X\x06\x00\x00\x00_nodesq8K\x01h\n}q9(h8K\x00N\x86q:X\x06\x00\x00\x00_coresq;K\x01N\x86q<uh;K\x01ubX\x07\x00\x00\x00threadsq=K\x01ub.')
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
