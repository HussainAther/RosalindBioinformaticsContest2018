
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x0f\x00\x00\x00sjl_s3_cp190_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00sampleq\nK\x00N\x86q\x0bsX\x06\x00\x00\x00sampleq\x0ch\x06ubX\x07\x00\x00\x00threadsq\rK\x01X\x05\x00\x00\x00inputq\x0ecsnakemake.io\nInputFiles\nq\x0f)\x81q\x10(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq\x11X\x19\x00\x00\x00dedup/sjl_s3_cp190_R1.bamq\x12e}q\x13(X\x03\x00\x00\x00inpq\x14h\x11h\x08}q\x15(h\x14K\x00N\x86q\x16X\x02\x00\x00\x00ipq\x17K\x01N\x86q\x18uh\x17h\x12ubX\x03\x00\x00\x00logq\x19csnakemake.io\nLog\nq\x1a)\x81q\x1b}q\x1ch\x08}q\x1dsbX\x06\x00\x00\x00configq\x1e}q\x1fX\t\x00\x00\x00resourcesq csnakemake.io\nResources\nq!)\x81q"(K\x01K\x01e}q#(h\x08}q$(X\x06\x00\x00\x00_coresq%K\x00N\x86q&X\x06\x00\x00\x00_nodesq\'K\x01N\x86q(uh%K\x01h\'K\x01ubX\x06\x00\x00\x00outputq)csnakemake.io\nOutputFiles\nq*)\x81q+(X2\x00\x00\x00peak_out/macs2/sjl_s3_cp190_R1/sjl_s3_cp190_R1.bedq,X?\x00\x00\x00peak_out/macs2/sjl_s3_cp190_R1/sjl_s3_cp190_R1_peaks.narrowPeakq-e}q.(X\x03\x00\x00\x00bedq/h,X\n\x00\x00\x00narrowPeakq0h-h\x08}q1(h/K\x00N\x86q2h0K\x01N\x86q3uubX\x04\x00\x00\x00ruleq4X\x05\x00\x00\x00macs2q5X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X\x1e\x00\x00\x00peak_out/macs2/sjl_s3_cp190_R1q9a}q:(h\x08}q;X\x06\x00\x00\x00prefixq<K\x00N\x86q=sh<h9ubub.')
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
