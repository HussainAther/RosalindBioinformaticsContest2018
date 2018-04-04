
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x0e\x00\x00\x00sjl_kc_shep_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00sampleq\nK\x00N\x86q\x0bsX\x06\x00\x00\x00sampleq\x0ch\x06ubX\x06\x00\x00\x00outputq\rcsnakemake.io\nOutputFiles\nq\x0e)\x81q\x0f(X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq\x10X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq\x11e}q\x12(h\x08}q\x13(X\n\x00\x00\x00narrowPeakq\x14K\x00N\x86q\x15X\x03\x00\x00\x00bedq\x16K\x01N\x86q\x17uh\x14h\x10h\x16h\x11ubX\t\x00\x00\x00resourcesq\x18csnakemake.io\nResources\nq\x19)\x81q\x1a(K\x01K\x01e}q\x1b(X\x06\x00\x00\x00_coresq\x1cK\x01h\x08}q\x1d(h\x1cK\x00N\x86q\x1eX\x06\x00\x00\x00_nodesq\x1fK\x01N\x86q uh\x1fK\x01ubX\x03\x00\x00\x00logq!csnakemake.io\nLog\nq")\x81q#}q$h\x08}q%sbX\x05\x00\x00\x00inputq&csnakemake.io\nInputFiles\nq\')\x81q((X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq)X\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq*e}q+(X\x03\x00\x00\x00inpq,h)h\x08}q-(h,K\x00N\x86q.X\x02\x00\x00\x00ipq/K\x01N\x86q0uh/h*ubX\x06\x00\x00\x00configq1}q2X\x07\x00\x00\x00threadsq3K\x01X\x04\x00\x00\x00ruleq4X\x05\x00\x00\x00macs2q5X\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q9a}q:(X\x06\x00\x00\x00prefixq;h9h\x08}q<h;K\x00N\x86q=subub.')
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
shell('touch {snakemake.output.bed}')
shell('Rscript peak_out/macs2/{snakemake.params.prefix}_model.r')
