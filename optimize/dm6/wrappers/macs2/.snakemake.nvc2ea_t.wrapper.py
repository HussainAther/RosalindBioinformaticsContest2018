
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_coresq\x07K\x01X\x06\x00\x00\x00_nodesq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x08K\x00N\x86q\x0bh\x07K\x01N\x86q\x0cuubX\x05\x00\x00\x00inputq\rcsnakemake.io\nInputFiles\nq\x0e)\x81q\x0f(X\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq\x10X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq\x11e}q\x12(X\x02\x00\x00\x00ipq\x13h\x10h\t}q\x14(h\x13K\x00N\x86q\x15X\x03\x00\x00\x00inpq\x16K\x01N\x86q\x17uh\x16h\x11ubX\x06\x00\x00\x00configq\x18}q\x19X\x04\x00\x00\x00ruleq\x1aX\x05\x00\x00\x00macs2q\x1bX\x03\x00\x00\x00logq\x1ccsnakemake.io\nLog\nq\x1d)\x81q\x1e}q\x1fh\t}q sbX\t\x00\x00\x00wildcardsq!csnakemake.io\nWildcards\nq")\x81q#X\x0e\x00\x00\x00sjl_kc_shep_R1q$a}q%(X\x06\x00\x00\x00sampleq&h$h\t}q\'X\x06\x00\x00\x00sampleq(K\x00N\x86q)subX\x06\x00\x00\x00outputq*csnakemake.io\nOutputFiles\nq+)\x81q,(X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq-X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq.e}q/(X\x03\x00\x00\x00bedq0h-h\t}q1(h0K\x00N\x86q2X\n\x00\x00\x00narrowPeakq3K\x01N\x86q4uh3h.ubX\x07\x00\x00\x00threadsq5K\x01X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8(h$X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q9e}q:(X\x06\x00\x00\x00prefixq;h9h\t}q<(X\x0e\x00\x00\x00wrapper_sampleq=K\x00N\x86q>h;K\x01N\x86q?uh=h$ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.r > {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.pdf')
#shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
