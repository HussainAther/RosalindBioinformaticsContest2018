
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_namesq\x08}q\t(h\x07K\x00N\x86q\nX\x06\x00\x00\x00_coresq\x0bK\x01N\x86q\x0cuh\x0bK\x01ubX\t\x00\x00\x00wildcardsq\rcsnakemake.io\nWildcards\nq\x0e)\x81q\x0fX\x0e\x00\x00\x00sjl_cl8_mod_R1q\x10a}q\x11(h\x08}q\x12X\x06\x00\x00\x00sampleq\x13K\x00N\x86q\x14sX\x06\x00\x00\x00sampleq\x15h\x10ubX\x06\x00\x00\x00outputq\x16csnakemake.io\nOutputFiles\nq\x17)\x81q\x18(X0\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1/sjl_cl8_mod_R1.bedq\x19X=\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1/sjl_cl8_mod_R1_peaks.narrowPeakq\x1ae}q\x1b(h\x08}q\x1c(X\x03\x00\x00\x00bedq\x1dK\x00N\x86q\x1eX\n\x00\x00\x00narrowPeakq\x1fK\x01N\x86q uh\x1fh\x1ah\x1dh\x19ubX\x07\x00\x00\x00threadsq!K\x01X\x05\x00\x00\x00inputq"csnakemake.io\nInputFiles\nq#)\x81q$(X\x18\x00\x00\x00dedup/sjl_cl8_mod_R1.bamq%X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq&e}q\'(X\x02\x00\x00\x00ipq(h%h\x08}q)(h(K\x00N\x86q*X\x03\x00\x00\x00inpq+K\x01N\x86q,uh+h&ubX\x04\x00\x00\x00ruleq-X\x05\x00\x00\x00macs2q.X\x06\x00\x00\x00paramsq/csnakemake.io\nParams\nq0)\x81q1X\x1d\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1q2a}q3(X\x06\x00\x00\x00prefixq4h2h\x08}q5h4K\x00N\x86q6subX\x06\x00\x00\x00configq7}q8X\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x08}q=sbub.')
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
