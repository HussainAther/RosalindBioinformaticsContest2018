
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x06\x00\x00\x00outputq\x05csnakemake.io\nOutputFiles\nq\x06)\x81q\x07(X2\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1/sjl_cl8_suhw_R1.bedq\x08X?\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1/sjl_cl8_suhw_R1_peaks.narrowPeakq\te}q\n(X\n\x00\x00\x00narrowPeakq\x0bh\tX\x06\x00\x00\x00_namesq\x0c}q\r(h\x0bK\x01N\x86q\x0eX\x03\x00\x00\x00bedq\x0fK\x00N\x86q\x10uh\x0fh\x08ubX\t\x00\x00\x00wildcardsq\x11csnakemake.io\nWildcards\nq\x12)\x81q\x13X\x0f\x00\x00\x00sjl_cl8_suhw_R1q\x14a}q\x15(X\x06\x00\x00\x00sampleq\x16h\x14h\x0c}q\x17X\x06\x00\x00\x00sampleq\x18K\x00N\x86q\x19subX\x05\x00\x00\x00inputq\x1acsnakemake.io\nInputFiles\nq\x1b)\x81q\x1c(X\x19\x00\x00\x00dedup/sjl_cl8_suhw_R1.bamq\x1dX\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq\x1ee}q\x1f(h\x0c}q (X\x02\x00\x00\x00ipq!K\x00N\x86q"X\x03\x00\x00\x00inpq#K\x01N\x86q$uh!h\x1dh#h\x1eubX\x03\x00\x00\x00logq%csnakemake.io\nLog\nq&)\x81q\'}q(h\x0c}q)sbX\t\x00\x00\x00resourcesq*csnakemake.io\nResources\nq+)\x81q,(K\x01K\x01e}q-(X\x06\x00\x00\x00_nodesq.K\x01X\x06\x00\x00\x00_coresq/K\x01h\x0c}q0(h/K\x00N\x86q1h.K\x01N\x86q2uubX\x07\x00\x00\x00threadsq3K\x01X\x06\x00\x00\x00paramsq4csnakemake.io\nParams\nq5)\x81q6(X\x1e\x00\x00\x00peak_out/macs2/sjl_cl8_suhw_R1q7h\x14e}q8(X\x06\x00\x00\x00prefixq9h7X\x0e\x00\x00\x00wrapper_sampleq:h\x14h\x0c}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubX\x04\x00\x00\x00ruleq>X\x05\x00\x00\x00macs2q?ub.')
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
