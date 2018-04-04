
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x0f\x00\x00\x00sjl_s2_cp190_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00sampleq\nK\x00N\x86q\x0bsX\x06\x00\x00\x00sampleq\x0ch\x06ubX\x06\x00\x00\x00paramsq\rcsnakemake.io\nParams\nq\x0e)\x81q\x0fX\x1e\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1q\x10a}q\x11(h\x08}q\x12X\x06\x00\x00\x00prefixq\x13K\x00N\x86q\x14sh\x13h\x10ubX\t\x00\x00\x00resourcesq\x15csnakemake.io\nResources\nq\x16)\x81q\x17(K\x01K\x01e}q\x18(h\x08}q\x19(X\x06\x00\x00\x00_nodesq\x1aK\x00N\x86q\x1bX\x06\x00\x00\x00_coresq\x1cK\x01N\x86q\x1duh\x1aK\x01h\x1cK\x01ubX\x07\x00\x00\x00threadsq\x1eK\x01X\x04\x00\x00\x00ruleq\x1fX\x05\x00\x00\x00macs2q X\x05\x00\x00\x00inputq!csnakemake.io\nInputFiles\nq")\x81q#(X\x19\x00\x00\x00dedup/sjl_s2_cp190_R1.bamq$X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq%e}q&(X\x02\x00\x00\x00ipq\'h$h\x08}q((h\'K\x00N\x86q)X\x03\x00\x00\x00inpq*K\x01N\x86q+uh*h%ubX\x03\x00\x00\x00logq,csnakemake.io\nLog\nq-)\x81q.}q/h\x08}q0sbX\x06\x00\x00\x00outputq1csnakemake.io\nOutputFiles\nq2)\x81q3(X2\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1.bedq4X?\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1_peaks.narrowPeakq5e}q6(X\x03\x00\x00\x00bedq7h4h\x08}q8(h7K\x00N\x86q9X\n\x00\x00\x00narrowPeakq:K\x01N\x86q;uh:h5ubX\x06\x00\x00\x00configq<}q=ub.')
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
