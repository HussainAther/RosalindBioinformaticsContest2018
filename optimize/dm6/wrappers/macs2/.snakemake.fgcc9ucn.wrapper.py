
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x03\x00\x00\x00logq\x05csnakemake.io\nLog\nq\x06)\x81q\x07}q\x08X\x06\x00\x00\x00_namesq\t}q\nsbX\x06\x00\x00\x00paramsq\x0bcsnakemake.io\nParams\nq\x0c)\x81q\rX#\x00\x00\x00peak_out/macs2/el42_kc_rump-10c3_R1q\x0ea}q\x0f(h\t}q\x10X\x06\x00\x00\x00prefixq\x11K\x00N\x86q\x12sh\x11h\x0eubX\x05\x00\x00\x00inputq\x13csnakemake.io\nInputFiles\nq\x14)\x81q\x15(X\x1a\x00\x00\x00dedup/el38_kc_input_R1.bamq\x16X\x1e\x00\x00\x00dedup/el42_kc_rump-10c3_R1.bamq\x17e}q\x18(h\t}q\x19(X\x03\x00\x00\x00inpq\x1aK\x00N\x86q\x1bX\x02\x00\x00\x00ipq\x1cK\x01N\x86q\x1duh\x1ah\x16h\x1ch\x17ubX\t\x00\x00\x00wildcardsq\x1ecsnakemake.io\nWildcards\nq\x1f)\x81q X\x14\x00\x00\x00el42_kc_rump-10c3_R1q!a}q"(h\t}q#X\x06\x00\x00\x00sampleq$K\x00N\x86q%sX\x06\x00\x00\x00sampleq&h!ubX\t\x00\x00\x00resourcesq\'csnakemake.io\nResources\nq()\x81q)(K\x01K\x01e}q*(h\t}q+(X\x06\x00\x00\x00_coresq,K\x00N\x86q-X\x06\x00\x00\x00_nodesq.K\x01N\x86q/uh.K\x01h,K\x01ubX\x04\x00\x00\x00ruleq0X\x05\x00\x00\x00macs2q1X\x07\x00\x00\x00threadsq2K\x01X\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X<\x00\x00\x00peak_out/macs2/el42_kc_rump-10c3_R1/el42_kc_rump-10c3_R1.bedq6XI\x00\x00\x00peak_out/macs2/el42_kc_rump-10c3_R1/el42_kc_rump-10c3_R1_peaks.narrowPeakq7e}q8(X\x03\x00\x00\x00bedq9h6h\t}q:(h9K\x00N\x86q;X\n\x00\x00\x00narrowPeakq<K\x01N\x86q=uh<h7ubub.')
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
