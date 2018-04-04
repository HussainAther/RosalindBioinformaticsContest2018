
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X<\x00\x00\x00peak_out/macs2/lm42_kc_rump-10c3_R1/lm42_kc_rump-10c3_R1.bedq\x06XI\x00\x00\x00peak_out/macs2/lm42_kc_rump-10c3_R1/lm42_kc_rump-10c3_R1_peaks.narrowPeakq\x07e}q\x08(X\x03\x00\x00\x00bedq\th\x06X\n\x00\x00\x00narrowPeakq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x07\x00\x00\x00threadsq\x0fK\x01X\x03\x00\x00\x00logq\x10csnakemake.io\nLog\nq\x11)\x81q\x12}q\x13h\x0b}q\x14sbX\x06\x00\x00\x00configq\x15}q\x16X\x06\x00\x00\x00paramsq\x17csnakemake.io\nParams\nq\x18)\x81q\x19X#\x00\x00\x00peak_out/macs2/lm42_kc_rump-10c3_R1q\x1aa}q\x1b(X\x06\x00\x00\x00prefixq\x1ch\x1ah\x0b}q\x1dh\x1cK\x00N\x86q\x1esubX\t\x00\x00\x00wildcardsq\x1fcsnakemake.io\nWildcards\nq )\x81q!X\x14\x00\x00\x00lm42_kc_rump-10c3_R1q"a}q#(X\x06\x00\x00\x00sampleq$h"h\x0b}q%X\x06\x00\x00\x00sampleq&K\x00N\x86q\'subX\x05\x00\x00\x00inputq(csnakemake.io\nInputFiles\nq))\x81q*(X\x1e\x00\x00\x00dedup/lm42_kc_rump-10c3_R1.bamq+X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq,e}q-(X\x02\x00\x00\x00ipq.h+X\x03\x00\x00\x00inpq/h,h\x0b}q0(h.K\x00N\x86q1h/K\x01N\x86q2uubX\t\x00\x00\x00resourcesq3csnakemake.io\nResources\nq4)\x81q5(K\x01K\x01e}q6(X\x06\x00\x00\x00_coresq7K\x01X\x06\x00\x00\x00_nodesq8K\x01h\x0b}q9(h7K\x00N\x86q:h8K\x01N\x86q;uubX\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=ub.')
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
