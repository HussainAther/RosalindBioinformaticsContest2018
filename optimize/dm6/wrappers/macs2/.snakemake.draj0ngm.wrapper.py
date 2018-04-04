
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_namesq\x07}q\x08(X\x06\x00\x00\x00_coresq\tK\x00N\x86q\nX\x06\x00\x00\x00_nodesq\x0bK\x01N\x86q\x0cuh\tK\x01h\x0bK\x01ubX\x06\x00\x00\x00paramsq\rcsnakemake.io\nParams\nq\x0e)\x81q\x0f(X\x1e\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1q\x10X\x0f\x00\x00\x00sjl_s2_cp190_R1q\x11e}q\x12(h\x07}q\x13(X\x06\x00\x00\x00prefixq\x14K\x00N\x86q\x15X\x0e\x00\x00\x00wrapper_sampleq\x16K\x01N\x86q\x17uh\x14h\x10h\x16h\x11ubX\x06\x00\x00\x00outputq\x18csnakemake.io\nOutputFiles\nq\x19)\x81q\x1a(X2\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1.bedq\x1bX?\x00\x00\x00peak_out/macs2/sjl_s2_cp190_R1/sjl_s2_cp190_R1_peaks.narrowPeakq\x1ce}q\x1d(X\x03\x00\x00\x00bedq\x1eh\x1bh\x07}q\x1f(h\x1eK\x00N\x86q X\n\x00\x00\x00narrowPeakq!K\x01N\x86q"uh!h\x1cubX\x04\x00\x00\x00ruleq#X\x05\x00\x00\x00macs2q$X\x05\x00\x00\x00inputq%csnakemake.io\nInputFiles\nq&)\x81q\'(X\x19\x00\x00\x00dedup/sjl_s2_cp190_R1.bamq(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq)e}q*(h\x07}q+(X\x02\x00\x00\x00ipq,K\x00N\x86q-X\x03\x00\x00\x00inpq.K\x01N\x86q/uh,h(h.h)ubX\x07\x00\x00\x00threadsq0K\x01X\x06\x00\x00\x00configq1}q2X\t\x00\x00\x00wildcardsq3csnakemake.io\nWildcards\nq4)\x81q5h\x11a}q6(h\x07}q7X\x06\x00\x00\x00sampleq8K\x00N\x86q9sX\x06\x00\x00\x00sampleq:h\x11ubX\x03\x00\x00\x00logq;csnakemake.io\nLog\nq<)\x81q=}q>h\x07}q?sbub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.r')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
