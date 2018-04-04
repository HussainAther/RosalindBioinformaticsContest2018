
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x04\x00\x00\x00ruleq\tX\x05\x00\x00\x00macs2q\nX\x06\x00\x00\x00configq\x0b}q\x0cX\x06\x00\x00\x00paramsq\rcsnakemake.io\nParams\nq\x0e)\x81q\x0fX!\x00\x00\x00peak_out/macs2/lm44_bg3_mod-rb_R1q\x10a}q\x11(h\x07}q\x12X\x06\x00\x00\x00prefixq\x13K\x00N\x86q\x14sh\x13h\x10ubX\t\x00\x00\x00wildcardsq\x15csnakemake.io\nWildcards\nq\x16)\x81q\x17X\x12\x00\x00\x00lm44_bg3_mod-rb_R1q\x18a}q\x19(h\x07}q\x1aX\x06\x00\x00\x00sampleq\x1bK\x00N\x86q\x1csX\x06\x00\x00\x00sampleq\x1dh\x18ubX\t\x00\x00\x00resourcesq\x1ecsnakemake.io\nResources\nq\x1f)\x81q (K\x01K\x01e}q!(h\x07}q"(X\x06\x00\x00\x00_nodesq#K\x00N\x86q$X\x06\x00\x00\x00_coresq%K\x01N\x86q&uh%K\x01h#K\x01ubX\x07\x00\x00\x00threadsq\'K\x01X\x05\x00\x00\x00inputq(csnakemake.io\nInputFiles\nq))\x81q*(X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq+X\x1c\x00\x00\x00dedup/lm44_bg3_mod-rb_R1.bamq,e}q-(X\x03\x00\x00\x00inpq.h+h\x07}q/(h.K\x00N\x86q0X\x02\x00\x00\x00ipq1K\x01N\x86q2uh1h,ubX\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X8\x00\x00\x00peak_out/macs2/lm44_bg3_mod-rb_R1/lm44_bg3_mod-rb_R1.bedq6XE\x00\x00\x00peak_out/macs2/lm44_bg3_mod-rb_R1/lm44_bg3_mod-rb_R1_peaks.narrowPeakq7e}q8(X\n\x00\x00\x00narrowPeakq9h7h\x07}q:(h9K\x01N\x86q;X\x03\x00\x00\x00bedq<K\x00N\x86q=uh<h6ubub.')
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
