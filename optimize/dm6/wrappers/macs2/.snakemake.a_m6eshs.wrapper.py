
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\x06\x00\x00\x00configq\x05}q\x06X\t\x00\x00\x00wildcardsq\x07csnakemake.io\nWildcards\nq\x08)\x81q\tX\x12\x00\x00\x00lm07_kc_shep-r5_R1q\na}q\x0b(X\x06\x00\x00\x00sampleq\x0ch\nX\x06\x00\x00\x00_namesq\r}q\x0eX\x06\x00\x00\x00sampleq\x0fK\x00N\x86q\x10subX\x06\x00\x00\x00outputq\x11csnakemake.io\nOutputFiles\nq\x12)\x81q\x13(X8\x00\x00\x00peak_out/macs2/lm07_kc_shep-r5_R1/lm07_kc_shep-r5_R1.bedq\x14XE\x00\x00\x00peak_out/macs2/lm07_kc_shep-r5_R1/lm07_kc_shep-r5_R1_peaks.narrowPeakq\x15e}q\x16(X\x03\x00\x00\x00bedq\x17h\x14X\n\x00\x00\x00narrowPeakq\x18h\x15h\r}q\x19(h\x17K\x00N\x86q\x1ah\x18K\x01N\x86q\x1buubX\x06\x00\x00\x00paramsq\x1ccsnakemake.io\nParams\nq\x1d)\x81q\x1e(h\nX!\x00\x00\x00peak_out/macs2/lm07_kc_shep-r5_R1q\x1fe}q (X\x0e\x00\x00\x00wrapper_sampleq!h\nX\x06\x00\x00\x00prefixq"h\x1fh\r}q#(h!K\x00N\x86q$h"K\x01N\x86q%uubX\x05\x00\x00\x00inputq&csnakemake.io\nInputFiles\nq\')\x81q((X\x1c\x00\x00\x00dedup/lm07_kc_shep-r5_R1.bamq)X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq*e}q+(X\x02\x00\x00\x00ipq,h)X\x03\x00\x00\x00inpq-h*h\r}q.(h,K\x00N\x86q/h-K\x01N\x86q0uubX\x03\x00\x00\x00logq1csnakemake.io\nLog\nq2)\x81q3}q4h\r}q5sbX\t\x00\x00\x00resourcesq6csnakemake.io\nResources\nq7)\x81q8(K\x01K\x01e}q9(X\x06\x00\x00\x00_coresq:K\x01X\x06\x00\x00\x00_nodesq;K\x01h\r}q<(h;K\x00N\x86q=h:K\x01N\x86q>uubX\x07\x00\x00\x00threadsq?K\x01ub.')
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
