
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\x06\x00\x00\x00paramsq\x05csnakemake.io\nParams\nq\x06)\x81q\x07X"\x00\x00\x00peak_out/macs2/lm39_kc_rm62-rat_R1q\x08a}q\t(X\x06\x00\x00\x00prefixq\nh\x08X\x06\x00\x00\x00_namesq\x0b}q\x0ch\nK\x00N\x86q\rsubX\t\x00\x00\x00wildcardsq\x0ecsnakemake.io\nWildcards\nq\x0f)\x81q\x10X\x13\x00\x00\x00lm39_kc_rm62-rat_R1q\x11a}q\x12(X\x06\x00\x00\x00sampleq\x13h\x11h\x0b}q\x14X\x06\x00\x00\x00sampleq\x15K\x00N\x86q\x16subX\t\x00\x00\x00resourcesq\x17csnakemake.io\nResources\nq\x18)\x81q\x19(K\x01K\x01e}q\x1a(X\x06\x00\x00\x00_coresq\x1bK\x01h\x0b}q\x1c(h\x1bK\x00N\x86q\x1dX\x06\x00\x00\x00_nodesq\x1eK\x01N\x86q\x1fuh\x1eK\x01ubX\x03\x00\x00\x00logq csnakemake.io\nLog\nq!)\x81q"}q#h\x0b}q$sbX\x05\x00\x00\x00inputq%csnakemake.io\nInputFiles\nq&)\x81q\'(X\x1d\x00\x00\x00dedup/lm39_kc_rm62-rat_R1.bamq(X\x1a\x00\x00\x00dedup/lm09_kc_input_R1.bamq)e}q*(h\x0b}q+(X\x02\x00\x00\x00ipq,K\x00N\x86q-X\x03\x00\x00\x00inpq.K\x01N\x86q/uh.h)h,h(ubX\x07\x00\x00\x00threadsq0K\x01X\x06\x00\x00\x00outputq1csnakemake.io\nOutputFiles\nq2)\x81q3(XG\x00\x00\x00peak_out/macs2/lm39_kc_rm62-rat_R1/lm39_kc_rm62-rat_R1_peaks.narrowPeakq4X:\x00\x00\x00peak_out/macs2/lm39_kc_rm62-rat_R1/lm39_kc_rm62-rat_R1.bedq5e}q6(h\x0b}q7(X\n\x00\x00\x00narrowPeakq8K\x00N\x86q9X\x03\x00\x00\x00bedq:K\x01N\x86q;uh:h5h8h4ubX\x06\x00\x00\x00configq<}q=ub.')
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
