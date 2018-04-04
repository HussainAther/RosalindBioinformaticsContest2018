
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\t\x00\x00\x00resourcesq\tcsnakemake.io\nResources\nq\n)\x81q\x0b(K\x01K\x01e}q\x0c(X\x06\x00\x00\x00_nodesq\rK\x01X\x06\x00\x00\x00_coresq\x0eK\x01h\x07}q\x0f(h\rK\x00N\x86q\x10h\x0eK\x01N\x86q\x11uubX\x06\x00\x00\x00paramsq\x12csnakemake.io\nParams\nq\x13)\x81q\x14(X#\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1q\x15X\x14\x00\x00\x00el39_bg3_rump-5g4_R1q\x16e}q\x17(X\x06\x00\x00\x00prefixq\x18h\x15X\x0e\x00\x00\x00wrapper_sampleq\x19h\x16h\x07}q\x1a(h\x18K\x00N\x86q\x1bh\x19K\x01N\x86q\x1cuubX\x06\x00\x00\x00configq\x1d}q\x1eX\x06\x00\x00\x00outputq\x1fcsnakemake.io\nOutputFiles\nq )\x81q!(XI\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1/el39_bg3_rump-5g4_R1_peaks.narrowPeakq"X<\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1/el39_bg3_rump-5g4_R1.bedq#e}q$(X\n\x00\x00\x00narrowPeakq%h"X\x03\x00\x00\x00bedq&h#h\x07}q\'(h%K\x00N\x86q(h&K\x01N\x86q)uubX\x07\x00\x00\x00threadsq*K\x01X\x04\x00\x00\x00ruleq+X\x05\x00\x00\x00macs2q,X\t\x00\x00\x00wildcardsq-csnakemake.io\nWildcards\nq.)\x81q/h\x16a}q0(X\x06\x00\x00\x00sampleq1h\x16h\x07}q2X\x06\x00\x00\x00sampleq3K\x00N\x86q4subX\x05\x00\x00\x00inputq5csnakemake.io\nInputFiles\nq6)\x81q7(X\x1b\x00\x00\x00dedup/el37_bg3_input_R1.bamq8X\x1e\x00\x00\x00dedup/el39_bg3_rump-5g4_R1.bamq9e}q:(X\x03\x00\x00\x00inpq;h8X\x02\x00\x00\x00ipq<h9h\x07}q=(h;K\x00N\x86q>h<K\x01N\x86q?uubub.')
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
