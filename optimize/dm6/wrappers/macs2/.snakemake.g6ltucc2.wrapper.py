
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X>\x00\x00\x00peak_out/macs2/lm48_bg3_rump-10c3_R1/lm48_bg3_rump-10c3_R1.bedq\x06XK\x00\x00\x00peak_out/macs2/lm48_bg3_rump-10c3_R1/lm48_bg3_rump-10c3_R1_peaks.narrowPeakq\x07e}q\x08(X\x03\x00\x00\x00bedq\th\x06X\n\x00\x00\x00narrowPeakq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x05\x00\x00\x00inputq\x0fcsnakemake.io\nInputFiles\nq\x10)\x81q\x11(X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq\x12X\x1f\x00\x00\x00dedup/lm48_bg3_rump-10c3_R1.bamq\x13e}q\x14(X\x03\x00\x00\x00inpq\x15h\x12X\x02\x00\x00\x00ipq\x16h\x13h\x0b}q\x17(h\x15K\x00N\x86q\x18h\x16K\x01N\x86q\x19uubX\t\x00\x00\x00resourcesq\x1acsnakemake.io\nResources\nq\x1b)\x81q\x1c(K\x01K\x01e}q\x1d(X\x06\x00\x00\x00_nodesq\x1eK\x01X\x06\x00\x00\x00_coresq\x1fK\x01h\x0b}q (h\x1eK\x00N\x86q!h\x1fK\x01N\x86q"uubX\t\x00\x00\x00wildcardsq#csnakemake.io\nWildcards\nq$)\x81q%X\x15\x00\x00\x00lm48_bg3_rump-10c3_R1q&a}q\'(X\x06\x00\x00\x00sampleq(h&h\x0b}q)X\x06\x00\x00\x00sampleq*K\x00N\x86q+subX\x03\x00\x00\x00logq,csnakemake.io\nLog\nq-)\x81q.}q/h\x0b}q0sbX\x07\x00\x00\x00threadsq1K\x01X\x06\x00\x00\x00configq2}q3X\x04\x00\x00\x00ruleq4X\x05\x00\x00\x00macs2q5X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X$\x00\x00\x00peak_out/macs2/lm48_bg3_rump-10c3_R1q9a}q:(X\x06\x00\x00\x00prefixq;h9h\x0b}q<h;K\x00N\x86q=subub.')
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
