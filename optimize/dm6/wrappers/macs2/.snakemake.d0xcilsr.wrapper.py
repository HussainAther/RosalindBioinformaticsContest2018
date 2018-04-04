
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x04\x00\x00\x00ruleq\tX\x05\x00\x00\x00macs2q\nX\x05\x00\x00\x00inputq\x0bcsnakemake.io\nInputFiles\nq\x0c)\x81q\r(X\x1a\x00\x00\x00dedup/sjl_mbn2_suhw_R1.bamq\x0eX\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x0fe}q\x10(X\x02\x00\x00\x00ipq\x11h\x0eh\x07}q\x12(h\x11K\x00N\x86q\x13X\x03\x00\x00\x00inpq\x14K\x01N\x86q\x15uh\x14h\x0fubX\x06\x00\x00\x00outputq\x16csnakemake.io\nOutputFiles\nq\x17)\x81q\x18(XA\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1_peaks.narrowPeakq\x19X4\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1.bedq\x1ae}q\x1b(h\x07}q\x1c(X\n\x00\x00\x00narrowPeakq\x1dK\x00N\x86q\x1eX\x03\x00\x00\x00bedq\x1fK\x01N\x86q uh\x1dh\x19h\x1fh\x1aubX\x06\x00\x00\x00configq!}q"X\x07\x00\x00\x00threadsq#K\x01X\t\x00\x00\x00resourcesq$csnakemake.io\nResources\nq%)\x81q&(K\x01K\x01e}q\'(X\x06\x00\x00\x00_coresq(K\x01h\x07}q)(h(K\x00N\x86q*X\x06\x00\x00\x00_nodesq+K\x01N\x86q,uh+K\x01ubX\t\x00\x00\x00wildcardsq-csnakemake.io\nWildcards\nq.)\x81q/X\x10\x00\x00\x00sjl_mbn2_suhw_R1q0a}q1(X\x06\x00\x00\x00sampleq2h0h\x07}q3X\x06\x00\x00\x00sampleq4K\x00N\x86q5subX\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8(h0X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1q9e}q:(X\x0e\x00\x00\x00wrapper_sampleq;h0h\x07}q<(h;K\x00N\x86q=X\x06\x00\x00\x00prefixq>K\x01N\x86q?uh>h9ubub.')
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
