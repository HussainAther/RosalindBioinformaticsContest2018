
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00outputq\tcsnakemake.io\nOutputFiles\nq\n)\x81q\x0b(X0\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1.bedq\x0cX=\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1_peaks.narrowPeakq\re}q\x0e(X\x03\x00\x00\x00bedq\x0fh\x0ch\x07}q\x10(X\n\x00\x00\x00narrowPeakq\x11K\x01N\x86q\x12h\x0fK\x00N\x86q\x13uh\x11h\rubX\x06\x00\x00\x00configq\x14}q\x15X\x06\x00\x00\x00paramsq\x16csnakemake.io\nParams\nq\x17)\x81q\x18(X\x1d\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1q\x19X\x0e\x00\x00\x00sjl_s2_shep_R1q\x1ae}q\x1b(h\x07}q\x1c(X\x06\x00\x00\x00prefixq\x1dK\x00N\x86q\x1eX\x0e\x00\x00\x00wrapper_sampleq\x1fK\x01N\x86q uh\x1fh\x1ah\x1dh\x19ubX\t\x00\x00\x00wildcardsq!csnakemake.io\nWildcards\nq")\x81q#h\x1aa}q$(h\x07}q%X\x06\x00\x00\x00sampleq&K\x00N\x86q\'sX\x06\x00\x00\x00sampleq(h\x1aubX\t\x00\x00\x00resourcesq)csnakemake.io\nResources\nq*)\x81q+(K\x01K\x01e}q,(h\x07}q-(X\x06\x00\x00\x00_nodesq.K\x00N\x86q/X\x06\x00\x00\x00_coresq0K\x01N\x86q1uh.K\x01h0K\x01ubX\x05\x00\x00\x00inputq2csnakemake.io\nInputFiles\nq3)\x81q4(X\x18\x00\x00\x00dedup/sjl_s2_shep_R1.bamq5X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq6e}q7(X\x02\x00\x00\x00ipq8h5X\x03\x00\x00\x00inpq9h6h\x07}q:(h8K\x00N\x86q;h9K\x01N\x86q<uubX\x07\x00\x00\x00threadsq=K\x01X\x04\x00\x00\x00ruleq>X\x05\x00\x00\x00macs2q?ub.')
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
