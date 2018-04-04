
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X6\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1.bedq\x06XC\x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1/sjl_mbn2_cp190_R1_peaks.narrowPeakq\x07e}q\x08(X\x03\x00\x00\x00bedq\th\x06X\n\x00\x00\x00narrowPeakq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x05\x00\x00\x00inputq\x0fcsnakemake.io\nInputFiles\nq\x10)\x81q\x11(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x12X\x1b\x00\x00\x00dedup/sjl_mbn2_cp190_R1.bamq\x13e}q\x14(X\x03\x00\x00\x00inpq\x15h\x12h\x0b}q\x16(h\x15K\x00N\x86q\x17X\x02\x00\x00\x00ipq\x18K\x01N\x86q\x19uh\x18h\x13ubX\t\x00\x00\x00resourcesq\x1acsnakemake.io\nResources\nq\x1b)\x81q\x1c(K\x01K\x01e}q\x1d(X\x06\x00\x00\x00_coresq\x1eK\x01h\x0b}q\x1f(h\x1eK\x00N\x86q X\x06\x00\x00\x00_nodesq!K\x01N\x86q"uh!K\x01ubX\x03\x00\x00\x00logq#csnakemake.io\nLog\nq$)\x81q%}q&h\x0b}q\'sbX\t\x00\x00\x00wildcardsq(csnakemake.io\nWildcards\nq))\x81q*X\x11\x00\x00\x00sjl_mbn2_cp190_R1q+a}q,(h\x0b}q-X\x06\x00\x00\x00sampleq.K\x00N\x86q/sX\x06\x00\x00\x00sampleq0h+ubX\x06\x00\x00\x00configq1}q2X\x06\x00\x00\x00paramsq3csnakemake.io\nParams\nq4)\x81q5X \x00\x00\x00peak_out/macs2/sjl_mbn2_cp190_R1q6a}q7(h\x0b}q8X\x06\x00\x00\x00prefixq9K\x00N\x86q:sh9h6ubX\x04\x00\x00\x00ruleq;X\x05\x00\x00\x00macs2q<X\x07\x00\x00\x00threadsq=K\x01ub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.wildcards.sample}_model.r')
#shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
shell("cd {snakemake.params.prefix} && ln -sf $(basename {snakemake.output.narrowPeak}) $(basename {snakemake.output.bed})")
