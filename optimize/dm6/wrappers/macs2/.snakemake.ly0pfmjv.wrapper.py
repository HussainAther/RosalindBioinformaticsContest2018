
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05X!\x00\x00\x00peak_out/macs2/lm43_bg3_mod-gp_R1q\x06a}q\x07(X\x06\x00\x00\x00prefixq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nh\x08K\x00N\x86q\x0bsubX\t\x00\x00\x00wildcardsq\x0ccsnakemake.io\nWildcards\nq\r)\x81q\x0eX\x12\x00\x00\x00lm43_bg3_mod-gp_R1q\x0fa}q\x10(X\x06\x00\x00\x00sampleq\x11h\x0fh\t}q\x12X\x06\x00\x00\x00sampleq\x13K\x00N\x86q\x14subX\x04\x00\x00\x00ruleq\x15X\x05\x00\x00\x00macs2q\x16X\t\x00\x00\x00resourcesq\x17csnakemake.io\nResources\nq\x18)\x81q\x19(K\x01K\x01e}q\x1a(X\x06\x00\x00\x00_nodesq\x1bK\x01X\x06\x00\x00\x00_coresq\x1cK\x01h\t}q\x1d(h\x1bK\x00N\x86q\x1eh\x1cK\x01N\x86q\x1fuubX\x07\x00\x00\x00threadsq K\x01X\x03\x00\x00\x00logq!csnakemake.io\nLog\nq")\x81q#}q$h\t}q%sbX\x06\x00\x00\x00outputq&csnakemake.io\nOutputFiles\nq\')\x81q((XE\x00\x00\x00peak_out/macs2/lm43_bg3_mod-gp_R1/lm43_bg3_mod-gp_R1_peaks.narrowPeakq)X8\x00\x00\x00peak_out/macs2/lm43_bg3_mod-gp_R1/lm43_bg3_mod-gp_R1.bedq*e}q+(X\n\x00\x00\x00narrowPeakq,h)X\x03\x00\x00\x00bedq-h*h\t}q.(h,K\x00N\x86q/h-K\x01N\x86q0uubX\x05\x00\x00\x00inputq1csnakemake.io\nInputFiles\nq2)\x81q3(X\x1c\x00\x00\x00dedup/lm43_bg3_mod-gp_R1.bamq4X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq5e}q6(X\x02\x00\x00\x00ipq7h4X\x03\x00\x00\x00inpq8h5h\t}q9(h7K\x00N\x86q:h8K\x01N\x86q;uubX\x06\x00\x00\x00configq<}q=ub.')
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
