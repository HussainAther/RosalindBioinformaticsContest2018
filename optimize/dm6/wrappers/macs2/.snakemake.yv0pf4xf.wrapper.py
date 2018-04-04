
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X=\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1/sjl_s3_shep_R1_peaks.narrowPeakq\x06X0\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1/sjl_s3_shep_R1.bedq\x07e}q\x08(X\n\x00\x00\x00narrowPeakq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\x03\x00\x00\x00bedq\rK\x01N\x86q\x0euh\rh\x07ubX\x04\x00\x00\x00ruleq\x0fX\x05\x00\x00\x00macs2q\x10X\x06\x00\x00\x00paramsq\x11csnakemake.io\nParams\nq\x12)\x81q\x13X\x1d\x00\x00\x00peak_out/macs2/sjl_s3_shep_R1q\x14a}q\x15(X\x06\x00\x00\x00prefixq\x16h\x14h\n}q\x17h\x16K\x00N\x86q\x18subX\x03\x00\x00\x00logq\x19csnakemake.io\nLog\nq\x1a)\x81q\x1b}q\x1ch\n}q\x1dsbX\x07\x00\x00\x00threadsq\x1eK\x01X\x06\x00\x00\x00configq\x1f}q X\t\x00\x00\x00wildcardsq!csnakemake.io\nWildcards\nq")\x81q#X\x0e\x00\x00\x00sjl_s3_shep_R1q$a}q%(X\x06\x00\x00\x00sampleq&h$h\n}q\'X\x06\x00\x00\x00sampleq(K\x00N\x86q)subX\t\x00\x00\x00resourcesq*csnakemake.io\nResources\nq+)\x81q,(K\x01K\x01e}q-(X\x06\x00\x00\x00_coresq.K\x01h\n}q/(h.K\x00N\x86q0X\x06\x00\x00\x00_nodesq1K\x01N\x86q2uh1K\x01ubX\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x18\x00\x00\x00dedup/sjl_s3_shep_R1.bamq6X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq7e}q8(X\x02\x00\x00\x00ipq9h6h\n}q:(h9K\x00N\x86q;X\x03\x00\x00\x00inpq<K\x01N\x86q=uh<h7ubub.')
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
