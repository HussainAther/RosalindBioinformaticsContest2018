
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x19\x00\x00\x00dedup/sjl_s2_input_R1.bamq\x06X\x17\x00\x00\x00dedup/sjl_s2_mod_R1.bamq\x07e}q\x08(X\x03\x00\x00\x00inpq\th\x06X\x02\x00\x00\x00ipq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11(X\x1c\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1q\x12X\r\x00\x00\x00sjl_s2_mod_R1q\x13e}q\x14(X\x06\x00\x00\x00prefixq\x15h\x12X\x0e\x00\x00\x00wrapper_sampleq\x16h\x13h\x0b}q\x17(h\x15K\x00N\x86q\x18h\x16K\x01N\x86q\x19uubX\t\x00\x00\x00resourcesq\x1acsnakemake.io\nResources\nq\x1b)\x81q\x1c(K\x01K\x01e}q\x1d(X\x06\x00\x00\x00_coresq\x1eK\x01X\x06\x00\x00\x00_nodesq\x1fK\x01h\x0b}q (h\x1eK\x00N\x86q!h\x1fK\x01N\x86q"uubX\x04\x00\x00\x00ruleq#X\x05\x00\x00\x00macs2q$X\t\x00\x00\x00wildcardsq%csnakemake.io\nWildcards\nq&)\x81q\'h\x13a}q((X\x06\x00\x00\x00sampleq)h\x13h\x0b}q*X\x06\x00\x00\x00sampleq+K\x00N\x86q,subX\x06\x00\x00\x00configq-}q.X\x03\x00\x00\x00logq/csnakemake.io\nLog\nq0)\x81q1}q2h\x0b}q3sbX\x07\x00\x00\x00threadsq4K\x01X\x06\x00\x00\x00outputq5csnakemake.io\nOutputFiles\nq6)\x81q7(X;\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1_peaks.narrowPeakq8X.\x00\x00\x00peak_out/macs2/sjl_s2_mod_R1/sjl_s2_mod_R1.bedq9e}q:(X\n\x00\x00\x00narrowPeakq;h8X\x03\x00\x00\x00bedq<h9h\x0b}q=(h;K\x00N\x86q>h<K\x01N\x86q?uubub.')
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
#shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
