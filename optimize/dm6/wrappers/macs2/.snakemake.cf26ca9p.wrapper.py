
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\t\x00\x00\x00wildcardsq\tcsnakemake.io\nWildcards\nq\n)\x81q\x0bX\x0e\x00\x00\x00sjl_kc_shep_R1q\x0ca}q\r(X\x06\x00\x00\x00sampleq\x0eh\x0ch\x07}q\x0fX\x06\x00\x00\x00sampleq\x10K\x00N\x86q\x11subX\x06\x00\x00\x00outputq\x12csnakemake.io\nOutputFiles\nq\x13)\x81q\x14(X=\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1_peaks.narrowPeakq\x15X0\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1/sjl_kc_shep_R1.bedq\x16e}q\x17(h\x07}q\x18(X\n\x00\x00\x00narrowPeakq\x19K\x00N\x86q\x1aX\x03\x00\x00\x00bedq\x1bK\x01N\x86q\x1cuh\x1bh\x16h\x19h\x15ubX\x07\x00\x00\x00threadsq\x1dK\x01X\x06\x00\x00\x00configq\x1e}q\x1fX\x05\x00\x00\x00inputq csnakemake.io\nInputFiles\nq!)\x81q"(X\x18\x00\x00\x00dedup/sjl_kc_shep_R1.bamq#X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq$e}q%(h\x07}q&(X\x02\x00\x00\x00ipq\'K\x00N\x86q(X\x03\x00\x00\x00inpq)K\x01N\x86q*uh\'h#h)h$ubX\x04\x00\x00\x00ruleq+X\x05\x00\x00\x00macs2q,X\x06\x00\x00\x00paramsq-csnakemake.io\nParams\nq.)\x81q/X\x1d\x00\x00\x00peak_out/macs2/sjl_kc_shep_R1q0a}q1(h\x07}q2X\x06\x00\x00\x00prefixq3K\x00N\x86q4sh3h0ubX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_nodesq9K\x01h\x07}q:(h9K\x00N\x86q;X\x06\x00\x00\x00_coresq<K\x01N\x86q=uh<K\x01ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.input.ip}_model.r')
