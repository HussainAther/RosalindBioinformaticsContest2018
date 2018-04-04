
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X:\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1/el40_kc_rump-5g4_R1.bedq\x06XG\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1/el40_kc_rump-5g4_R1_peaks.narrowPeakq\x07e}q\x08X\x06\x00\x00\x00_namesq\t}q\nsbX\x05\x00\x00\x00inputq\x0bcsnakemake.io\nInputFiles\nq\x0c)\x81q\r(X\x1a\x00\x00\x00dedup/el38_kc_input_R1.bamq\x0eX\x1d\x00\x00\x00dedup/el40_kc_rump-5g4_R1.bamq\x0fe}q\x10(h\t}q\x11(X\x03\x00\x00\x00inpq\x12K\x00N\x86q\x13X\x02\x00\x00\x00ipq\x14K\x01N\x86q\x15uh\x12h\x0eh\x14h\x0fubX\t\x00\x00\x00wildcardsq\x16csnakemake.io\nWildcards\nq\x17)\x81q\x18X\x13\x00\x00\x00el40_kc_rump-5g4_R1q\x19a}q\x1a(X\x06\x00\x00\x00sampleq\x1bh\x19h\t}q\x1cX\x06\x00\x00\x00sampleq\x1dK\x00N\x86q\x1esubX\t\x00\x00\x00resourcesq\x1fcsnakemake.io\nResources\nq )\x81q!(K\x01K\x01e}q"(X\x06\x00\x00\x00_coresq#K\x01X\x06\x00\x00\x00_nodesq$K\x01h\t}q%(h$K\x00N\x86q&h#K\x01N\x86q\'uubX\x03\x00\x00\x00logq(csnakemake.io\nLog\nq))\x81q*}q+h\t}q,sbX\x07\x00\x00\x00threadsq-K\x01X\x04\x00\x00\x00ruleq.X\x05\x00\x00\x00macs2q/X\x06\x00\x00\x00paramsq0csnakemake.io\nParams\nq1)\x81q2X"\x00\x00\x00peak_out/macs2/el40_kc_rump-5g4_R1q3a}q4(X\x06\x00\x00\x00prefixq5h3h\t}q6h5K\x00N\x86q7subX\x06\x00\x00\x00configq8}q9ub.')
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

