
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00configq\x04}q\x05X\t\x00\x00\x00resourcesq\x06csnakemake.io\nResources\nq\x07)\x81q\x08(K\x01K\x01e}q\t(X\x06\x00\x00\x00_namesq\n}q\x0b(X\x06\x00\x00\x00_coresq\x0cK\x00N\x86q\rX\x06\x00\x00\x00_nodesq\x0eK\x01N\x86q\x0fuh\x0eK\x01h\x0cK\x01ubX\x03\x00\x00\x00logq\x10csnakemake.io\nLog\nq\x11)\x81q\x12}q\x13h\n}q\x14sbX\x05\x00\x00\x00inputq\x15csnakemake.io\nInputFiles\nq\x16)\x81q\x17(X\x18\x00\x00\x00dedup/sjl_s2_shep_R1.bamq\x18X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x19e}q\x1a(X\x02\x00\x00\x00ipq\x1bh\x18X\x03\x00\x00\x00inpq\x1ch\x19h\n}q\x1d(h\x1bK\x00N\x86q\x1eh\x1cK\x01N\x86q\x1fuubX\x06\x00\x00\x00paramsq csnakemake.io\nParams\nq!)\x81q"X\x1d\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1q#a}q$(h\n}q%X\x06\x00\x00\x00prefixq&K\x00N\x86q\'sh&h#ubX\x04\x00\x00\x00ruleq(X\x05\x00\x00\x00macs2q)X\x06\x00\x00\x00outputq*csnakemake.io\nOutputFiles\nq+)\x81q,(X=\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1_peaks.narrowPeakq-X0\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1.bedq.e}q/(X\n\x00\x00\x00narrowPeakq0h-X\x03\x00\x00\x00bedq1h.h\n}q2(h0K\x00N\x86q3h1K\x01N\x86q4uubX\t\x00\x00\x00wildcardsq5csnakemake.io\nWildcards\nq6)\x81q7X\x0e\x00\x00\x00sjl_s2_shep_R1q8a}q9(h\n}q:X\x06\x00\x00\x00sampleq;K\x00N\x86q<sX\x06\x00\x00\x00sampleq=h8ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.input.ip}_model.r')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
