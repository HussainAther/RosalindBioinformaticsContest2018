
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00configq\t}q\nX\x04\x00\x00\x00ruleq\x0bX\x05\x00\x00\x00macs2q\x0cX\x06\x00\x00\x00paramsq\rcsnakemake.io\nParams\nq\x0e)\x81q\x0fX\x1d\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1q\x10a}q\x11(h\x07}q\x12X\x06\x00\x00\x00prefixq\x13K\x00N\x86q\x14sh\x13h\x10ubX\x06\x00\x00\x00outputq\x15csnakemake.io\nOutputFiles\nq\x16)\x81q\x17(X=\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1/sjl_cl8_mod_R1_peaks.narrowPeakq\x18X0\x00\x00\x00peak_out/macs2/sjl_cl8_mod_R1/sjl_cl8_mod_R1.bedq\x19e}q\x1a(h\x07}q\x1b(X\n\x00\x00\x00narrowPeakq\x1cK\x00N\x86q\x1dX\x03\x00\x00\x00bedq\x1eK\x01N\x86q\x1fuh\x1eh\x19h\x1ch\x18ubX\x07\x00\x00\x00threadsq K\x01X\t\x00\x00\x00wildcardsq!csnakemake.io\nWildcards\nq")\x81q#X\x0e\x00\x00\x00sjl_cl8_mod_R1q$a}q%(h\x07}q&X\x06\x00\x00\x00sampleq\'K\x00N\x86q(sX\x06\x00\x00\x00sampleq)h$ubX\x05\x00\x00\x00inputq*csnakemake.io\nInputFiles\nq+)\x81q,(X\x18\x00\x00\x00dedup/sjl_cl8_mod_R1.bamq-X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq.e}q/(X\x02\x00\x00\x00ipq0h-X\x03\x00\x00\x00inpq1h.h\x07}q2(h0K\x00N\x86q3h1K\x01N\x86q4uubX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_coresq9K\x01h\x07}q:(h9K\x00N\x86q;X\x06\x00\x00\x00_nodesq<K\x01N\x86q=uh<K\x01ubub.')
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
