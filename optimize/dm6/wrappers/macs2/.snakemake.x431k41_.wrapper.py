
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00paramsq\x04csnakemake.io\nParams\nq\x05)\x81q\x06X\x1e\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1q\x07a}q\x08(X\x06\x00\x00\x00prefixq\th\x07X\x06\x00\x00\x00_namesq\n}q\x0bh\tK\x00N\x86q\x0csubX\x06\x00\x00\x00outputq\rcsnakemake.io\nOutputFiles\nq\x0e)\x81q\x0f(X2\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1.bedq\x10X?\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1_peaks.narrowPeakq\x11e}q\x12(X\x03\x00\x00\x00bedq\x13h\x10h\n}q\x14(h\x13K\x00N\x86q\x15X\n\x00\x00\x00narrowPeakq\x16K\x01N\x86q\x17uh\x16h\x11ubX\t\x00\x00\x00resourcesq\x18csnakemake.io\nResources\nq\x19)\x81q\x1a(K\x01K\x01e}q\x1b(X\x06\x00\x00\x00_coresq\x1cK\x01X\x06\x00\x00\x00_nodesq\x1dK\x01h\n}q\x1e(h\x1cK\x00N\x86q\x1fh\x1dK\x01N\x86q uubX\x03\x00\x00\x00logq!csnakemake.io\nLog\nq")\x81q#}q$h\n}q%sbX\x05\x00\x00\x00inputq&csnakemake.io\nInputFiles\nq\')\x81q((X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq)X\x19\x00\x00\x00dedup/sjl_s2_cp190_R1.bamq*e}q+(X\x03\x00\x00\x00inpq,h)h\n}q-(h,K\x00N\x86q.X\x02\x00\x00\x00ipq/K\x01N\x86q0uh/h*ubX\x04\x00\x00\x00ruleq1X\x05\x00\x00\x00macs2q2X\t\x00\x00\x00wildcardsq3csnakemake.io\nWildcards\nq4)\x81q5X\x0f\x00\x00\x00sjl_s2_cp190_R1q6a}q7(X\x06\x00\x00\x00sampleq8h6h\n}q9X\x06\x00\x00\x00sampleq:K\x00N\x86q;subX\x06\x00\x00\x00configq<}q=ub.')
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
