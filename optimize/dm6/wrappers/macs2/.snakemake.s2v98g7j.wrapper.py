
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00paramsq\x04csnakemake.io\nParams\nq\x05)\x81q\x06(X$\x00\x00\x00peak_out/macs2/lm48_bg3_rump-10c3_R1q\x07X\x15\x00\x00\x00lm48_bg3_rump-10c3_R1q\x08e}q\t(X\x06\x00\x00\x00prefixq\nh\x07X\x0e\x00\x00\x00wrapper_sampleq\x0bh\x08X\x06\x00\x00\x00_namesq\x0c}q\r(h\nK\x00N\x86q\x0eh\x0bK\x01N\x86q\x0fuubX\x06\x00\x00\x00outputq\x10csnakemake.io\nOutputFiles\nq\x11)\x81q\x12(XK\x00\x00\x00peak_out/macs2/lm48_bg3_rump-10c3_R1/lm48_bg3_rump-10c3_R1_peaks.narrowPeakq\x13X>\x00\x00\x00peak_out/macs2/lm48_bg3_rump-10c3_R1/lm48_bg3_rump-10c3_R1.bedq\x14e}q\x15(X\n\x00\x00\x00narrowPeakq\x16h\x13X\x03\x00\x00\x00bedq\x17h\x14h\x0c}q\x18(h\x16K\x00N\x86q\x19h\x17K\x01N\x86q\x1auubX\x06\x00\x00\x00configq\x1b}q\x1cX\x03\x00\x00\x00logq\x1dcsnakemake.io\nLog\nq\x1e)\x81q\x1f}q h\x0c}q!sbX\x04\x00\x00\x00ruleq"X\x05\x00\x00\x00macs2q#X\x05\x00\x00\x00inputq$csnakemake.io\nInputFiles\nq%)\x81q&(X\x1f\x00\x00\x00dedup/lm48_bg3_rump-10c3_R1.bamq\'X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq(e}q)(X\x03\x00\x00\x00inpq*h(X\x02\x00\x00\x00ipq+h\'h\x0c}q,(h+K\x00N\x86q-h*K\x01N\x86q.uubX\t\x00\x00\x00wildcardsq/csnakemake.io\nWildcards\nq0)\x81q1h\x08a}q2(X\x06\x00\x00\x00sampleq3h\x08h\x0c}q4X\x06\x00\x00\x00sampleq5K\x00N\x86q6subX\t\x00\x00\x00resourcesq7csnakemake.io\nResources\nq8)\x81q9(K\x01K\x01e}q:(X\x06\x00\x00\x00_nodesq;K\x01X\x06\x00\x00\x00_coresq<K\x01h\x0c}q=(h;K\x00N\x86q>h<K\x01N\x86q?uubub.')
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
