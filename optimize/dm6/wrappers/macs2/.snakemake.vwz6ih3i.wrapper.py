
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x04\x00\x00\x00ruleq\tX\x05\x00\x00\x00macs2q\nX\x06\x00\x00\x00configq\x0b}q\x0cX\t\x00\x00\x00resourcesq\rcsnakemake.io\nResources\nq\x0e)\x81q\x0f(K\x01K\x01e}q\x10(X\x06\x00\x00\x00_nodesq\x11K\x01X\x06\x00\x00\x00_coresq\x12K\x01h\x07}q\x13(h\x12K\x00N\x86q\x14h\x11K\x01N\x86q\x15uubX\x05\x00\x00\x00inputq\x16csnakemake.io\nInputFiles\nq\x17)\x81q\x18(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x19X\x17\x00\x00\x00dedup/sjl_s2_mod_R1.bamq\x1ae}q\x1b(X\x03\x00\x00\x00inpq\x1ch\x19X\x02\x00\x00\x00ipq\x1dh\x1ah\x07}q\x1e(h\x1cK\x00N\x86q\x1fh\x1dK\x01N\x86q uubX\x07\x00\x00\x00threadsq!K\x01X\t\x00\x00\x00wildcardsq"csnakemake.io\nWildcards\nq#)\x81q$X\r\x00\x00\x00sjl_s2_mod_R1q%a}q&(X\x06\x00\x00\x00sampleq\'h%h\x07}q(X\x06\x00\x00\x00sampleq)K\x00N\x86q*subX\x06\x00\x00\x00outputq+csnakemake.io\nOutputFiles\nq,)\x81q-(X.\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1.bedq.X;\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1_peaks.narrowPeakq/e}q0(X\x03\x00\x00\x00bedq1h.h\x07}q2(h1K\x00N\x86q3X\n\x00\x00\x00narrowPeakq4K\x01N\x86q5uh4h/ubX\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X\x1c\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1q9a}q:(X\x06\x00\x00\x00prefixq;h9h\x07}q<h;K\x00N\x86q=subub.')
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
