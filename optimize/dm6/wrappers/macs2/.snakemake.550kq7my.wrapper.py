
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x19\x00\x00\x00dedup/sjl_cl8_shep_R1.bamq\x06X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x02\x00\x00\x00ipq\x0bK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x03\x00\x00\x00logq\x0fcsnakemake.io\nLog\nq\x10)\x81q\x11}q\x12h\t}q\x13sbX\x06\x00\x00\x00configq\x14}q\x15X\t\x00\x00\x00wildcardsq\x16csnakemake.io\nWildcards\nq\x17)\x81q\x18X\x0f\x00\x00\x00sjl_cl8_shep_R1q\x19a}q\x1a(h\t}q\x1bX\x06\x00\x00\x00sampleq\x1cK\x00N\x86q\x1dsX\x06\x00\x00\x00sampleq\x1eh\x19ubX\x04\x00\x00\x00ruleq\x1fX\x05\x00\x00\x00macs2q X\x06\x00\x00\x00outputq!csnakemake.io\nOutputFiles\nq")\x81q#(X2\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1.bedq$X?\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1_peaks.narrowPeakq%e}q&(h\t}q\'(X\x03\x00\x00\x00bedq(K\x00N\x86q)X\n\x00\x00\x00narrowPeakq*K\x01N\x86q+uh(h$h*h%ubX\x06\x00\x00\x00paramsq,csnakemake.io\nParams\nq-)\x81q.X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1q/a}q0(h\t}q1X\x06\x00\x00\x00prefixq2K\x00N\x86q3sh2h/ubX\x07\x00\x00\x00threadsq4K\x01X\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(h\t}q9(X\x06\x00\x00\x00_nodesq:K\x00N\x86q;X\x06\x00\x00\x00_coresq<K\x01N\x86q=uh:K\x01h<K\x01ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.wildcards.sample}_model.r')
#shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
shell("cd {snakemake.params.prefix} && ln -sf $(basename {snakemake.output.narrowPeak}) $(basename {snakemake.output.bed})")
