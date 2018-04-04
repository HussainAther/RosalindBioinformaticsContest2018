
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x03\x00\x00\x00logq\x05csnakemake.io\nLog\nq\x06)\x81q\x07}q\x08X\x06\x00\x00\x00_namesq\t}q\nsbX\t\x00\x00\x00resourcesq\x0bcsnakemake.io\nResources\nq\x0c)\x81q\r(K\x01K\x01e}q\x0e(h\t}q\x0f(X\x06\x00\x00\x00_nodesq\x10K\x00N\x86q\x11X\x06\x00\x00\x00_coresq\x12K\x01N\x86q\x13uh\x10K\x01h\x12K\x01ubX\x04\x00\x00\x00ruleq\x14X\x05\x00\x00\x00macs2q\x15X\x05\x00\x00\x00inputq\x16csnakemake.io\nInputFiles\nq\x17)\x81q\x18(X\x19\x00\x00\x00dedup/sjl_mbn2_mod_R1.bamq\x19X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x1ae}q\x1b(h\t}q\x1c(X\x02\x00\x00\x00ipq\x1dK\x00N\x86q\x1eX\x03\x00\x00\x00inpq\x1fK\x01N\x86q uh\x1dh\x19h\x1fh\x1aubX\x06\x00\x00\x00outputq!csnakemake.io\nOutputFiles\nq")\x81q#(X2\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1.bedq$X?\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1_peaks.narrowPeakq%e}q&(h\t}q\'(X\x03\x00\x00\x00bedq(K\x00N\x86q)X\n\x00\x00\x00narrowPeakq*K\x01N\x86q+uh(h$h*h%ubX\t\x00\x00\x00wildcardsq,csnakemake.io\nWildcards\nq-)\x81q.X\x0f\x00\x00\x00sjl_mbn2_mod_R1q/a}q0(h\t}q1X\x06\x00\x00\x00sampleq2K\x00N\x86q3sX\x06\x00\x00\x00sampleq4h/ubX\x07\x00\x00\x00threadsq5K\x01X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X\x1e\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1q9a}q:(h\t}q;X\x06\x00\x00\x00prefixq<K\x00N\x86q=sh<h9ubub.')
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
