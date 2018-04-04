
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x04\x00\x00\x00ruleq\x05X\x05\x00\x00\x00macs2q\x06X\t\x00\x00\x00resourcesq\x07csnakemake.io\nResources\nq\x08)\x81q\t(K\x01K\x01e}q\n(X\x06\x00\x00\x00_coresq\x0bK\x01X\x06\x00\x00\x00_nodesq\x0cK\x01X\x06\x00\x00\x00_namesq\r}q\x0e(h\x0cK\x00N\x86q\x0fh\x0bK\x01N\x86q\x10uubX\x06\x00\x00\x00paramsq\x11csnakemake.io\nParams\nq\x12)\x81q\x13X\x1d\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1q\x14a}q\x15(X\x06\x00\x00\x00prefixq\x16h\x14h\r}q\x17h\x16K\x00N\x86q\x18subX\x06\x00\x00\x00outputq\x19csnakemake.io\nOutputFiles\nq\x1a)\x81q\x1b(X=\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1/sjl_s3_shep_R1_peaks.narrowPeakq\x1cX0\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1/sjl_s3_shep_R1.bedq\x1de}q\x1e(X\n\x00\x00\x00narrowPeakq\x1fh\x1cX\x03\x00\x00\x00bedq h\x1dh\r}q!(h\x1fK\x00N\x86q"h K\x01N\x86q#uubX\x05\x00\x00\x00inputq$csnakemake.io\nInputFiles\nq%)\x81q&(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq\'X\x18\x00\x00\x00dedup/sjl_s3_shep_R1.bamq(e}q)(X\x03\x00\x00\x00inpq*h\'X\x02\x00\x00\x00ipq+h(h\r}q,(h*K\x00N\x86q-h+K\x01N\x86q.uubX\t\x00\x00\x00wildcardsq/csnakemake.io\nWildcards\nq0)\x81q1X\x0e\x00\x00\x00sjl_s3_shep_R1q2a}q3(X\x06\x00\x00\x00sampleq4h2h\r}q5X\x06\x00\x00\x00sampleq6K\x00N\x86q7subX\x07\x00\x00\x00threadsq8K\x01X\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\r}q=sbub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.input.ip}_model.r')
