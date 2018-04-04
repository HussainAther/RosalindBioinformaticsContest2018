
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00paramsq\x04csnakemake.io\nParams\nq\x05)\x81q\x06X\x1d\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1q\x07a}q\x08(X\x06\x00\x00\x00prefixq\th\x07X\x06\x00\x00\x00_namesq\n}q\x0bh\tK\x00N\x86q\x0csubX\t\x00\x00\x00resourcesq\rcsnakemake.io\nResources\nq\x0e)\x81q\x0f(K\x01K\x01e}q\x10(X\x06\x00\x00\x00_nodesq\x11K\x01h\n}q\x12(X\x06\x00\x00\x00_coresq\x13K\x00N\x86q\x14h\x11K\x01N\x86q\x15uh\x13K\x01ubX\t\x00\x00\x00wildcardsq\x16csnakemake.io\nWildcards\nq\x17)\x81q\x18X\x0e\x00\x00\x00sjl_s3_shep_R1q\x19a}q\x1a(h\n}q\x1bX\x06\x00\x00\x00sampleq\x1cK\x00N\x86q\x1dsX\x06\x00\x00\x00sampleq\x1eh\x19ubX\x06\x00\x00\x00outputq\x1fcsnakemake.io\nOutputFiles\nq )\x81q!(X0\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1/sjl_s3_shep_R1.bedq"X=\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1/sjl_s3_shep_R1_peaks.narrowPeakq#e}q$(X\x03\x00\x00\x00bedq%h"h\n}q&(h%K\x00N\x86q\'X\n\x00\x00\x00narrowPeakq(K\x01N\x86q)uh(h#ubX\x05\x00\x00\x00inputq*csnakemake.io\nInputFiles\nq+)\x81q,(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq-X\x18\x00\x00\x00dedup/sjl_s3_shep_R1.bamq.e}q/(h\n}q0(X\x03\x00\x00\x00inpq1K\x00N\x86q2X\x02\x00\x00\x00ipq3K\x01N\x86q4uh1h-h3h.ubX\x04\x00\x00\x00ruleq5X\x05\x00\x00\x00macs2q6X\x03\x00\x00\x00logq7csnakemake.io\nLog\nq8)\x81q9}q:h\n}q;sbX\x06\x00\x00\x00configq<}q=ub.')
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
