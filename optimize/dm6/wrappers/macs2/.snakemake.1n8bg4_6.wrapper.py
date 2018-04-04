
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x19\x00\x00\x00dedup/sjl_cl8_suhw_R1.bamq\x06X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x07e}q\x08(X\x02\x00\x00\x00ipq\th\x06X\x03\x00\x00\x00inpq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1q\x12a}q\x13(X\x06\x00\x00\x00prefixq\x14h\x12h\x0b}q\x15h\x14K\x00N\x86q\x16subX\x04\x00\x00\x00ruleq\x17X\x05\x00\x00\x00macs2q\x18X\x07\x00\x00\x00threadsq\x19K\x01X\x03\x00\x00\x00logq\x1acsnakemake.io\nLog\nq\x1b)\x81q\x1c}q\x1dh\x0b}q\x1esbX\x06\x00\x00\x00outputq\x1fcsnakemake.io\nOutputFiles\nq )\x81q!(X?\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1/sjl_cl8_suhw_R1_peaks.narrowPeakq"X2\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1/sjl_cl8_suhw_R1.bedq#e}q$(X\n\x00\x00\x00narrowPeakq%h"X\x03\x00\x00\x00bedq&h#h\x0b}q\'(h%K\x00N\x86q(h&K\x01N\x86q)uubX\x06\x00\x00\x00configq*}q+X\t\x00\x00\x00wildcardsq,csnakemake.io\nWildcards\nq-)\x81q.X\x0f\x00\x00\x00sjl_cl8_suhw_R1q/a}q0(X\x06\x00\x00\x00sampleq1h/h\x0b}q2X\x06\x00\x00\x00sampleq3K\x00N\x86q4subX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_coresq9K\x01X\x06\x00\x00\x00_nodesq:K\x01h\x0b}q;(h:K\x00N\x86q<h9K\x01N\x86q=uubub.')
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
