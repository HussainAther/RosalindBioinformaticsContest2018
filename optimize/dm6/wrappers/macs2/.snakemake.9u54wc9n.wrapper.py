
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_namesq\x07}q\x08(X\x06\x00\x00\x00_nodesq\tK\x00N\x86q\nX\x06\x00\x00\x00_coresq\x0bK\x01N\x86q\x0cuh\tK\x01h\x0bK\x01ubX\t\x00\x00\x00wildcardsq\rcsnakemake.io\nWildcards\nq\x0e)\x81q\x0fX\x0e\x00\x00\x00sjl_kc_shep_R1q\x10a}q\x11(X\x06\x00\x00\x00sampleq\x12h\x10h\x07}q\x13X\x06\x00\x00\x00sampleq\x14K\x00N\x86q\x15subX\x07\x00\x00\x00threadsq\x16K\x01X\x06\x00\x00\x00paramsq\x17csnakemake.io\nParams\nq\x18)\x81q\x19X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q\x1aa}q\x1b(h\x07}q\x1cX\x06\x00\x00\x00prefixq\x1dK\x00N\x86q\x1esh\x1dh\x1aubX\x03\x00\x00\x00logq\x1fcsnakemake.io\nLog\nq )\x81q!}q"h\x07}q#sbX\x05\x00\x00\x00inputq$csnakemake.io\nInputFiles\nq%)\x81q&(X\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq\'X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq(e}q)(X\x02\x00\x00\x00ipq*h\'X\x03\x00\x00\x00inpq+h(h\x07}q,(h*K\x00N\x86q-h+K\x01N\x86q.uubX\x06\x00\x00\x00configq/}q0X\x06\x00\x00\x00outputq1csnakemake.io\nOutputFiles\nq2)\x81q3(X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq4X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq5e}q6(X\x03\x00\x00\x00bedq7h4h\x07}q8(h7K\x00N\x86q9X\n\x00\x00\x00narrowPeakq:K\x01N\x86q;uh:h5ubX\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=ub.')
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
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
