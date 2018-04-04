
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x04\x00\x00\x00ruleq\x05X\x05\x00\x00\x00macs2q\x06X\x07\x00\x00\x00threadsq\x07K\x01X\x06\x00\x00\x00paramsq\x08csnakemake.io\nParams\nq\t)\x81q\n(X\x0f\x00\x00\x00lm32_kc_suhw_R1q\x0bX\x1e\x00\x00\x00peak_out/macs2/lm32_kc_suhw_R1q\x0ce}q\r(X\x06\x00\x00\x00prefixq\x0eh\x0cX\x06\x00\x00\x00_namesq\x0f}q\x10(X\x0e\x00\x00\x00wrapper_sampleq\x11K\x00N\x86q\x12h\x0eK\x01N\x86q\x13uh\x11h\x0bubX\x05\x00\x00\x00inputq\x14csnakemake.io\nInputFiles\nq\x15)\x81q\x16(X\x19\x00\x00\x00dedup/lm32_kc_suhw_R1.bamq\x17X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq\x18e}q\x19(h\x0f}q\x1a(X\x02\x00\x00\x00ipq\x1bK\x00N\x86q\x1cX\x03\x00\x00\x00inpq\x1dK\x01N\x86q\x1euh\x1bh\x17h\x1dh\x18ubX\t\x00\x00\x00resourcesq\x1fcsnakemake.io\nResources\nq )\x81q!(K\x01K\x01e}q"(X\x06\x00\x00\x00_coresq#K\x01h\x0f}q$(X\x06\x00\x00\x00_nodesq%K\x00N\x86q&h#K\x01N\x86q\'uh%K\x01ubX\x06\x00\x00\x00outputq(csnakemake.io\nOutputFiles\nq))\x81q*(X?\x00\x00\x00peak_out/macs2/lm32_kc_suhw_R1/lm32_kc_suhw_R1_peaks.narrowPeakq+X2\x00\x00\x00peak_out/macs2/lm32_kc_suhw_R1/lm32_kc_suhw_R1.bedq,e}q-(X\n\x00\x00\x00narrowPeakq.h+h\x0f}q/(h.K\x00N\x86q0X\x03\x00\x00\x00bedq1K\x01N\x86q2uh1h,ubX\x03\x00\x00\x00logq3csnakemake.io\nLog\nq4)\x81q5}q6h\x0f}q7sbX\t\x00\x00\x00wildcardsq8csnakemake.io\nWildcards\nq9)\x81q:h\x0ba}q;(X\x06\x00\x00\x00sampleq<h\x0bh\x0f}q=X\x06\x00\x00\x00sampleq>K\x00N\x86q?subub.')
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
