
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00paramsq\tcsnakemake.io\nParams\nq\n)\x81q\x0bX\x1e\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1q\x0ca}q\r(X\x06\x00\x00\x00prefixq\x0eh\x0ch\x07}q\x0fh\x0eK\x00N\x86q\x10subX\x05\x00\x00\x00inputq\x11csnakemake.io\nInputFiles\nq\x12)\x81q\x13(X\x19\x00\x00\x00dedup/sjl_s2_cp190_R1.bamq\x14X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x15e}q\x16(X\x02\x00\x00\x00ipq\x17h\x14h\x07}q\x18(h\x17K\x00N\x86q\x19X\x03\x00\x00\x00inpq\x1aK\x01N\x86q\x1buh\x1ah\x15ubX\x04\x00\x00\x00ruleq\x1cX\x05\x00\x00\x00macs2q\x1dX\x07\x00\x00\x00threadsq\x1eK\x01X\t\x00\x00\x00wildcardsq\x1fcsnakemake.io\nWildcards\nq )\x81q!X\x0f\x00\x00\x00sjl_s2_cp190_R1q"a}q#(X\x06\x00\x00\x00sampleq$h"h\x07}q%X\x06\x00\x00\x00sampleq&K\x00N\x86q\'subX\x06\x00\x00\x00outputq(csnakemake.io\nOutputFiles\nq))\x81q*(X?\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1_peaks.narrowPeakq+X2\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1.bedq,e}q-(X\n\x00\x00\x00narrowPeakq.h+h\x07}q/(h.K\x00N\x86q0X\x03\x00\x00\x00bedq1K\x01N\x86q2uh1h,ubX\x06\x00\x00\x00configq3}q4X\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_coresq9K\x01X\x06\x00\x00\x00_nodesq:K\x01h\x07}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubub.')
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
