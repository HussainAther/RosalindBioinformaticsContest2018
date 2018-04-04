
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00paramsq\tcsnakemake.io\nParams\nq\n)\x81q\x0b(X\x15\x00\x00\x00el41_bg3_rump-10c3_R1q\x0cX$\x00\x00\x00peak_out/macs2/el41_bg3_rump-10c3_R1q\re}q\x0e(h\x07}q\x0f(X\x0e\x00\x00\x00wrapper_sampleq\x10K\x00N\x86q\x11X\x06\x00\x00\x00prefixq\x12K\x01N\x86q\x13uh\x12h\rh\x10h\x0cubX\t\x00\x00\x00wildcardsq\x14csnakemake.io\nWildcards\nq\x15)\x81q\x16h\x0ca}q\x17(h\x07}q\x18X\x06\x00\x00\x00sampleq\x19K\x00N\x86q\x1asX\x06\x00\x00\x00sampleq\x1bh\x0cubX\t\x00\x00\x00resourcesq\x1ccsnakemake.io\nResources\nq\x1d)\x81q\x1e(K\x01K\x01e}q\x1f(h\x07}q (X\x06\x00\x00\x00_nodesq!K\x00N\x86q"X\x06\x00\x00\x00_coresq#K\x01N\x86q$uh!K\x01h#K\x01ubX\x07\x00\x00\x00threadsq%K\x01X\x06\x00\x00\x00outputq&csnakemake.io\nOutputFiles\nq\')\x81q((XK\x00\x00\x00peak_out/macs2/el41_bg3_rump-10c3_R1/el41_bg3_rump-10c3_R1_peaks.narrowPeakq)X>\x00\x00\x00peak_out/macs2/el41_bg3_rump-10c3_R1/el41_bg3_rump-10c3_R1.bedq*e}q+(X\n\x00\x00\x00narrowPeakq,h)X\x03\x00\x00\x00bedq-h*h\x07}q.(h,K\x00N\x86q/h-K\x01N\x86q0uubX\x04\x00\x00\x00ruleq1X\x05\x00\x00\x00macs2q2X\x06\x00\x00\x00configq3}q4X\x05\x00\x00\x00inputq5csnakemake.io\nInputFiles\nq6)\x81q7(X\x1b\x00\x00\x00dedup/el37_bg3_input_R1.bamq8X\x1f\x00\x00\x00dedup/el41_bg3_rump-10c3_R1.bamq9e}q:(X\x03\x00\x00\x00inpq;h8X\x02\x00\x00\x00ipq<h9h\x07}q=(h;K\x00N\x86q>h<K\x01N\x86q?uubub.')
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
