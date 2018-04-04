
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x19\x00\x00\x00dedup/sjl_mbn2_mod_R1.bamq\x06X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x02\x00\x00\x00ipq\x0bK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x03\x00\x00\x00logq\x0fcsnakemake.io\nLog\nq\x10)\x81q\x11}q\x12h\t}q\x13sbX\x06\x00\x00\x00configq\x14}q\x15X\x06\x00\x00\x00outputq\x16csnakemake.io\nOutputFiles\nq\x17)\x81q\x18(X?\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1_peaks.narrowPeakq\x19X2\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1.bedq\x1ae}q\x1b(X\n\x00\x00\x00narrowPeakq\x1ch\x19X\x03\x00\x00\x00bedq\x1dh\x1ah\t}q\x1e(h\x1cK\x00N\x86q\x1fh\x1dK\x01N\x86q uubX\x06\x00\x00\x00paramsq!csnakemake.io\nParams\nq")\x81q#X\x1e\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1q$a}q%(h\t}q&X\x06\x00\x00\x00prefixq\'K\x00N\x86q(sh\'h$ubX\x07\x00\x00\x00threadsq)K\x01X\x04\x00\x00\x00ruleq*X\x05\x00\x00\x00macs2q+X\t\x00\x00\x00wildcardsq,csnakemake.io\nWildcards\nq-)\x81q.X\x0f\x00\x00\x00sjl_mbn2_mod_R1q/a}q0(h\t}q1X\x06\x00\x00\x00sampleq2K\x00N\x86q3sX\x06\x00\x00\x00sampleq4h/ubX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_coresq9K\x01h\t}q:(X\x06\x00\x00\x00_nodesq;K\x01N\x86q<h9K\x00N\x86q=uh;K\x01ubub.')
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
