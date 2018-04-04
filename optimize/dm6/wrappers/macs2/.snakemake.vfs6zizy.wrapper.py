
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x06\x00\x00\x00outputq\x05csnakemake.io\nOutputFiles\nq\x06)\x81q\x07(XC\x00\x00\x00peak_out/macs2/lm38_kc_mod-rb_R1/lm38_kc_mod-rb_R1_peaks.narrowPeakq\x08X6\x00\x00\x00peak_out/macs2/lm38_kc_mod-rb_R1/lm38_kc_mod-rb_R1.bedq\te}q\n(X\n\x00\x00\x00narrowPeakq\x0bh\x08X\x03\x00\x00\x00bedq\x0ch\tX\x06\x00\x00\x00_namesq\r}q\x0e(h\x0bK\x00N\x86q\x0fh\x0cK\x01N\x86q\x10uubX\x04\x00\x00\x00ruleq\x11X\x05\x00\x00\x00macs2q\x12X\x07\x00\x00\x00threadsq\x13K\x01X\x06\x00\x00\x00paramsq\x14csnakemake.io\nParams\nq\x15)\x81q\x16X \x00\x00\x00peak_out/macs2/lm38_kc_mod-rb_R1q\x17a}q\x18(h\r}q\x19X\x06\x00\x00\x00prefixq\x1aK\x00N\x86q\x1bsh\x1ah\x17ubX\t\x00\x00\x00resourcesq\x1ccsnakemake.io\nResources\nq\x1d)\x81q\x1e(K\x01K\x01e}q\x1f(h\r}q (X\x06\x00\x00\x00_nodesq!K\x00N\x86q"X\x06\x00\x00\x00_coresq#K\x01N\x86q$uh#K\x01h!K\x01ubX\t\x00\x00\x00wildcardsq%csnakemake.io\nWildcards\nq&)\x81q\'X\x11\x00\x00\x00lm38_kc_mod-rb_R1q(a}q)(h\r}q*X\x06\x00\x00\x00sampleq+K\x00N\x86q,sX\x06\x00\x00\x00sampleq-h(ubX\x05\x00\x00\x00inputq.csnakemake.io\nInputFiles\nq/)\x81q0(X\x1b\x00\x00\x00dedup/lm38_kc_mod-rb_R1.bamq1X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq2e}q3(X\x03\x00\x00\x00inpq4h2X\x02\x00\x00\x00ipq5h1h\r}q6(h5K\x00N\x86q7h4K\x01N\x86q8uubX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\r}q=sbub.')
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
