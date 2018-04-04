
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_coresq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x07K\x00N\x86q\x0bh\x08K\x01N\x86q\x0cuubX\x05\x00\x00\x00inputq\rcsnakemake.io\nInputFiles\nq\x0e)\x81q\x0f(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq\x10X\x17\x00\x00\x00dedup/sjl_s3_mod_R1.bamq\x11e}q\x12(h\t}q\x13(X\x03\x00\x00\x00inpq\x14K\x00N\x86q\x15X\x02\x00\x00\x00ipq\x16K\x01N\x86q\x17uh\x14h\x10h\x16h\x11ubX\x03\x00\x00\x00logq\x18csnakemake.io\nLog\nq\x19)\x81q\x1a}q\x1bh\t}q\x1csbX\x06\x00\x00\x00configq\x1d}q\x1eX\x06\x00\x00\x00paramsq\x1fcsnakemake.io\nParams\nq )\x81q!(X\x1c\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1q"X\r\x00\x00\x00sjl_s3_mod_R1q#e}q$(X\x0e\x00\x00\x00wrapper_sampleq%h#h\t}q&(X\x06\x00\x00\x00prefixq\'K\x00N\x86q(h%K\x01N\x86q)uh\'h"ubX\x06\x00\x00\x00outputq*csnakemake.io\nOutputFiles\nq+)\x81q,(X;\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1/sjl_s3_mod_R1_peaks.narrowPeakq-X.\x00\x00\x00peak_out/macs2/sjl_s3_mod_R1/sjl_s3_mod_R1.bedq.e}q/(h\t}q0(X\n\x00\x00\x00narrowPeakq1K\x00N\x86q2X\x03\x00\x00\x00bedq3K\x01N\x86q4uh1h-h3h.ubX\x04\x00\x00\x00ruleq5X\x05\x00\x00\x00macs2q6X\t\x00\x00\x00wildcardsq7csnakemake.io\nWildcards\nq8)\x81q9h#a}q:(h\t}q;X\x06\x00\x00\x00sampleq<K\x00N\x86q=sX\x06\x00\x00\x00sampleq>h#ubX\x07\x00\x00\x00threadsq?K\x01ub.')
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
