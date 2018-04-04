
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1q\x06a}q\x07(X\x06\x00\x00\x00prefixq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nh\x08K\x00N\x86q\x0bsubX\x03\x00\x00\x00logq\x0ccsnakemake.io\nLog\nq\r)\x81q\x0e}q\x0fh\t}q\x10sbX\x07\x00\x00\x00threadsq\x11K\x01X\x06\x00\x00\x00outputq\x12csnakemake.io\nOutputFiles\nq\x13)\x81q\x14(X2\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1/sjl_cl8_suhw_R1.bedq\x15X?\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1/sjl_cl8_suhw_R1_peaks.narrowPeakq\x16e}q\x17(X\x03\x00\x00\x00bedq\x18h\x15X\n\x00\x00\x00narrowPeakq\x19h\x16h\t}q\x1a(h\x18K\x00N\x86q\x1bh\x19K\x01N\x86q\x1cuubX\t\x00\x00\x00wildcardsq\x1dcsnakemake.io\nWildcards\nq\x1e)\x81q\x1fX\x0f\x00\x00\x00sjl_cl8_suhw_R1q a}q!(X\x06\x00\x00\x00sampleq"h h\t}q#X\x06\x00\x00\x00sampleq$K\x00N\x86q%subX\x06\x00\x00\x00configq&}q\'X\t\x00\x00\x00resourcesq(csnakemake.io\nResources\nq))\x81q*(K\x01K\x01e}q+(X\x06\x00\x00\x00_coresq,K\x01X\x06\x00\x00\x00_nodesq-K\x01h\t}q.(h,K\x00N\x86q/h-K\x01N\x86q0uubX\x05\x00\x00\x00inputq1csnakemake.io\nInputFiles\nq2)\x81q3(X\x19\x00\x00\x00dedup/sjl_cl8_suhw_R1.bamq4X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq5e}q6(X\x02\x00\x00\x00ipq7h4X\x03\x00\x00\x00inpq8h5h\t}q9(h7K\x00N\x86q:h8K\x01N\x86q;uubX\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=ub.')
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
