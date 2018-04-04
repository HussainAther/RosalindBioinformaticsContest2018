
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x05\x00\x00\x00inputq\x04csnakemake.io\nInputFiles\nq\x05)\x81q\x06(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x07X\x1b\x00\x00\x00dedup/sjl_mbn2_cp190_R1.bamq\x08e}q\t(X\x06\x00\x00\x00_namesq\n}q\x0b(X\x03\x00\x00\x00inpq\x0cK\x00N\x86q\rX\x02\x00\x00\x00ipq\x0eK\x01N\x86q\x0fuh\x0ch\x07h\x0eh\x08ubX\x06\x00\x00\x00paramsq\x10csnakemake.io\nParams\nq\x11)\x81q\x12(X\x11\x00\x00\x00sjl_mbn2_cp190_R1q\x13X \x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1q\x14e}q\x15(h\n}q\x16(X\x0e\x00\x00\x00wrapper_sampleq\x17K\x00N\x86q\x18X\x06\x00\x00\x00prefixq\x19K\x01N\x86q\x1auh\x17h\x13h\x19h\x14ubX\t\x00\x00\x00resourcesq\x1bcsnakemake.io\nResources\nq\x1c)\x81q\x1d(K\x01K\x01e}q\x1e(h\n}q\x1f(X\x06\x00\x00\x00_nodesq K\x00N\x86q!X\x06\x00\x00\x00_coresq"K\x01N\x86q#uh"K\x01h K\x01ubX\x06\x00\x00\x00outputq$csnakemake.io\nOutputFiles\nq%)\x81q&(X6\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1.bedq\'XC\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1_peaks.narrowPeakq(e}q)(h\n}q*(X\x03\x00\x00\x00bedq+K\x00N\x86q,X\n\x00\x00\x00narrowPeakq-K\x01N\x86q.uh+h\'h-h(ubX\x03\x00\x00\x00logq/csnakemake.io\nLog\nq0)\x81q1}q2h\n}q3sbX\x04\x00\x00\x00ruleq4X\x05\x00\x00\x00macs2q5X\t\x00\x00\x00wildcardsq6csnakemake.io\nWildcards\nq7)\x81q8h\x13a}q9(h\n}q:X\x06\x00\x00\x00sampleq;K\x00N\x86q<sX\x06\x00\x00\x00sampleq=h\x13ubX\x06\x00\x00\x00configq>}q?ub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.r')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
