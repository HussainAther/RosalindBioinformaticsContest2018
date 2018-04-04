
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x07\x00\x00\x00threadsq\x05K\x01X\x06\x00\x00\x00outputq\x06csnakemake.io\nOutputFiles\nq\x07)\x81q\x08(X6\x00\x00\x00peak_out/macs2/lm38_kc_mod-rb_R1/lm38_kc_mod-rb_R1.bedq\tXC\x00\x00\x00peak_out/macs2/lm38_kc_mod-rb_R1/lm38_kc_mod-rb_R1_peaks.narrowPeakq\ne}q\x0b(X\n\x00\x00\x00narrowPeakq\x0ch\nX\x03\x00\x00\x00bedq\rh\tX\x06\x00\x00\x00_namesq\x0e}q\x0f(h\x0cK\x01N\x86q\x10h\rK\x00N\x86q\x11uubX\t\x00\x00\x00resourcesq\x12csnakemake.io\nResources\nq\x13)\x81q\x14(K\x01K\x01e}q\x15(X\x06\x00\x00\x00_nodesq\x16K\x01X\x06\x00\x00\x00_coresq\x17K\x01h\x0e}q\x18(h\x16K\x00N\x86q\x19h\x17K\x01N\x86q\x1auubX\t\x00\x00\x00wildcardsq\x1bcsnakemake.io\nWildcards\nq\x1c)\x81q\x1dX\x11\x00\x00\x00lm38_kc_mod-rb_R1q\x1ea}q\x1f(X\x06\x00\x00\x00sampleq h\x1eh\x0e}q!X\x06\x00\x00\x00sampleq"K\x00N\x86q#subX\x06\x00\x00\x00paramsq$csnakemake.io\nParams\nq%)\x81q&X \x00\x00\x00peak_out/macs2/lm38_kc_mod-rb_R1q\'a}q((X\x06\x00\x00\x00prefixq)h\'h\x0e}q*h)K\x00N\x86q+subX\x04\x00\x00\x00ruleq,X\x05\x00\x00\x00macs2q-X\x05\x00\x00\x00inputq.csnakemake.io\nInputFiles\nq/)\x81q0(X\x1b\x00\x00\x00dedup/lm38_kc_mod-rb_R1.bamq1X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq2e}q3(X\x03\x00\x00\x00inpq4h2X\x02\x00\x00\x00ipq5h1h\x0e}q6(h5K\x00N\x86q7h4K\x01N\x86q8uubX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x0e}q=sbub.')
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
