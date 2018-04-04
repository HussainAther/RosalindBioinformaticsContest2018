
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05X"\x00\x00\x00peak_out/macs2/lm47_bg3_rump5g4_R1q\x06a}q\x07(X\x06\x00\x00\x00prefixq\x08h\x06X\x06\x00\x00\x00_namesq\t}q\nh\x08K\x00N\x86q\x0bsubX\t\x00\x00\x00resourcesq\x0ccsnakemake.io\nResources\nq\r)\x81q\x0e(K\x01K\x01e}q\x0f(X\x06\x00\x00\x00_nodesq\x10K\x01X\x06\x00\x00\x00_coresq\x11K\x01h\t}q\x12(h\x10K\x01N\x86q\x13h\x11K\x00N\x86q\x14uubX\x06\x00\x00\x00outputq\x15csnakemake.io\nOutputFiles\nq\x16)\x81q\x17(X:\x00\x00\x00peak_out/macs2/lm47_bg3_rump5g4_R1/lm47_bg3_rump5g4_R1.bedq\x18XG\x00\x00\x00peak_out/macs2/lm47_bg3_rump5g4_R1/lm47_bg3_rump5g4_R1_peaks.narrowPeakq\x19e}q\x1a(X\x03\x00\x00\x00bedq\x1bh\x18X\n\x00\x00\x00narrowPeakq\x1ch\x19h\t}q\x1d(h\x1bK\x00N\x86q\x1eh\x1cK\x01N\x86q\x1fuubX\x03\x00\x00\x00logq csnakemake.io\nLog\nq!)\x81q"}q#h\t}q$sbX\x07\x00\x00\x00threadsq%K\x01X\x05\x00\x00\x00inputq&csnakemake.io\nInputFiles\nq\')\x81q((X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq)X\x1d\x00\x00\x00dedup/lm47_bg3_rump5g4_R1.bamq*e}q+(X\x03\x00\x00\x00inpq,h)X\x02\x00\x00\x00ipq-h*h\t}q.(h,K\x00N\x86q/h-K\x01N\x86q0uubX\t\x00\x00\x00wildcardsq1csnakemake.io\nWildcards\nq2)\x81q3X\x13\x00\x00\x00lm47_bg3_rump5g4_R1q4a}q5(X\x06\x00\x00\x00sampleq6h4h\t}q7X\x06\x00\x00\x00sampleq8K\x00N\x86q9subX\x06\x00\x00\x00configq:}q;X\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=ub.')
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
