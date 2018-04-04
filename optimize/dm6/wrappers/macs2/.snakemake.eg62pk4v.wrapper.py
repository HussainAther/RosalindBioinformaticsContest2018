
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X.\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1/sjl_s3_mod_R1.bedq\x06X;\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1/sjl_s3_mod_R1_peaks.narrowPeakq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x03\x00\x00\x00bedq\x0bK\x00N\x86q\x0cX\n\x00\x00\x00narrowPeakq\rK\x01N\x86q\x0euh\rh\x07h\x0bh\x06ubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11X\x1c\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1q\x12a}q\x13(h\t}q\x14X\x06\x00\x00\x00prefixq\x15K\x00N\x86q\x16sh\x15h\x12ubX\x05\x00\x00\x00inputq\x17csnakemake.io\nInputFiles\nq\x18)\x81q\x19(X\x17\x00\x00\x00dedup/sjl_s3_mod_R1.bamq\x1aX\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq\x1be}q\x1c(h\t}q\x1d(X\x02\x00\x00\x00ipq\x1eK\x00N\x86q\x1fX\x03\x00\x00\x00inpq K\x01N\x86q!uh\x1eh\x1ah h\x1bubX\x04\x00\x00\x00ruleq"X\x05\x00\x00\x00macs2q#X\t\x00\x00\x00resourcesq$csnakemake.io\nResources\nq%)\x81q&(K\x01K\x01e}q\'(h\t}q((X\x06\x00\x00\x00_coresq)K\x00N\x86q*X\x06\x00\x00\x00_nodesq+K\x01N\x86q,uh+K\x01h)K\x01ubX\t\x00\x00\x00wildcardsq-csnakemake.io\nWildcards\nq.)\x81q/X\r\x00\x00\x00sjl_s3_mod_R1q0a}q1(h\t}q2X\x06\x00\x00\x00sampleq3K\x00N\x86q4sX\x06\x00\x00\x00sampleq5h0ubX\x06\x00\x00\x00configq6}q7X\x07\x00\x00\x00threadsq8K\x01X\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\t}q=sbub.')
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
