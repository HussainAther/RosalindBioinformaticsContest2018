
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq\x06X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq\x07e}q\x08(X\x02\x00\x00\x00ipq\th\x06X\x03\x00\x00\x00inpq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x03\x00\x00\x00logq\x0fcsnakemake.io\nLog\nq\x10)\x81q\x11}q\x12h\x0b}q\x13sbX\t\x00\x00\x00resourcesq\x14csnakemake.io\nResources\nq\x15)\x81q\x16(K\x01K\x01e}q\x17(X\x06\x00\x00\x00_nodesq\x18K\x01h\x0b}q\x19(h\x18K\x00N\x86q\x1aX\x06\x00\x00\x00_coresq\x1bK\x01N\x86q\x1cuh\x1bK\x01ubX\x06\x00\x00\x00configq\x1d}q\x1eX\t\x00\x00\x00wildcardsq\x1fcsnakemake.io\nWildcards\nq )\x81q!X\x0e\x00\x00\x00sjl_kc_shep_R1q"a}q#(X\x06\x00\x00\x00sampleq$h"h\x0b}q%X\x06\x00\x00\x00sampleq&K\x00N\x86q\'subX\x04\x00\x00\x00ruleq(X\x05\x00\x00\x00macs2q)X\x06\x00\x00\x00outputq*csnakemake.io\nOutputFiles\nq+)\x81q,(X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq-X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq.e}q/(X\x03\x00\x00\x00bedq0h-X\n\x00\x00\x00narrowPeakq1h.h\x0b}q2(h0K\x00N\x86q3h1K\x01N\x86q4uubX\x07\x00\x00\x00threadsq5K\x01X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8(h"X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q9e}q:(X\x0e\x00\x00\x00wrapper_sampleq;h"X\x06\x00\x00\x00prefixq<h9h\x0b}q=(h;K\x00N\x86q>h<K\x01N\x86q?uubub.')
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
