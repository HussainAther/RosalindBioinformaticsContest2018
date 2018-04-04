
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05X\x1f\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00prefixq\nK\x00N\x86q\x0bsh\nh\x06ubX\x05\x00\x00\x00inputq\x0ccsnakemake.io\nInputFiles\nq\r)\x81q\x0e(X\x1a\x00\x00\x00dedup/sjl_cl8_cp190_R1.bamq\x0fX\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x10e}q\x11(X\x02\x00\x00\x00ipq\x12h\x0fh\x08}q\x13(h\x12K\x00N\x86q\x14X\x03\x00\x00\x00inpq\x15K\x01N\x86q\x16uh\x15h\x10ubX\x04\x00\x00\x00ruleq\x17X\x05\x00\x00\x00macs2q\x18X\x06\x00\x00\x00configq\x19}q\x1aX\x06\x00\x00\x00outputq\x1bcsnakemake.io\nOutputFiles\nq\x1c)\x81q\x1d(X4\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1.bedq\x1eXA\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1_peaks.narrowPeakq\x1fe}q (X\n\x00\x00\x00narrowPeakq!h\x1fX\x03\x00\x00\x00bedq"h\x1eh\x08}q#(h!K\x01N\x86q$h"K\x00N\x86q%uubX\x07\x00\x00\x00threadsq&K\x01X\t\x00\x00\x00resourcesq\'csnakemake.io\nResources\nq()\x81q)(K\x01K\x01e}q*(X\x06\x00\x00\x00_coresq+K\x01h\x08}q,(X\x06\x00\x00\x00_nodesq-K\x00N\x86q.h+K\x01N\x86q/uh-K\x01ubX\x03\x00\x00\x00logq0csnakemake.io\nLog\nq1)\x81q2}q3h\x08}q4sbX\t\x00\x00\x00wildcardsq5csnakemake.io\nWildcards\nq6)\x81q7X\x10\x00\x00\x00sjl_cl8_cp190_R1q8a}q9(X\x06\x00\x00\x00sampleq:h8h\x08}q;X\x06\x00\x00\x00sampleq<K\x00N\x86q=subub.')
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
