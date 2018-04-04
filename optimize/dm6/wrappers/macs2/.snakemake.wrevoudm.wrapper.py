
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\t\x00\x00\x00resourcesq\x05csnakemake.io\nResources\nq\x06)\x81q\x07(K\x01K\x01e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x06\x00\x00\x00_nodesq\x0bK\x00N\x86q\x0cX\x06\x00\x00\x00_coresq\rK\x01N\x86q\x0euh\rK\x01h\x0bK\x01ubX\t\x00\x00\x00wildcardsq\x0fcsnakemake.io\nWildcards\nq\x10)\x81q\x11X\x0e\x00\x00\x00sjl_s3_shep_R1q\x12a}q\x13(h\t}q\x14X\x06\x00\x00\x00sampleq\x15K\x00N\x86q\x16sX\x06\x00\x00\x00sampleq\x17h\x12ubX\x05\x00\x00\x00inputq\x18csnakemake.io\nInputFiles\nq\x19)\x81q\x1a(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq\x1bX\x18\x00\x00\x00dedup/sjl_s3_shep_R1.bamq\x1ce}q\x1d(X\x02\x00\x00\x00ipq\x1eh\x1cX\x03\x00\x00\x00inpq\x1fh\x1bh\t}q (h\x1fK\x00N\x86q!h\x1eK\x01N\x86q"uubX\x07\x00\x00\x00threadsq#K\x01X\x06\x00\x00\x00paramsq$csnakemake.io\nParams\nq%)\x81q&X\x1d\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1q\'a}q((h\t}q)X\x06\x00\x00\x00prefixq*K\x00N\x86q+sh*h\'ubX\x06\x00\x00\x00outputq,csnakemake.io\nOutputFiles\nq-)\x81q.(X=\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1/sjl_s3_shep_R1_peaks.narrowPeakq/X0\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1/sjl_s3_shep_R1.bedq0e}q1(X\n\x00\x00\x00narrowPeakq2h/h\t}q3(h2K\x00N\x86q4X\x03\x00\x00\x00bedq5K\x01N\x86q6uh5h0ubX\x03\x00\x00\x00logq7csnakemake.io\nLog\nq8)\x81q9}q:h\t}q;sbX\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=ub.')
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
