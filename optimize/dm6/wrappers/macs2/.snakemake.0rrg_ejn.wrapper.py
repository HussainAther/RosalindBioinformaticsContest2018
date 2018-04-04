
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x17\x00\x00\x00dedup/sjl_kc_mod_R1.bamq\x06X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq\x07e}q\x08(X\x02\x00\x00\x00ipq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\rh\x07ubX\t\x00\x00\x00resourcesq\x0fcsnakemake.io\nResources\nq\x10)\x81q\x11(K\x01K\x01e}q\x12(h\n}q\x13(X\x06\x00\x00\x00_nodesq\x14K\x00N\x86q\x15X\x06\x00\x00\x00_coresq\x16K\x01N\x86q\x17uh\x14K\x01h\x16K\x01ubX\x06\x00\x00\x00configq\x18}q\x19X\x03\x00\x00\x00logq\x1acsnakemake.io\nLog\nq\x1b)\x81q\x1c}q\x1dh\n}q\x1esbX\x06\x00\x00\x00paramsq\x1fcsnakemake.io\nParams\nq )\x81q!X\x1c\x00\x00\x00peak_out/macs2/sjl_kc_mod_R1q"a}q#(h\n}q$X\x06\x00\x00\x00prefixq%K\x00N\x86q&sh%h"ubX\x07\x00\x00\x00threadsq\'K\x01X\x04\x00\x00\x00ruleq(X\x05\x00\x00\x00macs2q)X\t\x00\x00\x00wildcardsq*csnakemake.io\nWildcards\nq+)\x81q,X\r\x00\x00\x00sjl_kc_mod_R1q-a}q.(h\n}q/X\x06\x00\x00\x00sampleq0K\x00N\x86q1sX\x06\x00\x00\x00sampleq2h-ubX\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X.\x00\x00\x00peak_out/macs2/sjl_kc_mod_R1/sjl_kc_mod_R1.bedq6X;\x00\x00\x00peak_out/macs2/sjl_kc_mod_R1/sjl_kc_mod_R1_peaks.narrowPeakq7e}q8(X\x03\x00\x00\x00bedq9h6h\n}q:(h9K\x00N\x86q;X\n\x00\x00\x00narrowPeakq<K\x01N\x86q=uh<h7ubub.')
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
