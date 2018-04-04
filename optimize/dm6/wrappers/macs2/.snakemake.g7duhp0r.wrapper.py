
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\t\x00\x00\x00resourcesq\tcsnakemake.io\nResources\nq\n)\x81q\x0b(K\x01K\x01e}q\x0c(X\x06\x00\x00\x00_coresq\rK\x01X\x06\x00\x00\x00_nodesq\x0eK\x01h\x07}q\x0f(h\x0eK\x00N\x86q\x10h\rK\x01N\x86q\x11uubX\x05\x00\x00\x00inputq\x12csnakemake.io\nInputFiles\nq\x13)\x81q\x14(X\x1d\x00\x00\x00dedup/el40_kc_rump-5g4_R1.bamq\x15X\x1a\x00\x00\x00dedup/el38_kc_input_R1.bamq\x16e}q\x17(X\x02\x00\x00\x00ipq\x18h\x15h\x07}q\x19(h\x18K\x00N\x86q\x1aX\x03\x00\x00\x00inpq\x1bK\x01N\x86q\x1cuh\x1bh\x16ubX\x06\x00\x00\x00configq\x1d}q\x1eX\x07\x00\x00\x00threadsq\x1fK\x01X\x06\x00\x00\x00outputq csnakemake.io\nOutputFiles\nq!)\x81q"(X:\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1/el40_kc_rump-5g4_R1.bedq#XG\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1/el40_kc_rump-5g4_R1_peaks.narrowPeakq$e}q%(h\x07}q&(X\x03\x00\x00\x00bedq\'K\x00N\x86q(X\n\x00\x00\x00narrowPeakq)K\x01N\x86q*uh\'h#h)h$ubX\x04\x00\x00\x00ruleq+X\x05\x00\x00\x00macs2q,X\t\x00\x00\x00wildcardsq-csnakemake.io\nWildcards\nq.)\x81q/X\x13\x00\x00\x00el40_kc_rump-5g4_R1q0a}q1(X\x06\x00\x00\x00sampleq2h0h\x07}q3X\x06\x00\x00\x00sampleq4K\x00N\x86q5subX\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X"\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1q9a}q:(X\x06\x00\x00\x00prefixq;h9h\x07}q<h;K\x00N\x86q=subub.')
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
