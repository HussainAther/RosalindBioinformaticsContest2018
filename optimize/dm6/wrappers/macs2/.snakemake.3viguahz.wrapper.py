
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\t\x00\x00\x00resourcesq\tcsnakemake.io\nResources\nq\n)\x81q\x0b(K\x01K\x01e}q\x0c(X\x06\x00\x00\x00_coresq\rK\x01X\x06\x00\x00\x00_nodesq\x0eK\x01h\x07}q\x0f(h\rK\x00N\x86q\x10h\x0eK\x01N\x86q\x11uubX\x06\x00\x00\x00configq\x12}q\x13X\x06\x00\x00\x00outputq\x14csnakemake.io\nOutputFiles\nq\x15)\x81q\x16(X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq\x17X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq\x18e}q\x19(X\n\x00\x00\x00narrowPeakq\x1ah\x17X\x03\x00\x00\x00bedq\x1bh\x18h\x07}q\x1c(h\x1aK\x00N\x86q\x1dh\x1bK\x01N\x86q\x1euubX\t\x00\x00\x00wildcardsq\x1fcsnakemake.io\nWildcards\nq )\x81q!X\x0e\x00\x00\x00sjl_kc_shep_R1q"a}q#(X\x06\x00\x00\x00sampleq$h"h\x07}q%X\x06\x00\x00\x00sampleq&K\x00N\x86q\'subX\x05\x00\x00\x00inputq(csnakemake.io\nInputFiles\nq))\x81q*(X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq+X\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq,e}q-(X\x03\x00\x00\x00inpq.h+X\x02\x00\x00\x00ipq/h,h\x07}q0(h.K\x00N\x86q1h/K\x01N\x86q2uubX\x04\x00\x00\x00ruleq3X\x05\x00\x00\x00macs2q4X\x07\x00\x00\x00threadsq5K\x01X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q9a}q:(X\x06\x00\x00\x00prefixq;h9h\x07}q<h;K\x00N\x86q=subub.')
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
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
