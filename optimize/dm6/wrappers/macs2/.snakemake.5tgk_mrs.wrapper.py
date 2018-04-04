
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\x03\x00\x00\x00logq\x05csnakemake.io\nLog\nq\x06)\x81q\x07}q\x08X\x06\x00\x00\x00_namesq\t}q\nsbX\x06\x00\x00\x00configq\x0b}q\x0cX\t\x00\x00\x00wildcardsq\rcsnakemake.io\nWildcards\nq\x0e)\x81q\x0fX\r\x00\x00\x00sjl_s2_mod_R1q\x10a}q\x11(X\x06\x00\x00\x00sampleq\x12h\x10h\t}q\x13X\x06\x00\x00\x00sampleq\x14K\x00N\x86q\x15subX\x05\x00\x00\x00inputq\x16csnakemake.io\nInputFiles\nq\x17)\x81q\x18(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x19X\x17\x00\x00\x00dedup/sjl_s2_mod_R1.bamq\x1ae}q\x1b(h\t}q\x1c(X\x03\x00\x00\x00inpq\x1dK\x00N\x86q\x1eX\x02\x00\x00\x00ipq\x1fK\x01N\x86q uh\x1dh\x19h\x1fh\x1aubX\t\x00\x00\x00resourcesq!csnakemake.io\nResources\nq")\x81q#(K\x01K\x01e}q$(X\x06\x00\x00\x00_coresq%K\x01X\x06\x00\x00\x00_nodesq&K\x01h\t}q\'(h%K\x00N\x86q(h&K\x01N\x86q)uubX\x06\x00\x00\x00outputq*csnakemake.io\nOutputFiles\nq+)\x81q,(X.\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1.bedq-X;\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1_peaks.narrowPeakq.e}q/(h\t}q0(X\x03\x00\x00\x00bedq1K\x00N\x86q2X\n\x00\x00\x00narrowPeakq3K\x01N\x86q4uh1h-h3h.ubX\x06\x00\x00\x00paramsq5csnakemake.io\nParams\nq6)\x81q7X\x1c\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1q8a}q9(X\x06\x00\x00\x00prefixq:h8h\t}q;h:K\x00N\x86q<subX\x07\x00\x00\x00threadsq=K\x01ub.')
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
