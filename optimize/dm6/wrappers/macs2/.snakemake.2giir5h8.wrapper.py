
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x0f\x00\x00\x00sjl_s3_cp190_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00sampleq\nK\x00N\x86q\x0bsX\x06\x00\x00\x00sampleq\x0ch\x06ubX\x06\x00\x00\x00outputq\rcsnakemake.io\nOutputFiles\nq\x0e)\x81q\x0f(X2\x00\x00\x00peak_out/macs2/sjl_s3_cp190_R1/sjl_s3_cp190_R1.bedq\x10X?\x00\x00\x00peak_out/macs2/sjl_s3_cp190_R1/sjl_s3_cp190_R1_peaks.narrowPeakq\x11e}q\x12(X\x03\x00\x00\x00bedq\x13h\x10h\x08}q\x14(h\x13K\x00N\x86q\x15X\n\x00\x00\x00narrowPeakq\x16K\x01N\x86q\x17uh\x16h\x11ubX\x07\x00\x00\x00threadsq\x18K\x01X\t\x00\x00\x00resourcesq\x19csnakemake.io\nResources\nq\x1a)\x81q\x1b(K\x01K\x01e}q\x1c(h\x08}q\x1d(X\x06\x00\x00\x00_coresq\x1eK\x00N\x86q\x1fX\x06\x00\x00\x00_nodesq K\x01N\x86q!uh\x1eK\x01h K\x01ubX\x06\x00\x00\x00paramsq"csnakemake.io\nParams\nq#)\x81q$X\x1e\x00\x00\x00peak_out/macs2/sjl_s3_cp190_R1q%a}q&(h\x08}q\'X\x06\x00\x00\x00prefixq(K\x00N\x86q)sh(h%ubX\x06\x00\x00\x00configq*}q+X\x05\x00\x00\x00inputq,csnakemake.io\nInputFiles\nq-)\x81q.(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq/X\x19\x00\x00\x00dedup/sjl_s3_cp190_R1.bamq0e}q1(X\x03\x00\x00\x00inpq2h/X\x02\x00\x00\x00ipq3h0h\x08}q4(h2K\x00N\x86q5h3K\x01N\x86q6uubX\x04\x00\x00\x00ruleq7X\x05\x00\x00\x00macs2q8X\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x08}q=sbub.')
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
