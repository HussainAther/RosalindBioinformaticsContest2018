
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_coresq\x07K\x01X\x06\x00\x00\x00_nodesq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x08K\x01N\x86q\x0bh\x07K\x00N\x86q\x0cuubX\x06\x00\x00\x00outputq\rcsnakemake.io\nOutputFiles\nq\x0e)\x81q\x0f(X2\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1.bedq\x10X?\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1/sjl_cl8_shep_R1_peaks.narrowPeakq\x11e}q\x12(X\x03\x00\x00\x00bedq\x13h\x10X\n\x00\x00\x00narrowPeakq\x14h\x11h\t}q\x15(h\x13K\x00N\x86q\x16h\x14K\x01N\x86q\x17uubX\x07\x00\x00\x00threadsq\x18K\x01X\x06\x00\x00\x00configq\x19}q\x1aX\x05\x00\x00\x00inputq\x1bcsnakemake.io\nInputFiles\nq\x1c)\x81q\x1d(X\x19\x00\x00\x00dedup/sjl_cl8_shep_R1.bamq\x1eX\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x1fe}q (X\x03\x00\x00\x00inpq!h\x1fX\x02\x00\x00\x00ipq"h\x1eh\t}q#(h"K\x00N\x86q$h!K\x01N\x86q%uubX\x04\x00\x00\x00ruleq&X\x05\x00\x00\x00macs2q\'X\x06\x00\x00\x00paramsq(csnakemake.io\nParams\nq))\x81q*(X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_shep_R1q+X\x0f\x00\x00\x00sjl_cl8_shep_R1q,e}q-(X\x06\x00\x00\x00prefixq.h+X\x0e\x00\x00\x00wrapper_sampleq/h,h\t}q0(h.K\x00N\x86q1h/K\x01N\x86q2uubX\x03\x00\x00\x00logq3csnakemake.io\nLog\nq4)\x81q5}q6h\t}q7sbX\t\x00\x00\x00wildcardsq8csnakemake.io\nWildcards\nq9)\x81q:h,a}q;(X\x06\x00\x00\x00sampleq<h,h\t}q=X\x06\x00\x00\x00sampleq>K\x00N\x86q?subub.')
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
