
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X?\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1_peaks.narrowPeakq\x06X2\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1.bedq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\n\x00\x00\x00narrowPeakq\x0bK\x00N\x86q\x0cX\x03\x00\x00\x00bedq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1q\x12a}q\x13(X\x06\x00\x00\x00prefixq\x14h\x12h\t}q\x15h\x14K\x00N\x86q\x16subX\t\x00\x00\x00wildcardsq\x17csnakemake.io\nWildcards\nq\x18)\x81q\x19X\x0f\x00\x00\x00sjl_cl8_shep_R1q\x1aa}q\x1b(X\x06\x00\x00\x00sampleq\x1ch\x1ah\t}q\x1dX\x06\x00\x00\x00sampleq\x1eK\x00N\x86q\x1fsubX\x07\x00\x00\x00threadsq K\x01X\x06\x00\x00\x00configq!}q"X\x04\x00\x00\x00ruleq#X\x05\x00\x00\x00macs2q$X\t\x00\x00\x00resourcesq%csnakemake.io\nResources\nq&)\x81q\'(K\x01K\x01e}q((X\x06\x00\x00\x00_coresq)K\x01X\x06\x00\x00\x00_nodesq*K\x01h\t}q+(h*K\x00N\x86q,h)K\x01N\x86q-uubX\x03\x00\x00\x00logq.csnakemake.io\nLog\nq/)\x81q0}q1h\t}q2sbX\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x19\x00\x00\x00dedup/sjl_cl8_shep_R1.bamq6X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq7e}q8(X\x02\x00\x00\x00ipq9h6h\t}q:(h9K\x00N\x86q;X\x03\x00\x00\x00inpq<K\x01N\x86q=uh<h7ubub.')
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
