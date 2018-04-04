
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\x06\x00\x00\x00paramsq\x05csnakemake.io\nParams\nq\x06)\x81q\x07X$\x00\x00\x00peak_out/macs2/el41_bg3_rump-10c3_R1q\x08a}q\t(X\x06\x00\x00\x00prefixq\nh\x08X\x06\x00\x00\x00_namesq\x0b}q\x0ch\nK\x00N\x86q\rsubX\x03\x00\x00\x00logq\x0ecsnakemake.io\nLog\nq\x0f)\x81q\x10}q\x11h\x0b}q\x12sbX\t\x00\x00\x00wildcardsq\x13csnakemake.io\nWildcards\nq\x14)\x81q\x15X\x15\x00\x00\x00el41_bg3_rump-10c3_R1q\x16a}q\x17(h\x0b}q\x18X\x06\x00\x00\x00sampleq\x19K\x00N\x86q\x1asX\x06\x00\x00\x00sampleq\x1bh\x16ubX\t\x00\x00\x00resourcesq\x1ccsnakemake.io\nResources\nq\x1d)\x81q\x1e(K\x01K\x01e}q\x1f(X\x06\x00\x00\x00_nodesq K\x01h\x0b}q!(h K\x00N\x86q"X\x06\x00\x00\x00_coresq#K\x01N\x86q$uh#K\x01ubX\x06\x00\x00\x00outputq%csnakemake.io\nOutputFiles\nq&)\x81q\'(X>\x00\x00\x00peak_out/macs2/el41_bg3_rump-10c3_R1/el41_bg3_rump-10c3_R1.bedq(XK\x00\x00\x00peak_out/macs2/el41_bg3_rump-10c3_R1/el41_bg3_rump-10c3_R1_peaks.narrowPeakq)e}q*(X\x03\x00\x00\x00bedq+h(X\n\x00\x00\x00narrowPeakq,h)h\x0b}q-(h+K\x00N\x86q.h,K\x01N\x86q/uubX\x05\x00\x00\x00inputq0csnakemake.io\nInputFiles\nq1)\x81q2(X\x1b\x00\x00\x00dedup/el37_bg3_input_R1.bamq3X\x1f\x00\x00\x00dedup/el41_bg3_rump-10c3_R1.bamq4e}q5(X\x03\x00\x00\x00inpq6h3h\x0b}q7(h6K\x00N\x86q8X\x02\x00\x00\x00ipq9K\x01N\x86q:uh9h4ubX\x06\x00\x00\x00configq;}q<X\x07\x00\x00\x00threadsq=K\x01ub.')
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
