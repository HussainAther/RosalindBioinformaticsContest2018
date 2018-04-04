
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(XG\x00\x00\x00peak_out/macs2/lm35_bg3_shep-r5_R1/lm35_bg3_shep-r5_R1_peaks.narrowPeakq\x06X:\x00\x00\x00peak_out/macs2/lm35_bg3_shep-r5_R1/lm35_bg3_shep-r5_R1.bedq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\n\x00\x00\x00narrowPeakq\x0bK\x00N\x86q\x0cX\x03\x00\x00\x00bedq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x06\x00\x00\x00configq\x0f}q\x10X\x07\x00\x00\x00threadsq\x11K\x01X\x06\x00\x00\x00paramsq\x12csnakemake.io\nParams\nq\x13)\x81q\x14X"\x00\x00\x00peak_out/macs2/lm35_bg3_shep-r5_R1q\x15a}q\x16(h\t}q\x17X\x06\x00\x00\x00prefixq\x18K\x00N\x86q\x19sh\x18h\x15ubX\x04\x00\x00\x00ruleq\x1aX\x05\x00\x00\x00macs2q\x1bX\x05\x00\x00\x00inputq\x1ccsnakemake.io\nInputFiles\nq\x1d)\x81q\x1e(X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq\x1fX\x1d\x00\x00\x00dedup/lm35_bg3_shep-r5_R1.bamq e}q!(h\t}q"(X\x03\x00\x00\x00inpq#K\x00N\x86q$X\x02\x00\x00\x00ipq%K\x01N\x86q&uh#h\x1fh%h ubX\x03\x00\x00\x00logq\'csnakemake.io\nLog\nq()\x81q)}q*h\t}q+sbX\t\x00\x00\x00wildcardsq,csnakemake.io\nWildcards\nq-)\x81q.X\x13\x00\x00\x00lm35_bg3_shep-r5_R1q/a}q0(h\t}q1X\x06\x00\x00\x00sampleq2K\x00N\x86q3sX\x06\x00\x00\x00sampleq4h/ubX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(h\t}q9(X\x06\x00\x00\x00_nodesq:K\x00N\x86q;X\x06\x00\x00\x00_coresq<K\x01N\x86q=uh:K\x01h<K\x01ubub.')
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
