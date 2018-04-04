
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x06X\x19\x00\x00\x00dedup/sjl_s2_cp190_R1.bamq\x07e}q\x08(X\x03\x00\x00\x00inpq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\x02\x00\x00\x00ipq\rK\x01N\x86q\x0euh\rh\x07ubX\x07\x00\x00\x00threadsq\x0fK\x01X\t\x00\x00\x00resourcesq\x10csnakemake.io\nResources\nq\x11)\x81q\x12(K\x01K\x01e}q\x13(X\x06\x00\x00\x00_nodesq\x14K\x01X\x06\x00\x00\x00_coresq\x15K\x01h\n}q\x16(h\x15K\x00N\x86q\x17h\x14K\x01N\x86q\x18uubX\x04\x00\x00\x00ruleq\x19X\x05\x00\x00\x00macs2q\x1aX\t\x00\x00\x00wildcardsq\x1bcsnakemake.io\nWildcards\nq\x1c)\x81q\x1dX\x0f\x00\x00\x00sjl_s2_cp190_R1q\x1ea}q\x1f(X\x06\x00\x00\x00sampleq h\x1eh\n}q!X\x06\x00\x00\x00sampleq"K\x00N\x86q#subX\x06\x00\x00\x00outputq$csnakemake.io\nOutputFiles\nq%)\x81q&(X?\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1_peaks.narrowPeakq\'X2\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1.bedq(e}q)(X\n\x00\x00\x00narrowPeakq*h\'X\x03\x00\x00\x00bedq+h(h\n}q,(h*K\x00N\x86q-h+K\x01N\x86q.uubX\x06\x00\x00\x00configq/}q0X\x03\x00\x00\x00logq1csnakemake.io\nLog\nq2)\x81q3}q4h\n}q5sbX\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8(X\x1e\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1q9h\x1ee}q:(X\x0e\x00\x00\x00wrapper_sampleq;h\x1eh\n}q<(X\x06\x00\x00\x00prefixq=K\x00N\x86q>h;K\x01N\x86q?uh=h9ubub.')
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
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
