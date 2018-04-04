
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05(X\x12\x00\x00\x00lm43_bg3_mod-gp_R1q\x06X!\x00\x00\x00peak_out/macs2/lm43_bg3_mod-gp_R1q\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x0e\x00\x00\x00wrapper_sampleq\x0bK\x00N\x86q\x0cX\x06\x00\x00\x00prefixq\rK\x01N\x86q\x0euh\rh\x07h\x0bh\x06ubX\x05\x00\x00\x00inputq\x0fcsnakemake.io\nInputFiles\nq\x10)\x81q\x11(X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq\x12X\x1c\x00\x00\x00dedup/lm43_bg3_mod-gp_R1.bamq\x13e}q\x14(X\x02\x00\x00\x00ipq\x15h\x13X\x03\x00\x00\x00inpq\x16h\x12h\t}q\x17(h\x16K\x00N\x86q\x18h\x15K\x01N\x86q\x19uubX\x07\x00\x00\x00threadsq\x1aK\x01X\x06\x00\x00\x00configq\x1b}q\x1cX\x03\x00\x00\x00logq\x1dcsnakemake.io\nLog\nq\x1e)\x81q\x1f}q h\t}q!sbX\x04\x00\x00\x00ruleq"X\x05\x00\x00\x00macs2q#X\t\x00\x00\x00wildcardsq$csnakemake.io\nWildcards\nq%)\x81q&h\x06a}q\'(h\t}q(X\x06\x00\x00\x00sampleq)K\x00N\x86q*sX\x06\x00\x00\x00sampleq+h\x06ubX\t\x00\x00\x00resourcesq,csnakemake.io\nResources\nq-)\x81q.(K\x01K\x01e}q/(h\t}q0(X\x06\x00\x00\x00_coresq1K\x00N\x86q2X\x06\x00\x00\x00_nodesq3K\x01N\x86q4uh3K\x01h1K\x01ubX\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(XE\x00\x00\x00peak_out/macs2/lm43_bg3_mod-gp_R1/lm43_bg3_mod-gp_R1_peaks.narrowPeakq8X8\x00\x00\x00peak_out/macs2/lm43_bg3_mod-gp_R1/lm43_bg3_mod-gp_R1.bedq9e}q:(X\n\x00\x00\x00narrowPeakq;h8h\t}q<(h;K\x00N\x86q=X\x03\x00\x00\x00bedq>K\x01N\x86q?uh>h9ubub.')
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
