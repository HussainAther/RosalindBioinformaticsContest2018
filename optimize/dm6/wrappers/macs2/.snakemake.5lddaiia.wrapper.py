
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x13\x00\x00\x00lm41_kc_rump-5g4_R1q\x06a}q\x07(X\x06\x00\x00\x00sampleq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nX\x06\x00\x00\x00sampleq\x0bK\x00N\x86q\x0csubX\x03\x00\x00\x00logq\rcsnakemake.io\nLog\nq\x0e)\x81q\x0f}q\x10h\t}q\x11sbX\t\x00\x00\x00resourcesq\x12csnakemake.io\nResources\nq\x13)\x81q\x14(K\x01K\x01e}q\x15(h\t}q\x16(X\x06\x00\x00\x00_nodesq\x17K\x00N\x86q\x18X\x06\x00\x00\x00_coresq\x19K\x01N\x86q\x1auh\x17K\x01h\x19K\x01ubX\x05\x00\x00\x00inputq\x1bcsnakemake.io\nInputFiles\nq\x1c)\x81q\x1d(X\x1d\x00\x00\x00dedup/lm41_kc_rump-5g4_R1.bamq\x1eX\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq\x1fe}q (h\t}q!(X\x02\x00\x00\x00ipq"K\x00N\x86q#X\x03\x00\x00\x00inpq$K\x01N\x86q%uh"h\x1eh$h\x1fubX\x06\x00\x00\x00paramsq&csnakemake.io\nParams\nq\')\x81q(X"\x00\x00\x00peak_out/macs2/lm41_kc_rump-5g4_R1q)a}q*(h\t}q+X\x06\x00\x00\x00prefixq,K\x00N\x86q-sh,h)ubX\x06\x00\x00\x00configq.}q/X\x07\x00\x00\x00threadsq0K\x01X\x06\x00\x00\x00outputq1csnakemake.io\nOutputFiles\nq2)\x81q3(XG\x00\x00\x00peak_out/macs2/lm41_kc_rump-5g4_R1/lm41_kc_rump-5g4_R1_peaks.narrowPeakq4X:\x00\x00\x00peak_out/macs2/lm41_kc_rump-5g4_R1/lm41_kc_rump-5g4_R1.bedq5e}q6(h\t}q7(X\n\x00\x00\x00narrowPeakq8K\x00N\x86q9X\x03\x00\x00\x00bedq:K\x01N\x86q;uh8h4h:h5ubX\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=ub.')
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
