
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x05\x00\x00\x00inputq\tcsnakemake.io\nInputFiles\nq\n)\x81q\x0b(X\x1d\x00\x00\x00dedup/lm41_kc_rump-5g4_R1.bamq\x0cX\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq\re}q\x0e(X\x02\x00\x00\x00ipq\x0fh\x0cX\x03\x00\x00\x00inpq\x10h\rh\x07}q\x11(h\x0fK\x00N\x86q\x12h\x10K\x01N\x86q\x13uubX\x04\x00\x00\x00ruleq\x14X\x05\x00\x00\x00macs2q\x15X\x06\x00\x00\x00outputq\x16csnakemake.io\nOutputFiles\nq\x17)\x81q\x18(XG\x00\x00\x00peak_out/macs2/lm41_kc_rump-5g4_R1/lm41_kc_rump-5g4_R1_peaks.narrowPeakq\x19X:\x00\x00\x00peak_out/macs2/lm41_kc_rump-5g4_R1/lm41_kc_rump-5g4_R1.bedq\x1ae}q\x1b(X\n\x00\x00\x00narrowPeakq\x1ch\x19X\x03\x00\x00\x00bedq\x1dh\x1ah\x07}q\x1e(h\x1cK\x00N\x86q\x1fh\x1dK\x01N\x86q uubX\x06\x00\x00\x00paramsq!csnakemake.io\nParams\nq")\x81q#(X"\x00\x00\x00peak_out/macs2/lm41_kc_rump-5g4_R1q$X\x13\x00\x00\x00lm41_kc_rump-5g4_R1q%e}q&(X\x0e\x00\x00\x00wrapper_sampleq\'h%X\x06\x00\x00\x00prefixq(h$h\x07}q)(h(K\x00N\x86q*h\'K\x01N\x86q+uubX\x07\x00\x00\x00threadsq,K\x01X\t\x00\x00\x00resourcesq-csnakemake.io\nResources\nq.)\x81q/(K\x01K\x01e}q0(X\x06\x00\x00\x00_coresq1K\x01X\x06\x00\x00\x00_nodesq2K\x01h\x07}q3(h1K\x00N\x86q4h2K\x01N\x86q5uubX\t\x00\x00\x00wildcardsq6csnakemake.io\nWildcards\nq7)\x81q8h%a}q9(X\x06\x00\x00\x00sampleq:h%h\x07}q;X\x06\x00\x00\x00sampleq<K\x00N\x86q=subX\x06\x00\x00\x00configq>}q?ub.')
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
