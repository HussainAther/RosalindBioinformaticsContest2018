
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x03\x00\x00\x00logq\x04csnakemake.io\nLog\nq\x05)\x81q\x06}q\x07X\x06\x00\x00\x00_namesq\x08}q\tsbX\t\x00\x00\x00wildcardsq\ncsnakemake.io\nWildcards\nq\x0b)\x81q\x0cX\x0e\x00\x00\x00sjl_s3_suhw_R1q\ra}q\x0e(X\x06\x00\x00\x00sampleq\x0fh\rh\x08}q\x10X\x06\x00\x00\x00sampleq\x11K\x00N\x86q\x12subX\x06\x00\x00\x00paramsq\x13csnakemake.io\nParams\nq\x14)\x81q\x15X\x1d\x00\x00\x00peak_out/macs2/sjl_s3_suhw_R1q\x16a}q\x17(X\x06\x00\x00\x00prefixq\x18h\x16h\x08}q\x19h\x18K\x00N\x86q\x1asubX\t\x00\x00\x00resourcesq\x1bcsnakemake.io\nResources\nq\x1c)\x81q\x1d(K\x01K\x01e}q\x1e(X\x06\x00\x00\x00_nodesq\x1fK\x01h\x08}q (h\x1fK\x00N\x86q!X\x06\x00\x00\x00_coresq"K\x01N\x86q#uh"K\x01ubX\x06\x00\x00\x00configq$}q%X\x06\x00\x00\x00outputq&csnakemake.io\nOutputFiles\nq\')\x81q((X0\x00\x00\x00peak_out/macs2/sjl_s3_suhw_R1/sjl_s3_suhw_R1.bedq)X=\x00\x00\x00peak_out/macs2/sjl_s3_suhw_R1/sjl_s3_suhw_R1_peaks.narrowPeakq*e}q+(h\x08}q,(X\x03\x00\x00\x00bedq-K\x00N\x86q.X\n\x00\x00\x00narrowPeakq/K\x01N\x86q0uh-h)h/h*ubX\x04\x00\x00\x00ruleq1X\x05\x00\x00\x00macs2q2X\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq6X\x18\x00\x00\x00dedup/sjl_s3_suhw_R1.bamq7e}q8(X\x03\x00\x00\x00inpq9h6h\x08}q:(h9K\x00N\x86q;X\x02\x00\x00\x00ipq<K\x01N\x86q=uh<h7ubub.')
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
