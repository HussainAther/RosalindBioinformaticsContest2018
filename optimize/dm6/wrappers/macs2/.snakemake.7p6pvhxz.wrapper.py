
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00outputq\x04csnakemake.io\nOutputFiles\nq\x05)\x81q\x06(XI\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1/el39_bg3_rump-5g4_R1_peaks.narrowPeakq\x07X<\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1/el39_bg3_rump-5g4_R1.bedq\x08e}q\t(X\n\x00\x00\x00narrowPeakq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\nK\x00N\x86q\rX\x03\x00\x00\x00bedq\x0eK\x01N\x86q\x0fuh\x0eh\x08ubX\t\x00\x00\x00resourcesq\x10csnakemake.io\nResources\nq\x11)\x81q\x12(K\x01K\x01e}q\x13(h\x0b}q\x14(X\x06\x00\x00\x00_coresq\x15K\x00N\x86q\x16X\x06\x00\x00\x00_nodesq\x17K\x01N\x86q\x18uh\x15K\x01h\x17K\x01ubX\x05\x00\x00\x00inputq\x19csnakemake.io\nInputFiles\nq\x1a)\x81q\x1b(X\x1b\x00\x00\x00dedup/el37_bg3_input_R1.bamq\x1cX\x1e\x00\x00\x00dedup/el39_bg3_rump-5g4_R1.bamq\x1de}q\x1e(X\x03\x00\x00\x00inpq\x1fh\x1cX\x02\x00\x00\x00ipq h\x1dh\x0b}q!(h\x1fK\x00N\x86q"h K\x01N\x86q#uubX\x03\x00\x00\x00logq$csnakemake.io\nLog\nq%)\x81q&}q\'h\x0b}q(sbX\x04\x00\x00\x00ruleq)X\x05\x00\x00\x00macs2q*X\x06\x00\x00\x00configq+}q,X\t\x00\x00\x00wildcardsq-csnakemake.io\nWildcards\nq.)\x81q/X\x14\x00\x00\x00el39_bg3_rump-5g4_R1q0a}q1(h\x0b}q2X\x06\x00\x00\x00sampleq3K\x00N\x86q4sX\x06\x00\x00\x00sampleq5h0ubX\x06\x00\x00\x00paramsq6csnakemake.io\nParams\nq7)\x81q8X#\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1q9a}q:(h\x0b}q;X\x06\x00\x00\x00prefixq<K\x00N\x86q=sh<h9ubub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.sample}_model.r')
