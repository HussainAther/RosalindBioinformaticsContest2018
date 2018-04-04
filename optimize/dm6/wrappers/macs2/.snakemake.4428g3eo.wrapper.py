
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\x06\x00\x00\x00outputq\x05csnakemake.io\nOutputFiles\nq\x06)\x81q\x07(X8\x00\x00\x00peak_out/macs2/lm10_kc_shep-gp_R1/lm10_kc_shep-gp_R1.bedq\x08XE\x00\x00\x00peak_out/macs2/lm10_kc_shep-gp_R1/lm10_kc_shep-gp_R1_peaks.narrowPeakq\te}q\n(X\x06\x00\x00\x00_namesq\x0b}q\x0c(X\x03\x00\x00\x00bedq\rK\x00N\x86q\x0eX\n\x00\x00\x00narrowPeakq\x0fK\x01N\x86q\x10uh\rh\x08h\x0fh\tubX\x03\x00\x00\x00logq\x11csnakemake.io\nLog\nq\x12)\x81q\x13}q\x14h\x0b}q\x15sbX\x07\x00\x00\x00threadsq\x16K\x01X\t\x00\x00\x00resourcesq\x17csnakemake.io\nResources\nq\x18)\x81q\x19(K\x01K\x01e}q\x1a(X\x06\x00\x00\x00_coresq\x1bK\x01h\x0b}q\x1c(h\x1bK\x00N\x86q\x1dX\x06\x00\x00\x00_nodesq\x1eK\x01N\x86q\x1fuh\x1eK\x01ubX\t\x00\x00\x00wildcardsq csnakemake.io\nWildcards\nq!)\x81q"X\x12\x00\x00\x00lm10_kc_shep-gp_R1q#a}q$(h\x0b}q%X\x06\x00\x00\x00sampleq&K\x00N\x86q\'sX\x06\x00\x00\x00sampleq(h#ubX\x06\x00\x00\x00paramsq)csnakemake.io\nParams\nq*)\x81q+X!\x00\x00\x00peak_out/macs2/lm10_kc_shep-gp_R1q,a}q-(h\x0b}q.X\x06\x00\x00\x00prefixq/K\x00N\x86q0sh/h,ubX\x05\x00\x00\x00inputq1csnakemake.io\nInputFiles\nq2)\x81q3(X\x1c\x00\x00\x00dedup/lm10_kc_shep-gp_R1.bamq4X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq5e}q6(h\x0b}q7(X\x02\x00\x00\x00ipq8K\x00N\x86q9X\x03\x00\x00\x00inpq:K\x01N\x86q;uh8h4h:h5ubX\x06\x00\x00\x00configq<}q=ub.')
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
