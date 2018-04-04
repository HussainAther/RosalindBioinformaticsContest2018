
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x0e\x00\x00\x00sjl_kc_shep_R1q\x06a}q\x07(X\x06\x00\x00\x00sampleq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nX\x06\x00\x00\x00sampleq\x0bK\x00N\x86q\x0csubX\x07\x00\x00\x00threadsq\rK\x01X\x06\x00\x00\x00configq\x0e}q\x0fX\t\x00\x00\x00resourcesq\x10csnakemake.io\nResources\nq\x11)\x81q\x12(K\x01K\x01e}q\x13(X\x06\x00\x00\x00_nodesq\x14K\x01h\t}q\x15(h\x14K\x00N\x86q\x16X\x06\x00\x00\x00_coresq\x17K\x01N\x86q\x18uh\x17K\x01ubX\x05\x00\x00\x00inputq\x19csnakemake.io\nInputFiles\nq\x1a)\x81q\x1b(X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq\x1cX\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq\x1de}q\x1e(X\x03\x00\x00\x00inpq\x1fh\x1cX\x02\x00\x00\x00ipq h\x1dh\t}q!(h\x1fK\x00N\x86q"h K\x01N\x86q#uubX\x06\x00\x00\x00outputq$csnakemake.io\nOutputFiles\nq%)\x81q&(X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq\'X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq(e}q)(X\x03\x00\x00\x00bedq*h\'h\t}q+(h*K\x00N\x86q,X\n\x00\x00\x00narrowPeakq-K\x01N\x86q.uh-h(ubX\x06\x00\x00\x00paramsq/csnakemake.io\nParams\nq0)\x81q1X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q2a}q3(h\t}q4X\x06\x00\x00\x00prefixq5K\x00N\x86q6sh5h2ubX\x03\x00\x00\x00logq7csnakemake.io\nLog\nq8)\x81q9}q:h\t}q;sbX\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=ub.')
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
