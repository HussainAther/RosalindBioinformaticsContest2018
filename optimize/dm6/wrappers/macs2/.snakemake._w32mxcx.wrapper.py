
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00paramsq\tcsnakemake.io\nParams\nq\n)\x81q\x0bX \x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1q\x0ca}q\r(X\x06\x00\x00\x00prefixq\x0eh\x0ch\x07}q\x0fh\x0eK\x00N\x86q\x10subX\x04\x00\x00\x00ruleq\x11X\x05\x00\x00\x00macs2q\x12X\t\x00\x00\x00resourcesq\x13csnakemake.io\nResources\nq\x14)\x81q\x15(K\x01K\x01e}q\x16(X\x06\x00\x00\x00_coresq\x17K\x01X\x06\x00\x00\x00_nodesq\x18K\x01h\x07}q\x19(h\x18K\x00N\x86q\x1ah\x17K\x01N\x86q\x1buubX\x07\x00\x00\x00threadsq\x1cK\x01X\x05\x00\x00\x00inputq\x1dcsnakemake.io\nInputFiles\nq\x1e)\x81q\x1f(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq X\x1b\x00\x00\x00dedup/sjl_mbn2_cp190_R1.bamq!e}q"(X\x03\x00\x00\x00inpq#h X\x02\x00\x00\x00ipq$h!h\x07}q%(h#K\x00N\x86q&h$K\x01N\x86q\'uubX\x06\x00\x00\x00configq(}q)X\x06\x00\x00\x00outputq*csnakemake.io\nOutputFiles\nq+)\x81q,(X6\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1.bedq-XC\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1_peaks.narrowPeakq.e}q/(X\x03\x00\x00\x00bedq0h-X\n\x00\x00\x00narrowPeakq1h.h\x07}q2(h0K\x00N\x86q3h1K\x01N\x86q4uubX\t\x00\x00\x00wildcardsq5csnakemake.io\nWildcards\nq6)\x81q7X\x11\x00\x00\x00sjl_mbn2_cp190_R1q8a}q9(X\x06\x00\x00\x00sampleq:h8h\x07}q;X\x06\x00\x00\x00sampleq<K\x00N\x86q=subub.')
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
