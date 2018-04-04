
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x05\x00\x00\x00inputq\tcsnakemake.io\nInputFiles\nq\n)\x81q\x0b(X\x1a\x00\x00\x00dedup/sjl_mbn2_shep_R1.bamq\x0cX\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\re}q\x0e(X\x02\x00\x00\x00ipq\x0fh\x0ch\x07}q\x10(h\x0fK\x00N\x86q\x11X\x03\x00\x00\x00inpq\x12K\x01N\x86q\x13uh\x12h\rubX\x06\x00\x00\x00outputq\x14csnakemake.io\nOutputFiles\nq\x15)\x81q\x16(X4\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1.bedq\x17XA\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1_peaks.narrowPeakq\x18e}q\x19(X\x03\x00\x00\x00bedq\x1ah\x17h\x07}q\x1b(X\n\x00\x00\x00narrowPeakq\x1cK\x01N\x86q\x1dh\x1aK\x00N\x86q\x1euh\x1ch\x18ubX\x07\x00\x00\x00threadsq\x1fK\x01X\x04\x00\x00\x00ruleq X\x05\x00\x00\x00macs2q!X\x06\x00\x00\x00paramsq"csnakemake.io\nParams\nq#)\x81q$(X\x10\x00\x00\x00sjl_mbn2_shep_R1q%X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1q&e}q\'(h\x07}q((X\x0e\x00\x00\x00wrapper_sampleq)K\x00N\x86q*X\x06\x00\x00\x00prefixq+K\x01N\x86q,uh)h%h+h&ubX\x06\x00\x00\x00configq-}q.X\t\x00\x00\x00wildcardsq/csnakemake.io\nWildcards\nq0)\x81q1h%a}q2(h\x07}q3X\x06\x00\x00\x00sampleq4K\x00N\x86q5sX\x06\x00\x00\x00sampleq6h%ubX\t\x00\x00\x00resourcesq7csnakemake.io\nResources\nq8)\x81q9(K\x01K\x01e}q:(h\x07}q;(X\x06\x00\x00\x00_coresq<K\x00N\x86q=X\x06\x00\x00\x00_nodesq>K\x01N\x86q?uh<K\x01h>K\x01ubub.')
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
