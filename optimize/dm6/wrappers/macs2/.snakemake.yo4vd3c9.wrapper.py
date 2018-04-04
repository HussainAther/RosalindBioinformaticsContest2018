
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_coresq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x08K\x00N\x86q\x0bh\x07K\x01N\x86q\x0cuubX\t\x00\x00\x00wildcardsq\rcsnakemake.io\nWildcards\nq\x0e)\x81q\x0fX\x0f\x00\x00\x00sjl_s2_cp190_R1q\x10a}q\x11(X\x06\x00\x00\x00sampleq\x12h\x10h\t}q\x13X\x06\x00\x00\x00sampleq\x14K\x00N\x86q\x15subX\x05\x00\x00\x00inputq\x16csnakemake.io\nInputFiles\nq\x17)\x81q\x18(X\x19\x00\x00\x00dedup/sjl_s2_cp190_R1.bamq\x19X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x1ae}q\x1b(X\x03\x00\x00\x00inpq\x1ch\x1aX\x02\x00\x00\x00ipq\x1dh\x19h\t}q\x1e(h\x1dK\x00N\x86q\x1fh\x1cK\x01N\x86q uubX\x06\x00\x00\x00paramsq!csnakemake.io\nParams\nq")\x81q#(h\x10X\x1e\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1q$e}q%(X\x0e\x00\x00\x00wrapper_sampleq&h\x10X\x06\x00\x00\x00prefixq\'h$h\t}q((h&K\x00N\x86q)h\'K\x01N\x86q*uubX\x07\x00\x00\x00threadsq+K\x01X\x06\x00\x00\x00outputq,csnakemake.io\nOutputFiles\nq-)\x81q.(X2\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1.bedq/X?\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1_peaks.narrowPeakq0e}q1(X\n\x00\x00\x00narrowPeakq2h0X\x03\x00\x00\x00bedq3h/h\t}q4(h3K\x00N\x86q5h2K\x01N\x86q6uubX\x03\x00\x00\x00logq7csnakemake.io\nLog\nq8)\x81q9}q:h\t}q;sbX\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=X\x06\x00\x00\x00configq>}q?ub.')
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
