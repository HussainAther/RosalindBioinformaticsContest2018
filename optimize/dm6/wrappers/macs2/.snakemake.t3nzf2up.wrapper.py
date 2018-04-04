
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq\x06X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq\x07e}q\x08(X\n\x00\x00\x00narrowPeakq\th\x06X\x03\x00\x00\x00bedq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x04\x00\x00\x00ruleq\x0fX\x05\x00\x00\x00macs2q\x10X\x06\x00\x00\x00configq\x11}q\x12X\t\x00\x00\x00wildcardsq\x13csnakemake.io\nWildcards\nq\x14)\x81q\x15X\x0e\x00\x00\x00sjl_kc_shep_R1q\x16a}q\x17(X\x06\x00\x00\x00sampleq\x18h\x16h\x0b}q\x19X\x06\x00\x00\x00sampleq\x1aK\x00N\x86q\x1bsubX\x05\x00\x00\x00inputq\x1ccsnakemake.io\nInputFiles\nq\x1d)\x81q\x1e(X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq\x1fX\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq e}q!(X\x03\x00\x00\x00inpq"h\x1fX\x02\x00\x00\x00ipq#h h\x0b}q$(h"K\x00N\x86q%h#K\x01N\x86q&uubX\x06\x00\x00\x00paramsq\'csnakemake.io\nParams\nq()\x81q)(X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q*h\x16e}q+(X\x0e\x00\x00\x00wrapper_sampleq,h\x16X\x06\x00\x00\x00prefixq-h*h\x0b}q.(h-K\x00N\x86q/h,K\x01N\x86q0uubX\x03\x00\x00\x00logq1csnakemake.io\nLog\nq2)\x81q3}q4h\x0b}q5sbX\x07\x00\x00\x00threadsq6K\x01X\t\x00\x00\x00resourcesq7csnakemake.io\nResources\nq8)\x81q9(K\x01K\x01e}q:(X\x06\x00\x00\x00_coresq;K\x01X\x06\x00\x00\x00_nodesq<K\x01h\x0b}q=(h<K\x00N\x86q>h;K\x01N\x86q?uubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.params.sample}_model.r')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
