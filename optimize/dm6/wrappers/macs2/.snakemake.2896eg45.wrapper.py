
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_coresq\x07K\x01X\x06\x00\x00\x00_nodesq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x07K\x00N\x86q\x0bh\x08K\x01N\x86q\x0cuubX\x05\x00\x00\x00inputq\rcsnakemake.io\nInputFiles\nq\x0e)\x81q\x0f(X\x18\x00\x00\x00dedup/sjl_s2_shep_R1.bamq\x10X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x11e}q\x12(X\x02\x00\x00\x00ipq\x13h\x10X\x03\x00\x00\x00inpq\x14h\x11h\t}q\x15(h\x13K\x00N\x86q\x16h\x14K\x01N\x86q\x17uubX\x07\x00\x00\x00threadsq\x18K\x01X\t\x00\x00\x00wildcardsq\x19csnakemake.io\nWildcards\nq\x1a)\x81q\x1bX\x0e\x00\x00\x00sjl_s2_shep_R1q\x1ca}q\x1d(X\x06\x00\x00\x00sampleq\x1eh\x1ch\t}q\x1fX\x06\x00\x00\x00sampleq K\x00N\x86q!subX\x06\x00\x00\x00configq"}q#X\x04\x00\x00\x00ruleq$X\x05\x00\x00\x00macs2q%X\x06\x00\x00\x00paramsq&csnakemake.io\nParams\nq\')\x81q(X\x1d\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1q)a}q*(X\x06\x00\x00\x00prefixq+h)h\t}q,h+K\x00N\x86q-subX\x06\x00\x00\x00outputq.csnakemake.io\nOutputFiles\nq/)\x81q0(X0\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1.bedq1X=\x00\x00\x00peak_out/macs2/sjl_s2_shep_R1/sjl_s2_shep_R1_peaks.narrowPeakq2e}q3(X\x03\x00\x00\x00bedq4h1X\n\x00\x00\x00narrowPeakq5h2h\t}q6(h4K\x00N\x86q7h5K\x01N\x86q8uubX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\t}q=sbub.')
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
