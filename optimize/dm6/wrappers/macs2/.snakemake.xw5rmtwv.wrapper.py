
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x04\x00\x00\x00ruleq\tX\x05\x00\x00\x00macs2q\nX\x06\x00\x00\x00paramsq\x0bcsnakemake.io\nParams\nq\x0c)\x81q\r(X\x1f\x00\x00\x00peak_out/macs2/lm33_bg3_suhw_R1q\x0eX\x10\x00\x00\x00lm33_bg3_suhw_R1q\x0fe}q\x10(h\x07}q\x11(X\x06\x00\x00\x00prefixq\x12K\x00N\x86q\x13X\x0e\x00\x00\x00wrapper_sampleq\x14K\x01N\x86q\x15uh\x12h\x0eh\x14h\x0fubX\x05\x00\x00\x00inputq\x16csnakemake.io\nInputFiles\nq\x17)\x81q\x18(X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq\x19X\x1a\x00\x00\x00dedup/lm33_bg3_suhw_R1.bamq\x1ae}q\x1b(h\x07}q\x1c(X\x03\x00\x00\x00inpq\x1dK\x00N\x86q\x1eX\x02\x00\x00\x00ipq\x1fK\x01N\x86q uh\x1dh\x19h\x1fh\x1aubX\t\x00\x00\x00resourcesq!csnakemake.io\nResources\nq")\x81q#(K\x01K\x01e}q$(h\x07}q%(X\x06\x00\x00\x00_coresq&K\x00N\x86q\'X\x06\x00\x00\x00_nodesq(K\x01N\x86q)uh&K\x01h(K\x01ubX\t\x00\x00\x00wildcardsq*csnakemake.io\nWildcards\nq+)\x81q,h\x0fa}q-(h\x07}q.X\x06\x00\x00\x00sampleq/K\x00N\x86q0sX\x06\x00\x00\x00sampleq1h\x0fubX\x07\x00\x00\x00threadsq2K\x01X\x06\x00\x00\x00configq3}q4X\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(X4\x00\x00\x00peak_out/macs2/lm33_bg3_suhw_R1/lm33_bg3_suhw_R1.bedq8XA\x00\x00\x00peak_out/macs2/lm33_bg3_suhw_R1/lm33_bg3_suhw_R1_peaks.narrowPeakq9e}q:(h\x07}q;(X\x03\x00\x00\x00bedq<K\x00N\x86q=X\n\x00\x00\x00narrowPeakq>K\x01N\x86q?uh<h8h>h9ubub.')
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
