
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x05\x00\x00\x00inputq\x04csnakemake.io\nInputFiles\nq\x05)\x81q\x06(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq\x07X\x18\x00\x00\x00dedup/sjl_s3_shep_R1.bamq\x08e}q\t(X\x03\x00\x00\x00inpq\nh\x07X\x02\x00\x00\x00ipq\x0bh\x08X\x06\x00\x00\x00_namesq\x0c}q\r(h\nK\x00N\x86q\x0eh\x0bK\x01N\x86q\x0fuubX\x03\x00\x00\x00logq\x10csnakemake.io\nLog\nq\x11)\x81q\x12}q\x13h\x0c}q\x14sbX\x06\x00\x00\x00configq\x15}q\x16X\x04\x00\x00\x00ruleq\x17X\x05\x00\x00\x00macs2q\x18X\x06\x00\x00\x00outputq\x19csnakemake.io\nOutputFiles\nq\x1a)\x81q\x1b(X0\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1/sjl_s3_shep_R1.bedq\x1cX=\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1/sjl_s3_shep_R1_peaks.narrowPeakq\x1de}q\x1e(X\x03\x00\x00\x00bedq\x1fh\x1ch\x0c}q (h\x1fK\x00N\x86q!X\n\x00\x00\x00narrowPeakq"K\x01N\x86q#uh"h\x1dubX\x06\x00\x00\x00paramsq$csnakemake.io\nParams\nq%)\x81q&(X\x0e\x00\x00\x00sjl_s3_shep_R1q\'X\x1d\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1q(e}q)(X\x06\x00\x00\x00prefixq*h(X\x0e\x00\x00\x00wrapper_sampleq+h\'h\x0c}q,(h+K\x00N\x86q-h*K\x01N\x86q.uubX\t\x00\x00\x00resourcesq/csnakemake.io\nResources\nq0)\x81q1(K\x01K\x01e}q2(X\x06\x00\x00\x00_nodesq3K\x01h\x0c}q4(h3K\x00N\x86q5X\x06\x00\x00\x00_coresq6K\x01N\x86q7uh6K\x01ubX\t\x00\x00\x00wildcardsq8csnakemake.io\nWildcards\nq9)\x81q:h\'a}q;(h\x0c}q<X\x06\x00\x00\x00sampleq=K\x00N\x86q>sX\x06\x00\x00\x00sampleq?h\'ubub.')
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
