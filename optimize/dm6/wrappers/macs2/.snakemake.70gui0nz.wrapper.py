
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x1a\x00\x00\x00dedup/sjl_mbn2_shep_R1.bamq\x06X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x07e}q\x08(X\x02\x00\x00\x00ipq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\rh\x07ubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11(X\x10\x00\x00\x00sjl_mbn2_shep_R1q\x12X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1q\x13e}q\x14(X\x0e\x00\x00\x00wrapper_sampleq\x15h\x12X\x06\x00\x00\x00prefixq\x16h\x13h\n}q\x17(h\x15K\x00N\x86q\x18h\x16K\x01N\x86q\x19uubX\x04\x00\x00\x00ruleq\x1aX\x05\x00\x00\x00macs2q\x1bX\x07\x00\x00\x00threadsq\x1cK\x01X\x06\x00\x00\x00outputq\x1dcsnakemake.io\nOutputFiles\nq\x1e)\x81q\x1f(X4\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1.bedq XA\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1_peaks.narrowPeakq!e}q"(X\x03\x00\x00\x00bedq#h h\n}q$(h#K\x00N\x86q%X\n\x00\x00\x00narrowPeakq&K\x01N\x86q\'uh&h!ubX\x06\x00\x00\x00configq(}q)X\x03\x00\x00\x00logq*csnakemake.io\nLog\nq+)\x81q,}q-h\n}q.sbX\t\x00\x00\x00wildcardsq/csnakemake.io\nWildcards\nq0)\x81q1h\x12a}q2(X\x06\x00\x00\x00sampleq3h\x12h\n}q4X\x06\x00\x00\x00sampleq5K\x00N\x86q6subX\t\x00\x00\x00resourcesq7csnakemake.io\nResources\nq8)\x81q9(K\x01K\x01e}q:(X\x06\x00\x00\x00_nodesq;K\x01X\x06\x00\x00\x00_coresq<K\x01h\n}q=(h;K\x00N\x86q>h<K\x01N\x86q?uubub.')
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
