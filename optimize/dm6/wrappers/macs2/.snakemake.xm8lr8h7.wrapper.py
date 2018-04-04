
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_coresq\x07K\x01X\x06\x00\x00\x00_nodesq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x07K\x00N\x86q\x0bh\x08K\x01N\x86q\x0cuubX\x06\x00\x00\x00configq\r}q\x0eX\x05\x00\x00\x00inputq\x0fcsnakemake.io\nInputFiles\nq\x10)\x81q\x11(X\x1f\x00\x00\x00dedup/el41_bg3_rump-10c3_R1.bamq\x12X\x1b\x00\x00\x00dedup/el37_bg3_input_R1.bamq\x13e}q\x14(X\x02\x00\x00\x00ipq\x15h\x12X\x03\x00\x00\x00inpq\x16h\x13h\t}q\x17(h\x15K\x00N\x86q\x18h\x16K\x01N\x86q\x19uubX\x03\x00\x00\x00logq\x1acsnakemake.io\nLog\nq\x1b)\x81q\x1c}q\x1dh\t}q\x1esbX\x04\x00\x00\x00ruleq\x1fX\x05\x00\x00\x00macs2q X\x06\x00\x00\x00paramsq!csnakemake.io\nParams\nq")\x81q#X$\x00\x00\x00peak_out/macs2/el41_bg3_rump-10c3_R1q$a}q%(X\x06\x00\x00\x00prefixq&h$h\t}q\'h&K\x00N\x86q(subX\t\x00\x00\x00wildcardsq)csnakemake.io\nWildcards\nq*)\x81q+X\x15\x00\x00\x00el41_bg3_rump-10c3_R1q,a}q-(X\x06\x00\x00\x00sampleq.h,h\t}q/X\x06\x00\x00\x00sampleq0K\x00N\x86q1subX\x07\x00\x00\x00threadsq2K\x01X\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X>\x00\x00\x00peak_out/macs2/el41_bg3_rump-10c3_R1/el41_bg3_rump-10c3_R1.bedq6XK\x00\x00\x00peak_out/macs2/el41_bg3_rump-10c3_R1/el41_bg3_rump-10c3_R1_peaks.narrowPeakq7e}q8(X\x03\x00\x00\x00bedq9h6h\t}q:(h9K\x00N\x86q;X\n\x00\x00\x00narrowPeakq<K\x01N\x86q=uh<h7ubub.')
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
