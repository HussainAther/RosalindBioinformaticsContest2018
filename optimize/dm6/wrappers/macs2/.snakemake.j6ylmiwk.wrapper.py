
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x1c\x00\x00\x00dedup/lm06_kc_shep-gp_R1.bamq\x06X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq\x07e}q\x08(X\x02\x00\x00\x00ipq\th\x06X\x03\x00\x00\x00inpq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x07\x00\x00\x00threadsq\x0fK\x01X\x06\x00\x00\x00paramsq\x10csnakemake.io\nParams\nq\x11)\x81q\x12X!\x00\x00\x00peak_out/macs2/lm06_kc_shep-gp_R1q\x13a}q\x14(h\x0b}q\x15X\x06\x00\x00\x00prefixq\x16K\x00N\x86q\x17sh\x16h\x13ubX\x04\x00\x00\x00ruleq\x18X\x05\x00\x00\x00macs2q\x19X\t\x00\x00\x00wildcardsq\x1acsnakemake.io\nWildcards\nq\x1b)\x81q\x1cX\x12\x00\x00\x00lm06_kc_shep-gp_R1q\x1da}q\x1e(h\x0b}q\x1fX\x06\x00\x00\x00sampleq K\x00N\x86q!sX\x06\x00\x00\x00sampleq"h\x1dubX\x06\x00\x00\x00outputq#csnakemake.io\nOutputFiles\nq$)\x81q%(XE\x00\x00\x00peak_out/macs2/lm06_kc_shep-gp_R1/lm06_kc_shep-gp_R1_peaks.narrowPeakq&X8\x00\x00\x00peak_out/macs2/lm06_kc_shep-gp_R1/lm06_kc_shep-gp_R1.bedq\'e}q((X\n\x00\x00\x00narrowPeakq)h&h\x0b}q*(h)K\x00N\x86q+X\x03\x00\x00\x00bedq,K\x01N\x86q-uh,h\'ubX\x03\x00\x00\x00logq.csnakemake.io\nLog\nq/)\x81q0}q1h\x0b}q2sbX\x06\x00\x00\x00configq3}q4X\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(h\x0b}q9(X\x06\x00\x00\x00_nodesq:K\x00N\x86q;X\x06\x00\x00\x00_coresq<K\x01N\x86q=uh<K\x01h:K\x01ubub.')
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
