
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00ruleq\x03X\x05\x00\x00\x00macs2q\x04X\x06\x00\x00\x00configq\x05}q\x06X\x06\x00\x00\x00outputq\x07csnakemake.io\nOutputFiles\nq\x08)\x81q\t(XA\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1_peaks.narrowPeakq\nX4\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1.bedq\x0be}q\x0c(X\n\x00\x00\x00narrowPeakq\rh\nX\x03\x00\x00\x00bedq\x0eh\x0bX\x06\x00\x00\x00_namesq\x0f}q\x10(h\rK\x00N\x86q\x11h\x0eK\x01N\x86q\x12uubX\x06\x00\x00\x00paramsq\x13csnakemake.io\nParams\nq\x14)\x81q\x15(X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1q\x16X\x10\x00\x00\x00sjl_mbn2_suhw_R1q\x17e}q\x18(X\x0e\x00\x00\x00wrapper_sampleq\x19h\x17X\x06\x00\x00\x00prefixq\x1ah\x16h\x0f}q\x1b(h\x1aK\x00N\x86q\x1ch\x19K\x01N\x86q\x1duubX\x03\x00\x00\x00logq\x1ecsnakemake.io\nLog\nq\x1f)\x81q }q!h\x0f}q"sbX\x07\x00\x00\x00threadsq#K\x01X\t\x00\x00\x00wildcardsq$csnakemake.io\nWildcards\nq%)\x81q&h\x17a}q\'(X\x06\x00\x00\x00sampleq(h\x17h\x0f}q)X\x06\x00\x00\x00sampleq*K\x00N\x86q+subX\x05\x00\x00\x00inputq,csnakemake.io\nInputFiles\nq-)\x81q.(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq/X\x1a\x00\x00\x00dedup/sjl_mbn2_suhw_R1.bamq0e}q1(X\x03\x00\x00\x00inpq2h/X\x02\x00\x00\x00ipq3h0h\x0f}q4(h2K\x00N\x86q5h3K\x01N\x86q6uubX\t\x00\x00\x00resourcesq7csnakemake.io\nResources\nq8)\x81q9(K\x01K\x01e}q:(X\x06\x00\x00\x00_coresq;K\x01X\x06\x00\x00\x00_nodesq<K\x01h\x0f}q=(h<K\x00N\x86q>h;K\x01N\x86q?uubub.')
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
