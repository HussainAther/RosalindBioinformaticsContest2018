
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X8\x00\x00\x00peak_out/macs2/lm08_kc_shep-r6_R1/lm08_kc_shep-r6_R1.bedq\x06XE\x00\x00\x00peak_out/macs2/lm08_kc_shep-r6_R1/lm08_kc_shep-r6_R1_peaks.narrowPeakq\x07e}q\x08(X\x03\x00\x00\x00bedq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\n\x00\x00\x00narrowPeakq\rK\x01N\x86q\x0euh\rh\x07ubX\x04\x00\x00\x00ruleq\x0fX\x05\x00\x00\x00macs2q\x10X\t\x00\x00\x00resourcesq\x11csnakemake.io\nResources\nq\x12)\x81q\x13(K\x01K\x01e}q\x14(X\x06\x00\x00\x00_coresq\x15K\x01X\x06\x00\x00\x00_nodesq\x16K\x01h\n}q\x17(h\x15K\x00N\x86q\x18h\x16K\x01N\x86q\x19uubX\x06\x00\x00\x00configq\x1a}q\x1bX\x03\x00\x00\x00logq\x1ccsnakemake.io\nLog\nq\x1d)\x81q\x1e}q\x1fh\n}q sbX\t\x00\x00\x00wildcardsq!csnakemake.io\nWildcards\nq")\x81q#X\x12\x00\x00\x00lm08_kc_shep-r6_R1q$a}q%(X\x06\x00\x00\x00sampleq&h$h\n}q\'X\x06\x00\x00\x00sampleq(K\x00N\x86q)subX\x06\x00\x00\x00paramsq*csnakemake.io\nParams\nq+)\x81q,X!\x00\x00\x00peak_out/macs2/lm08_kc_shep-r6_R1q-a}q.(X\x06\x00\x00\x00prefixq/h-h\n}q0h/K\x00N\x86q1subX\x07\x00\x00\x00threadsq2K\x01X\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq6X\x1c\x00\x00\x00dedup/lm08_kc_shep-r6_R1.bamq7e}q8(X\x03\x00\x00\x00inpq9h6h\n}q:(h9K\x00N\x86q;X\x02\x00\x00\x00ipq<K\x01N\x86q=uh<h7ubub.')
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
