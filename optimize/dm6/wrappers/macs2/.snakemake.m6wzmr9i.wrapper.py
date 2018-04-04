
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X6\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1.bedq\x06XC\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1_peaks.narrowPeakq\x07e}q\x08(X\x03\x00\x00\x00bedq\th\x06X\x06\x00\x00\x00_namesq\n}q\x0b(h\tK\x00N\x86q\x0cX\n\x00\x00\x00narrowPeakq\rK\x01N\x86q\x0euh\rh\x07ubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11X \x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1q\x12a}q\x13(X\x06\x00\x00\x00prefixq\x14h\x12h\n}q\x15h\x14K\x00N\x86q\x16subX\t\x00\x00\x00resourcesq\x17csnakemake.io\nResources\nq\x18)\x81q\x19(K\x01K\x01e}q\x1a(X\x06\x00\x00\x00_coresq\x1bK\x01X\x06\x00\x00\x00_nodesq\x1cK\x01h\n}q\x1d(h\x1cK\x00N\x86q\x1eh\x1bK\x01N\x86q\x1fuubX\x03\x00\x00\x00logq csnakemake.io\nLog\nq!)\x81q"}q#h\n}q$sbX\x06\x00\x00\x00configq%}q&X\x04\x00\x00\x00ruleq\'X\x05\x00\x00\x00macs2q(X\x07\x00\x00\x00threadsq)K\x01X\x05\x00\x00\x00inputq*csnakemake.io\nInputFiles\nq+)\x81q,(X\x1b\x00\x00\x00dedup/sjl_mbn2_cp190_R1.bamq-X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq.e}q/(X\x02\x00\x00\x00ipq0h-X\x03\x00\x00\x00inpq1h.h\n}q2(h0K\x00N\x86q3h1K\x01N\x86q4uubX\t\x00\x00\x00wildcardsq5csnakemake.io\nWildcards\nq6)\x81q7X\x11\x00\x00\x00sjl_mbn2_cp190_R1q8a}q9(X\x06\x00\x00\x00sampleq:h8h\n}q;X\x06\x00\x00\x00sampleq<K\x00N\x86q=subub.')
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
