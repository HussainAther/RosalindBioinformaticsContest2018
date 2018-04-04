
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_coresq\x07K\x01X\x06\x00\x00\x00_namesq\x08}q\t(h\x07K\x00N\x86q\nX\x06\x00\x00\x00_nodesq\x0bK\x01N\x86q\x0cuh\x0bK\x01ubX\x03\x00\x00\x00logq\rcsnakemake.io\nLog\nq\x0e)\x81q\x0f}q\x10h\x08}q\x11sbX\x06\x00\x00\x00outputq\x12csnakemake.io\nOutputFiles\nq\x13)\x81q\x14(X0\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1.bedq\x15X=\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1_peaks.narrowPeakq\x16e}q\x17(X\x03\x00\x00\x00bedq\x18h\x15X\n\x00\x00\x00narrowPeakq\x19h\x16h\x08}q\x1a(h\x18K\x00N\x86q\x1bh\x19K\x01N\x86q\x1cuubX\x06\x00\x00\x00paramsq\x1dcsnakemake.io\nParams\nq\x1e)\x81q\x1f(X\x0e\x00\x00\x00sjl_s2_shep_R1q X\x1d\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1q!e}q"(X\x06\x00\x00\x00prefixq#h!h\x08}q$(X\x0e\x00\x00\x00wrapper_sampleq%K\x00N\x86q&h#K\x01N\x86q\'uh%h ubX\x04\x00\x00\x00ruleq(X\x05\x00\x00\x00macs2q)X\x05\x00\x00\x00inputq*csnakemake.io\nInputFiles\nq+)\x81q,(X\x18\x00\x00\x00dedup/sjl_s2_shep_R1.bamq-X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq.e}q/(X\x02\x00\x00\x00ipq0h-X\x03\x00\x00\x00inpq1h.h\x08}q2(h0K\x00N\x86q3h1K\x01N\x86q4uubX\x07\x00\x00\x00threadsq5K\x01X\x06\x00\x00\x00configq6}q7X\t\x00\x00\x00wildcardsq8csnakemake.io\nWildcards\nq9)\x81q:h a}q;(X\x06\x00\x00\x00sampleq<h h\x08}q=X\x06\x00\x00\x00sampleq>K\x00N\x86q?subub.')
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
