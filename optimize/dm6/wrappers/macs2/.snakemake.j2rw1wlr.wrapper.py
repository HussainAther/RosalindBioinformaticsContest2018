
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05X#\x00\x00\x00peak_out/macs2/lm45_bg3_rm62-rat_R1q\x06a}q\x07(X\x06\x00\x00\x00prefixq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nh\x08K\x00N\x86q\x0bsubX\t\x00\x00\x00wildcardsq\x0ccsnakemake.io\nWildcards\nq\r)\x81q\x0eX\x14\x00\x00\x00lm45_bg3_rm62-rat_R1q\x0fa}q\x10(X\x06\x00\x00\x00sampleq\x11h\x0fh\t}q\x12X\x06\x00\x00\x00sampleq\x13K\x00N\x86q\x14subX\x07\x00\x00\x00threadsq\x15K\x01X\x06\x00\x00\x00outputq\x16csnakemake.io\nOutputFiles\nq\x17)\x81q\x18(X<\x00\x00\x00peak_out/macs2/lm45_bg3_rm62-rat_R1/lm45_bg3_rm62-rat_R1.bedq\x19XI\x00\x00\x00peak_out/macs2/lm45_bg3_rm62-rat_R1/lm45_bg3_rm62-rat_R1_peaks.narrowPeakq\x1ae}q\x1b(X\x03\x00\x00\x00bedq\x1ch\x19X\n\x00\x00\x00narrowPeakq\x1dh\x1ah\t}q\x1e(h\x1cK\x00N\x86q\x1fh\x1dK\x01N\x86q uubX\x03\x00\x00\x00logq!csnakemake.io\nLog\nq")\x81q#}q$h\t}q%sbX\x05\x00\x00\x00inputq&csnakemake.io\nInputFiles\nq\')\x81q((X\x1e\x00\x00\x00dedup/lm45_bg3_rm62-rat_R1.bamq)X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq*e}q+(X\x02\x00\x00\x00ipq,h)X\x03\x00\x00\x00inpq-h*h\t}q.(h,K\x00N\x86q/h-K\x01N\x86q0uubX\t\x00\x00\x00resourcesq1csnakemake.io\nResources\nq2)\x81q3(K\x01K\x01e}q4(X\x06\x00\x00\x00_nodesq5K\x01X\x06\x00\x00\x00_coresq6K\x01h\t}q7(h5K\x00N\x86q8h6K\x01N\x86q9uubX\x04\x00\x00\x00ruleq:X\x05\x00\x00\x00macs2q;X\x06\x00\x00\x00configq<}q=ub.')
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
