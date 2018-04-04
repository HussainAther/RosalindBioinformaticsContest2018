
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x19\x00\x00\x00dedup/sjl_mbn2_mod_R1.bamq\x06X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x07e}q\x08(X\x02\x00\x00\x00ipq\th\x06X\x03\x00\x00\x00inpq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x06\x00\x00\x00configq\x0f}q\x10X\x04\x00\x00\x00ruleq\x11X\x05\x00\x00\x00macs2q\x12X\t\x00\x00\x00wildcardsq\x13csnakemake.io\nWildcards\nq\x14)\x81q\x15X\x0f\x00\x00\x00sjl_mbn2_mod_R1q\x16a}q\x17(X\x06\x00\x00\x00sampleq\x18h\x16h\x0b}q\x19X\x06\x00\x00\x00sampleq\x1aK\x00N\x86q\x1bsubX\x06\x00\x00\x00outputq\x1ccsnakemake.io\nOutputFiles\nq\x1d)\x81q\x1e(X2\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1.bedq\x1fX?\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1_peaks.narrowPeakq e}q!(X\n\x00\x00\x00narrowPeakq"h X\x03\x00\x00\x00bedq#h\x1fh\x0b}q$(h"K\x01N\x86q%h#K\x00N\x86q&uubX\x07\x00\x00\x00threadsq\'K\x01X\x06\x00\x00\x00paramsq(csnakemake.io\nParams\nq))\x81q*X\x1e\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1q+a}q,(X\x06\x00\x00\x00prefixq-h+h\x0b}q.h-K\x00N\x86q/subX\t\x00\x00\x00resourcesq0csnakemake.io\nResources\nq1)\x81q2(K\x01K\x01e}q3(X\x06\x00\x00\x00_nodesq4K\x01X\x06\x00\x00\x00_coresq5K\x01h\x0b}q6(h4K\x01N\x86q7h5K\x00N\x86q8uubX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x0b}q=sbub.')
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
shell('touch {snakemake.output.bed}')
shell('Rscript peak_out/macs2/{snakemake.params.prefix}_model.r')
