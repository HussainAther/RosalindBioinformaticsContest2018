
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00configq\t}q\nX\x04\x00\x00\x00ruleq\x0bX\x05\x00\x00\x00macs2q\x0cX\t\x00\x00\x00wildcardsq\rcsnakemake.io\nWildcards\nq\x0e)\x81q\x0fX\r\x00\x00\x00sjl_kc_mod_R1q\x10a}q\x11(h\x07}q\x12X\x06\x00\x00\x00sampleq\x13K\x00N\x86q\x14sX\x06\x00\x00\x00sampleq\x15h\x10ubX\x06\x00\x00\x00paramsq\x16csnakemake.io\nParams\nq\x17)\x81q\x18X\x1c\x00\x00\x00peak_out/macs2/sjl_kc_mod_R1q\x19a}q\x1a(h\x07}q\x1bX\x06\x00\x00\x00prefixq\x1cK\x00N\x86q\x1dsh\x1ch\x19ubX\x06\x00\x00\x00outputq\x1ecsnakemake.io\nOutputFiles\nq\x1f)\x81q (X.\x00\x00\x00peak_out/macs2/sjl_kc_mod_R1/sjl_kc_mod_R1.bedq!X;\x00\x00\x00peak_out/macs2/sjl_kc_mod_R1/sjl_kc_mod_R1_peaks.narrowPeakq"e}q#(h\x07}q$(X\x03\x00\x00\x00bedq%K\x00N\x86q&X\n\x00\x00\x00narrowPeakq\'K\x01N\x86q(uh%h!h\'h"ubX\t\x00\x00\x00resourcesq)csnakemake.io\nResources\nq*)\x81q+(K\x01K\x01e}q,(X\x06\x00\x00\x00_nodesq-K\x01h\x07}q.(h-K\x00N\x86q/X\x06\x00\x00\x00_coresq0K\x01N\x86q1uh0K\x01ubX\x05\x00\x00\x00inputq2csnakemake.io\nInputFiles\nq3)\x81q4(X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq5X\x17\x00\x00\x00dedup/sjl_kc_mod_R1.bamq6e}q7(h\x07}q8(X\x03\x00\x00\x00inpq9K\x00N\x86q:X\x02\x00\x00\x00ipq;K\x01N\x86q<uh9h5h;h6ubX\x07\x00\x00\x00threadsq=K\x01ub.')
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
