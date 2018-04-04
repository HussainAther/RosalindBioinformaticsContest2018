
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05(X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1q\x06X\x10\x00\x00\x00sjl_mbn2_suhw_R1q\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x06\x00\x00\x00prefixq\x0bK\x00N\x86q\x0cX\x0e\x00\x00\x00wrapper_sampleq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x07\x00\x00\x00threadsq\x0fK\x01X\t\x00\x00\x00wildcardsq\x10csnakemake.io\nWildcards\nq\x11)\x81q\x12h\x07a}q\x13(h\t}q\x14X\x06\x00\x00\x00sampleq\x15K\x00N\x86q\x16sX\x06\x00\x00\x00sampleq\x17h\x07ubX\x06\x00\x00\x00outputq\x18csnakemake.io\nOutputFiles\nq\x19)\x81q\x1a(XA\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1_peaks.narrowPeakq\x1bX4\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1.bedq\x1ce}q\x1d(X\n\x00\x00\x00narrowPeakq\x1eh\x1bh\t}q\x1f(h\x1eK\x00N\x86q X\x03\x00\x00\x00bedq!K\x01N\x86q"uh!h\x1cubX\t\x00\x00\x00resourcesq#csnakemake.io\nResources\nq$)\x81q%(K\x01K\x01e}q&(h\t}q\'(X\x06\x00\x00\x00_nodesq(K\x00N\x86q)X\x06\x00\x00\x00_coresq*K\x01N\x86q+uh*K\x01h(K\x01ubX\x03\x00\x00\x00logq,csnakemake.io\nLog\nq-)\x81q.}q/h\t}q0sbX\x06\x00\x00\x00configq1}q2X\x05\x00\x00\x00inputq3csnakemake.io\nInputFiles\nq4)\x81q5(X\x1a\x00\x00\x00dedup/sjl_mbn2_suhw_R1.bamq6X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq7e}q8(X\x02\x00\x00\x00ipq9h6X\x03\x00\x00\x00inpq:h7h\t}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubX\x04\x00\x00\x00ruleq>X\x05\x00\x00\x00macs2q?ub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.r > {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.pdf')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
