
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_coresq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x07K\x00N\x86q\x0bh\x08K\x01N\x86q\x0cuubX\x04\x00\x00\x00ruleq\rX\x05\x00\x00\x00macs2q\x0eX\t\x00\x00\x00wildcardsq\x0fcsnakemake.io\nWildcards\nq\x10)\x81q\x11X\x0f\x00\x00\x00sjl_mbn2_mod_R1q\x12a}q\x13(X\x06\x00\x00\x00sampleq\x14h\x12h\t}q\x15X\x06\x00\x00\x00sampleq\x16K\x00N\x86q\x17subX\x05\x00\x00\x00inputq\x18csnakemake.io\nInputFiles\nq\x19)\x81q\x1a(X\x19\x00\x00\x00dedup/sjl_mbn2_mod_R1.bamq\x1bX\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x1ce}q\x1d(X\x02\x00\x00\x00ipq\x1eh\x1bh\t}q\x1f(h\x1eK\x00N\x86q X\x03\x00\x00\x00inpq!K\x01N\x86q"uh!h\x1cubX\x03\x00\x00\x00logq#csnakemake.io\nLog\nq$)\x81q%}q&h\t}q\'sbX\x06\x00\x00\x00configq(}q)X\x07\x00\x00\x00threadsq*K\x01X\x06\x00\x00\x00paramsq+csnakemake.io\nParams\nq,)\x81q-X\x1e\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1q.a}q/(X\x06\x00\x00\x00prefixq0h.h\t}q1h0K\x00N\x86q2subX\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X?\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1_peaks.narrowPeakq6X2\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1.bedq7e}q8(X\n\x00\x00\x00narrowPeakq9h6X\x03\x00\x00\x00bedq:h7h\t}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubub.')
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
shell('Rscript {snakemake.params.prefix}_model.r')
