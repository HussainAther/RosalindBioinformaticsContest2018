
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\t\x00\x00\x00resourcesq\tcsnakemake.io\nResources\nq\n)\x81q\x0b(K\x01K\x01e}q\x0c(X\x06\x00\x00\x00_nodesq\rK\x01h\x07}q\x0e(h\rK\x00N\x86q\x0fX\x06\x00\x00\x00_coresq\x10K\x01N\x86q\x11uh\x10K\x01ubX\x05\x00\x00\x00inputq\x12csnakemake.io\nInputFiles\nq\x13)\x81q\x14(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x15X\x19\x00\x00\x00dedup/sjl_mbn2_mod_R1.bamq\x16e}q\x17(X\x03\x00\x00\x00inpq\x18h\x15h\x07}q\x19(h\x18K\x00N\x86q\x1aX\x02\x00\x00\x00ipq\x1bK\x01N\x86q\x1cuh\x1bh\x16ubX\x06\x00\x00\x00configq\x1d}q\x1eX\x07\x00\x00\x00threadsq\x1fK\x01X\x06\x00\x00\x00outputq csnakemake.io\nOutputFiles\nq!)\x81q"(X?\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1_peaks.narrowPeakq#X2\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1/sjl_mbn2_mod_R1.bedq$e}q%(h\x07}q&(X\n\x00\x00\x00narrowPeakq\'K\x00N\x86q(X\x03\x00\x00\x00bedq)K\x01N\x86q*uh)h$h\'h#ubX\x04\x00\x00\x00ruleq+X\x05\x00\x00\x00macs2q,X\t\x00\x00\x00wildcardsq-csnakemake.io\nWildcards\nq.)\x81q/X\x0f\x00\x00\x00sjl_mbn2_mod_R1q0a}q1(X\x06\x00\x00\x00sampleq2h0h\x07}q3X\x06\x00\x00\x00sampleq4K\x00N\x86q5subX\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8(X\x1e\x00\x00\x00peak_out/macs2/sjl_mbn2_mod_R1q9h0e}q:(X\x06\x00\x00\x00prefixq;h9h\x07}q<(h;K\x00N\x86q=X\x0e\x00\x00\x00wrapper_sampleq>K\x01N\x86q?uh>h0ubub.')
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
