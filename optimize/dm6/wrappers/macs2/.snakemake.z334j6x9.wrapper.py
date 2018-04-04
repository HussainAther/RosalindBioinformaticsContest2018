
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq\x06X\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq\x07e}q\x08(X\x03\x00\x00\x00inpq\th\x06X\x02\x00\x00\x00ipq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x06\x00\x00\x00outputq\x0fcsnakemake.io\nOutputFiles\nq\x10)\x81q\x11(X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq\x12X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq\x13e}q\x14(X\n\x00\x00\x00narrowPeakq\x15h\x12X\x03\x00\x00\x00bedq\x16h\x13h\x0b}q\x17(h\x15K\x00N\x86q\x18h\x16K\x01N\x86q\x19uubX\t\x00\x00\x00wildcardsq\x1acsnakemake.io\nWildcards\nq\x1b)\x81q\x1cX\x0e\x00\x00\x00sjl_kc_shep_R1q\x1da}q\x1e(X\x06\x00\x00\x00sampleq\x1fh\x1dh\x0b}q X\x06\x00\x00\x00sampleq!K\x00N\x86q"subX\x03\x00\x00\x00logq#csnakemake.io\nLog\nq$)\x81q%}q&h\x0b}q\'sbX\x07\x00\x00\x00threadsq(K\x01X\x04\x00\x00\x00ruleq)X\x05\x00\x00\x00macs2q*X\x06\x00\x00\x00paramsq+csnakemake.io\nParams\nq,)\x81q-X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q.a}q/(X\x06\x00\x00\x00prefixq0h.h\x0b}q1h0K\x00N\x86q2subX\x06\x00\x00\x00configq3}q4X\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_coresq9K\x01X\x06\x00\x00\x00_nodesq:K\x01h\x0b}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubub.')
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
shell('Rscript {snakemake.params.prefix}_model.r')
