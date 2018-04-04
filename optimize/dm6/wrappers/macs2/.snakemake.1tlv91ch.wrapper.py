
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x04\x00\x00\x00ruleq\x04X\x05\x00\x00\x00macs2q\x05X\t\x00\x00\x00resourcesq\x06csnakemake.io\nResources\nq\x07)\x81q\x08(K\x01K\x01e}q\t(X\x06\x00\x00\x00_namesq\n}q\x0b(X\x06\x00\x00\x00_coresq\x0cK\x00N\x86q\rX\x06\x00\x00\x00_nodesq\x0eK\x01N\x86q\x0fuh\x0cK\x01h\x0eK\x01ubX\x06\x00\x00\x00configq\x10}q\x11X\x05\x00\x00\x00inputq\x12csnakemake.io\nInputFiles\nq\x13)\x81q\x14(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x15X\x18\x00\x00\x00dedup/sjl_s2_shep_R1.bamq\x16e}q\x17(X\x03\x00\x00\x00inpq\x18h\x15h\n}q\x19(h\x18K\x00N\x86q\x1aX\x02\x00\x00\x00ipq\x1bK\x01N\x86q\x1cuh\x1bh\x16ubX\x06\x00\x00\x00paramsq\x1dcsnakemake.io\nParams\nq\x1e)\x81q\x1fX\x1d\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1q a}q!(h\n}q"X\x06\x00\x00\x00prefixq#K\x00N\x86q$sh#h ubX\t\x00\x00\x00wildcardsq%csnakemake.io\nWildcards\nq&)\x81q\'X\x0e\x00\x00\x00sjl_s2_shep_R1q(a}q)(h\n}q*X\x06\x00\x00\x00sampleq+K\x00N\x86q,sX\x06\x00\x00\x00sampleq-h(ubX\x06\x00\x00\x00outputq.csnakemake.io\nOutputFiles\nq/)\x81q0(X=\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1_peaks.narrowPeakq1X0\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1.bedq2e}q3(X\n\x00\x00\x00narrowPeakq4h1h\n}q5(h4K\x00N\x86q6X\x03\x00\x00\x00bedq7K\x01N\x86q8uh7h2ubX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\n}q=sbub.')
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
