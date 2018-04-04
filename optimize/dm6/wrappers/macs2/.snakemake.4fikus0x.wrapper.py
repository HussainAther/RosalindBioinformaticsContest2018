
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(XI\x00\x00\x00peak_out/macs2/el42_kc_rump-10c3_R1/el42_kc_rump-10c3_R1_peaks.narrowPeakq\x06X<\x00\x00\x00peak_out/macs2/el42_kc_rump-10c3_R1/el42_kc_rump-10c3_R1.bedq\x07e}q\x08(X\n\x00\x00\x00narrowPeakq\th\x06X\x03\x00\x00\x00bedq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11X#\x00\x00\x00peak_out/macs2/el42_kc_rump-10c3_R1q\x12a}q\x13(h\x0b}q\x14X\x06\x00\x00\x00prefixq\x15K\x00N\x86q\x16sh\x15h\x12ubX\t\x00\x00\x00resourcesq\x17csnakemake.io\nResources\nq\x18)\x81q\x19(K\x01K\x01e}q\x1a(X\x06\x00\x00\x00_nodesq\x1bK\x01h\x0b}q\x1c(h\x1bK\x00N\x86q\x1dX\x06\x00\x00\x00_coresq\x1eK\x01N\x86q\x1fuh\x1eK\x01ubX\t\x00\x00\x00wildcardsq csnakemake.io\nWildcards\nq!)\x81q"X\x14\x00\x00\x00el42_kc_rump-10c3_R1q#a}q$(X\x06\x00\x00\x00sampleq%h#h\x0b}q&X\x06\x00\x00\x00sampleq\'K\x00N\x86q(subX\x05\x00\x00\x00inputq)csnakemake.io\nInputFiles\nq*)\x81q+(X\x1a\x00\x00\x00dedup/el38_kc_input_R1.bamq,X\x1e\x00\x00\x00dedup/el42_kc_rump-10c3_R1.bamq-e}q.(X\x03\x00\x00\x00inpq/h,X\x02\x00\x00\x00ipq0h-h\x0b}q1(h/K\x00N\x86q2h0K\x01N\x86q3uubX\x04\x00\x00\x00ruleq4X\x05\x00\x00\x00macs2q5X\x06\x00\x00\x00configq6}q7X\x03\x00\x00\x00logq8csnakemake.io\nLog\nq9)\x81q:}q;h\x0b}q<sbX\x07\x00\x00\x00threadsq=K\x01ub.')
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
