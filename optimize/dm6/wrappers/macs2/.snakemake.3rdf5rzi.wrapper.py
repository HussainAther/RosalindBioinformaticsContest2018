
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x10\x00\x00\x00sjl_mbn2_suhw_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00sampleq\nK\x00N\x86q\x0bsX\x06\x00\x00\x00sampleq\x0ch\x06ubX\t\x00\x00\x00resourcesq\rcsnakemake.io\nResources\nq\x0e)\x81q\x0f(K\x01K\x01e}q\x10(X\x06\x00\x00\x00_coresq\x11K\x01h\x08}q\x12(X\x06\x00\x00\x00_nodesq\x13K\x00N\x86q\x14h\x11K\x01N\x86q\x15uh\x13K\x01ubX\x05\x00\x00\x00inputq\x16csnakemake.io\nInputFiles\nq\x17)\x81q\x18(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x19X\x1a\x00\x00\x00dedup/sjl_mbn2_suhw_R1.bamq\x1ae}q\x1b(X\x03\x00\x00\x00inpq\x1ch\x19h\x08}q\x1d(h\x1cK\x00N\x86q\x1eX\x02\x00\x00\x00ipq\x1fK\x01N\x86q uh\x1fh\x1aubX\x07\x00\x00\x00threadsq!K\x01X\x06\x00\x00\x00outputq"csnakemake.io\nOutputFiles\nq#)\x81q$(XA\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1_peaks.narrowPeakq%X4\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1.bedq&e}q\'(X\n\x00\x00\x00narrowPeakq(h%X\x03\x00\x00\x00bedq)h&h\x08}q*(h(K\x00N\x86q+h)K\x01N\x86q,uubX\x06\x00\x00\x00paramsq-csnakemake.io\nParams\nq.)\x81q/X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1q0a}q1(X\x06\x00\x00\x00prefixq2h0h\x08}q3h2K\x00N\x86q4subX\x04\x00\x00\x00ruleq5X\x05\x00\x00\x00macs2q6X\x06\x00\x00\x00configq7}q8X\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x08}q=sbub.')
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
