
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_nodesq\x07K\x01X\x06\x00\x00\x00_namesq\x08}q\t(X\x06\x00\x00\x00_coresq\nK\x00N\x86q\x0bh\x07K\x01N\x86q\x0cuh\nK\x01ubX\x07\x00\x00\x00threadsq\rK\x01X\x05\x00\x00\x00inputq\x0ecsnakemake.io\nInputFiles\nq\x0f)\x81q\x10(X\x1e\x00\x00\x00dedup/el39_bg3_rump-5g4_R1.bamq\x11X\x1b\x00\x00\x00dedup/el37_bg3_input_R1.bamq\x12e}q\x13(X\x02\x00\x00\x00ipq\x14h\x11h\x08}q\x15(h\x14K\x00N\x86q\x16X\x03\x00\x00\x00inpq\x17K\x01N\x86q\x18uh\x17h\x12ubX\t\x00\x00\x00wildcardsq\x19csnakemake.io\nWildcards\nq\x1a)\x81q\x1bX\x14\x00\x00\x00el39_bg3_rump-5g4_R1q\x1ca}q\x1d(X\x06\x00\x00\x00sampleq\x1eh\x1ch\x08}q\x1fX\x06\x00\x00\x00sampleq K\x00N\x86q!subX\x06\x00\x00\x00paramsq"csnakemake.io\nParams\nq#)\x81q$X#\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1q%a}q&(h\x08}q\'X\x06\x00\x00\x00prefixq(K\x00N\x86q)sh(h%ubX\x06\x00\x00\x00configq*}q+X\x04\x00\x00\x00ruleq,X\x05\x00\x00\x00macs2q-X\x03\x00\x00\x00logq.csnakemake.io\nLog\nq/)\x81q0}q1h\x08}q2sbX\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X<\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1/el39_bg3_rump-5g4_R1.bedq6XI\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1/el39_bg3_rump-5g4_R1_peaks.narrowPeakq7e}q8h\x08}q9sbub.')
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

