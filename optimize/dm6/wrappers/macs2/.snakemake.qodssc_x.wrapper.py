
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(XG\x00\x00\x00peak_out/macs2/lm36_bg3_shep-r6_R1/lm36_bg3_shep-r6_R1_peaks.narrowPeakq\x06X:\x00\x00\x00peak_out/macs2/lm36_bg3_shep-r6_R1/lm36_bg3_shep-r6_R1.bedq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\n\x00\x00\x00narrowPeakq\x0bK\x00N\x86q\x0cX\x03\x00\x00\x00bedq\rK\x01N\x86q\x0euh\rh\x07h\x0bh\x06ubX\t\x00\x00\x00wildcardsq\x0fcsnakemake.io\nWildcards\nq\x10)\x81q\x11X\x13\x00\x00\x00lm36_bg3_shep-r6_R1q\x12a}q\x13(X\x06\x00\x00\x00sampleq\x14h\x12h\t}q\x15X\x06\x00\x00\x00sampleq\x16K\x00N\x86q\x17subX\x04\x00\x00\x00ruleq\x18X\x05\x00\x00\x00macs2q\x19X\x06\x00\x00\x00paramsq\x1acsnakemake.io\nParams\nq\x1b)\x81q\x1cX"\x00\x00\x00peak_out/macs2/lm36_bg3_shep-r6_R1q\x1da}q\x1e(X\x06\x00\x00\x00prefixq\x1fh\x1dh\t}q h\x1fK\x00N\x86q!subX\t\x00\x00\x00resourcesq"csnakemake.io\nResources\nq#)\x81q$(K\x01K\x01e}q%(X\x06\x00\x00\x00_coresq&K\x01h\t}q\'(X\x06\x00\x00\x00_nodesq(K\x00N\x86q)h&K\x01N\x86q*uh(K\x01ubX\x03\x00\x00\x00logq+csnakemake.io\nLog\nq,)\x81q-}q.h\t}q/sbX\x05\x00\x00\x00inputq0csnakemake.io\nInputFiles\nq1)\x81q2(X\x1d\x00\x00\x00dedup/lm36_bg3_shep-r6_R1.bamq3X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq4e}q5(h\t}q6(X\x02\x00\x00\x00ipq7K\x00N\x86q8X\x03\x00\x00\x00inpq9K\x01N\x86q:uh9h4h7h3ubX\x06\x00\x00\x00configq;}q<X\x07\x00\x00\x00threadsq=K\x01ub.')
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
