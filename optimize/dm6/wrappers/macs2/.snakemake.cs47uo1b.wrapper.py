
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_coresq\x07K\x01X\x06\x00\x00\x00_nodesq\x08K\x01X\x06\x00\x00\x00_namesq\t}q\n(h\x07K\x00N\x86q\x0bh\x08K\x01N\x86q\x0cuubX\x07\x00\x00\x00threadsq\rK\x01X\x03\x00\x00\x00logq\x0ecsnakemake.io\nLog\nq\x0f)\x81q\x10}q\x11h\t}q\x12sbX\x06\x00\x00\x00paramsq\x13csnakemake.io\nParams\nq\x14)\x81q\x15(X\x13\x00\x00\x00el40_kc_rump-5g4_R1q\x16X"\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1q\x17e}q\x18(X\x0e\x00\x00\x00wrapper_sampleq\x19h\x16X\x06\x00\x00\x00prefixq\x1ah\x17h\t}q\x1b(h\x19K\x00N\x86q\x1ch\x1aK\x01N\x86q\x1duubX\x04\x00\x00\x00ruleq\x1eX\x05\x00\x00\x00macs2q\x1fX\t\x00\x00\x00wildcardsq csnakemake.io\nWildcards\nq!)\x81q"h\x16a}q#(X\x06\x00\x00\x00sampleq$h\x16h\t}q%X\x06\x00\x00\x00sampleq&K\x00N\x86q\'subX\x06\x00\x00\x00outputq(csnakemake.io\nOutputFiles\nq))\x81q*(XG\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1/el40_kc_rump-5g4_R1_peaks.narrowPeakq+X:\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1/el40_kc_rump-5g4_R1.bedq,e}q-(X\n\x00\x00\x00narrowPeakq.h+X\x03\x00\x00\x00bedq/h,h\t}q0(h.K\x00N\x86q1h/K\x01N\x86q2uubX\x06\x00\x00\x00configq3}q4X\x05\x00\x00\x00inputq5csnakemake.io\nInputFiles\nq6)\x81q7(X\x1d\x00\x00\x00dedup/el40_kc_rump-5g4_R1.bamq8X\x1a\x00\x00\x00dedup/el38_kc_input_R1.bamq9e}q:(X\x02\x00\x00\x00ipq;h8X\x03\x00\x00\x00inpq<h9h\t}q=(h;K\x00N\x86q>h<K\x01N\x86q?uubub.')
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
