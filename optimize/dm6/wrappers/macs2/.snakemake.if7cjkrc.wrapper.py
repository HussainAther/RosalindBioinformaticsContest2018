
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00paramsq\x04csnakemake.io\nParams\nq\x05)\x81q\x06(X\x13\x00\x00\x00lm36_bg3_shep-r6_R1q\x07X"\x00\x00\x00peak_out/macs2/lm36_bg3_shep-r6_R1q\x08e}q\t(X\x0e\x00\x00\x00wrapper_sampleq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\nK\x00N\x86q\rX\x06\x00\x00\x00prefixq\x0eK\x01N\x86q\x0fuh\x0eh\x08ubX\x04\x00\x00\x00ruleq\x10X\x05\x00\x00\x00macs2q\x11X\x03\x00\x00\x00logq\x12csnakemake.io\nLog\nq\x13)\x81q\x14}q\x15h\x0b}q\x16sbX\t\x00\x00\x00wildcardsq\x17csnakemake.io\nWildcards\nq\x18)\x81q\x19h\x07a}q\x1a(h\x0b}q\x1bX\x06\x00\x00\x00sampleq\x1cK\x00N\x86q\x1dsX\x06\x00\x00\x00sampleq\x1eh\x07ubX\x05\x00\x00\x00inputq\x1fcsnakemake.io\nInputFiles\nq )\x81q!(X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq"X\x1d\x00\x00\x00dedup/lm36_bg3_shep-r6_R1.bamq#e}q$(h\x0b}q%(X\x03\x00\x00\x00inpq&K\x00N\x86q\'X\x02\x00\x00\x00ipq(K\x01N\x86q)uh&h"h(h#ubX\t\x00\x00\x00resourcesq*csnakemake.io\nResources\nq+)\x81q,(K\x01K\x01e}q-(h\x0b}q.(X\x06\x00\x00\x00_nodesq/K\x00N\x86q0X\x06\x00\x00\x00_coresq1K\x01N\x86q2uh1K\x01h/K\x01ubX\x06\x00\x00\x00configq3}q4X\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(X:\x00\x00\x00peak_out/macs2/lm36_bg3_shep-r6_R1/lm36_bg3_shep-r6_R1.bedq8XG\x00\x00\x00peak_out/macs2/lm36_bg3_shep-r6_R1/lm36_bg3_shep-r6_R1_peaks.narrowPeakq9e}q:(h\x0b}q;(X\x03\x00\x00\x00bedq<K\x00N\x86q=X\n\x00\x00\x00narrowPeakq>K\x01N\x86q?uh<h8h>h9ubub.')
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
