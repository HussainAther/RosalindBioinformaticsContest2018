
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00configq\x04}q\x05X\x04\x00\x00\x00ruleq\x06X\x05\x00\x00\x00macs2q\x07X\x06\x00\x00\x00paramsq\x08csnakemake.io\nParams\nq\t)\x81q\nX"\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1q\x0ba}q\x0c(X\x06\x00\x00\x00prefixq\rh\x0bX\x06\x00\x00\x00_namesq\x0e}q\x0fh\rK\x00N\x86q\x10subX\x06\x00\x00\x00outputq\x11csnakemake.io\nOutputFiles\nq\x12)\x81q\x13(X:\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1/el40_kc_rump-5g4_R1.bedq\x14XG\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1/el40_kc_rump-5g4_R1_peaks.narrowPeakq\x15e}q\x16(h\x0e}q\x17(X\x03\x00\x00\x00bedq\x18K\x00N\x86q\x19X\n\x00\x00\x00narrowPeakq\x1aK\x01N\x86q\x1buh\x18h\x14h\x1ah\x15ubX\t\x00\x00\x00resourcesq\x1ccsnakemake.io\nResources\nq\x1d)\x81q\x1e(K\x01K\x01e}q\x1f(X\x06\x00\x00\x00_nodesq K\x01h\x0e}q!(h K\x00N\x86q"X\x06\x00\x00\x00_coresq#K\x01N\x86q$uh#K\x01ubX\x05\x00\x00\x00inputq%csnakemake.io\nInputFiles\nq&)\x81q\'(X\x1d\x00\x00\x00dedup/el40_kc_rump-5g4_R1.bamq(X\x1a\x00\x00\x00dedup/el38_kc_input_R1.bamq)e}q*(X\x02\x00\x00\x00ipq+h(h\x0e}q,(h+K\x00N\x86q-X\x03\x00\x00\x00inpq.K\x01N\x86q/uh.h)ubX\t\x00\x00\x00wildcardsq0csnakemake.io\nWildcards\nq1)\x81q2X\x13\x00\x00\x00el40_kc_rump-5g4_R1q3a}q4(X\x06\x00\x00\x00sampleq5h3h\x0e}q6X\x06\x00\x00\x00sampleq7K\x00N\x86q8subX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x0e}q=sbub.')
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
