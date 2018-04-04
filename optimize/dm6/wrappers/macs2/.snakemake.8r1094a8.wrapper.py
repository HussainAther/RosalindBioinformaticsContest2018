
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\t\x00\x00\x00resourcesq\x04csnakemake.io\nResources\nq\x05)\x81q\x06(K\x01K\x01e}q\x07(X\x06\x00\x00\x00_namesq\x08}q\t(X\x06\x00\x00\x00_coresq\nK\x00N\x86q\x0bX\x06\x00\x00\x00_nodesq\x0cK\x01N\x86q\ruh\x0cK\x01h\nK\x01ubX\x06\x00\x00\x00outputq\x0ecsnakemake.io\nOutputFiles\nq\x0f)\x81q\x10(X2\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1/sjl_cl8_suhw_R1.bedq\x11X?\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1/sjl_cl8_suhw_R1_peaks.narrowPeakq\x12e}q\x13(h\x08}q\x14(X\n\x00\x00\x00narrowPeakq\x15K\x01N\x86q\x16X\x03\x00\x00\x00bedq\x17K\x00N\x86q\x18uh\x15h\x12h\x17h\x11ubX\x03\x00\x00\x00logq\x19csnakemake.io\nLog\nq\x1a)\x81q\x1b}q\x1ch\x08}q\x1dsbX\x06\x00\x00\x00paramsq\x1ecsnakemake.io\nParams\nq\x1f)\x81q X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1q!a}q"(h\x08}q#X\x06\x00\x00\x00prefixq$K\x00N\x86q%sh$h!ubX\t\x00\x00\x00wildcardsq&csnakemake.io\nWildcards\nq\')\x81q(X\x0f\x00\x00\x00sjl_cl8_suhw_R1q)a}q*(h\x08}q+X\x06\x00\x00\x00sampleq,K\x00N\x86q-sX\x06\x00\x00\x00sampleq.h)ubX\x04\x00\x00\x00ruleq/X\x05\x00\x00\x00macs2q0X\x06\x00\x00\x00configq1}q2X\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq6X\x19\x00\x00\x00dedup/sjl_cl8_suhw_R1.bamq7e}q8(h\x08}q9(X\x03\x00\x00\x00inpq:K\x00N\x86q;X\x02\x00\x00\x00ipq<K\x01N\x86q=uh:h6h<h7ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.sample}_model.r')
