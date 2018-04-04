
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x1b\x00\x00\x00dedup/lm37_kc_mod-gp_R1.bamq\x06X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq\x07e}q\x08(X\x02\x00\x00\x00ipq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\rh\x07ubX\x07\x00\x00\x00threadsq\x0fK\x01X\x04\x00\x00\x00ruleq\x10X\x05\x00\x00\x00macs2q\x11X\x06\x00\x00\x00outputq\x12csnakemake.io\nOutputFiles\nq\x13)\x81q\x14(X6\x00\x00\x00peak_out/macs2/lm37_kc_mod-gp_R1/lm37_kc_mod-gp_R1.bedq\x15XC\x00\x00\x00peak_out/macs2/lm37_kc_mod-gp_R1/lm37_kc_mod-gp_R1_peaks.narrowPeakq\x16e}q\x17(X\n\x00\x00\x00narrowPeakq\x18h\x16X\x03\x00\x00\x00bedq\x19h\x15h\n}q\x1a(h\x18K\x01N\x86q\x1bh\x19K\x00N\x86q\x1cuubX\x03\x00\x00\x00logq\x1dcsnakemake.io\nLog\nq\x1e)\x81q\x1f}q h\n}q!sbX\x06\x00\x00\x00configq"}q#X\x06\x00\x00\x00paramsq$csnakemake.io\nParams\nq%)\x81q&X \x00\x00\x00peak_out/macs2/lm37_kc_mod-gp_R1q\'a}q((X\x06\x00\x00\x00prefixq)h\'h\n}q*h)K\x00N\x86q+subX\t\x00\x00\x00wildcardsq,csnakemake.io\nWildcards\nq-)\x81q.X\x11\x00\x00\x00lm37_kc_mod-gp_R1q/a}q0(X\x06\x00\x00\x00sampleq1h/h\n}q2X\x06\x00\x00\x00sampleq3K\x00N\x86q4subX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_nodesq9K\x01h\n}q:(h9K\x00N\x86q;X\x06\x00\x00\x00_coresq<K\x01N\x86q=uh<K\x01ubub.')
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
