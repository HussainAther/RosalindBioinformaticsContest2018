
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\x05\x00\x00\x00inputq\x05csnakemake.io\nInputFiles\nq\x06)\x81q\x07(X\x1a\x00\x00\x00dedup/sjl_mbn2_suhw_R1.bamq\x08X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\te}q\n(X\x02\x00\x00\x00ipq\x0bh\x08X\x03\x00\x00\x00inpq\x0ch\tX\x06\x00\x00\x00_namesq\r}q\x0e(h\x0bK\x00N\x86q\x0fh\x0cK\x01N\x86q\x10uubX\x06\x00\x00\x00paramsq\x11csnakemake.io\nParams\nq\x12)\x81q\x13X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1q\x14a}q\x15(h\r}q\x16X\x06\x00\x00\x00prefixq\x17K\x00N\x86q\x18sh\x17h\x14ubX\x06\x00\x00\x00configq\x19}q\x1aX\x06\x00\x00\x00outputq\x1bcsnakemake.io\nOutputFiles\nq\x1c)\x81q\x1d(X4\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1.bedq\x1eXA\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1_peaks.narrowPeakq\x1fe}q (X\x03\x00\x00\x00bedq!h\x1eX\n\x00\x00\x00narrowPeakq"h\x1fh\r}q#(h!K\x00N\x86q$h"K\x01N\x86q%uubX\t\x00\x00\x00wildcardsq&csnakemake.io\nWildcards\nq\')\x81q(X\x10\x00\x00\x00sjl_mbn2_suhw_R1q)a}q*(h\r}q+X\x06\x00\x00\x00sampleq,K\x00N\x86q-sX\x06\x00\x00\x00sampleq.h)ubX\x07\x00\x00\x00threadsq/K\x01X\t\x00\x00\x00resourcesq0csnakemake.io\nResources\nq1)\x81q2(K\x01K\x01e}q3(h\r}q4(X\x06\x00\x00\x00_nodesq5K\x01N\x86q6X\x06\x00\x00\x00_coresq7K\x00N\x86q8uh5K\x01h7K\x01ubX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\r}q=sbub.')
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
shell('Rscript {snakemake.params.prefix}_model.r')
