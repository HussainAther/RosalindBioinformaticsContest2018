
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x03\x00\x00\x00logq\x05csnakemake.io\nLog\nq\x06)\x81q\x07}q\x08X\x06\x00\x00\x00_namesq\t}q\nsbX\x05\x00\x00\x00inputq\x0bcsnakemake.io\nInputFiles\nq\x0c)\x81q\r(X\x18\x00\x00\x00dedup/sjl_cl8_mod_R1.bamq\x0eX\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x0fe}q\x10(X\x02\x00\x00\x00ipq\x11h\x0eX\x03\x00\x00\x00inpq\x12h\x0fh\t}q\x13(h\x11K\x00N\x86q\x14h\x12K\x01N\x86q\x15uubX\t\x00\x00\x00wildcardsq\x16csnakemake.io\nWildcards\nq\x17)\x81q\x18X\x0e\x00\x00\x00sjl_cl8_mod_R1q\x19a}q\x1a(X\x06\x00\x00\x00sampleq\x1bh\x19h\t}q\x1cX\x06\x00\x00\x00sampleq\x1dK\x00N\x86q\x1esubX\x04\x00\x00\x00ruleq\x1fX\x05\x00\x00\x00macs2q X\t\x00\x00\x00resourcesq!csnakemake.io\nResources\nq")\x81q#(K\x01K\x01e}q$(X\x06\x00\x00\x00_nodesq%K\x01X\x06\x00\x00\x00_coresq&K\x01h\t}q\'(h&K\x00N\x86q(h%K\x01N\x86q)uubX\x06\x00\x00\x00outputq*csnakemake.io\nOutputFiles\nq+)\x81q,(X0\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1/sjl_cl8_mod_R1.bedq-X=\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1/sjl_cl8_mod_R1_peaks.narrowPeakq.e}q/(X\x03\x00\x00\x00bedq0h-X\n\x00\x00\x00narrowPeakq1h.h\t}q2(h0K\x00N\x86q3h1K\x01N\x86q4uubX\x06\x00\x00\x00paramsq5csnakemake.io\nParams\nq6)\x81q7(X\x1d\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1q8h\x19e}q9(X\x0e\x00\x00\x00wrapper_sampleq:h\x19X\x06\x00\x00\x00prefixq;h8h\t}q<(h;K\x00N\x86q=h:K\x01N\x86q>uubX\x07\x00\x00\x00threadsq?K\x01ub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.r')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
