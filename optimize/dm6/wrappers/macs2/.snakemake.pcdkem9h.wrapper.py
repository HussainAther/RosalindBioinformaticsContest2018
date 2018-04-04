
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x07\x00\x00\x00threadsq\x03K\x01X\x06\x00\x00\x00configq\x04}q\x05X\t\x00\x00\x00wildcardsq\x06csnakemake.io\nWildcards\nq\x07)\x81q\x08X\x10\x00\x00\x00lm33_bg3_suhw_R1q\ta}q\n(X\x06\x00\x00\x00_namesq\x0b}q\x0cX\x06\x00\x00\x00sampleq\rK\x00N\x86q\x0esX\x06\x00\x00\x00sampleq\x0fh\tubX\x05\x00\x00\x00inputq\x10csnakemake.io\nInputFiles\nq\x11)\x81q\x12(X\x1a\x00\x00\x00dedup/lm33_bg3_suhw_R1.bamq\x13X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq\x14e}q\x15(X\x02\x00\x00\x00ipq\x16h\x13X\x03\x00\x00\x00inpq\x17h\x14h\x0b}q\x18(h\x16K\x00N\x86q\x19h\x17K\x01N\x86q\x1auubX\t\x00\x00\x00resourcesq\x1bcsnakemake.io\nResources\nq\x1c)\x81q\x1d(K\x01K\x01e}q\x1e(X\x06\x00\x00\x00_coresq\x1fK\x01h\x0b}q (h\x1fK\x00N\x86q!X\x06\x00\x00\x00_nodesq"K\x01N\x86q#uh"K\x01ubX\x04\x00\x00\x00ruleq$X\x05\x00\x00\x00macs2q%X\x06\x00\x00\x00paramsq&csnakemake.io\nParams\nq\')\x81q(X\x1f\x00\x00\x00peak_out/macs2/lm33_bg3_suhw_R1q)a}q*(X\x06\x00\x00\x00prefixq+h)h\x0b}q,h+K\x00N\x86q-subX\x03\x00\x00\x00logq.csnakemake.io\nLog\nq/)\x81q0}q1h\x0b}q2sbX\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5(X4\x00\x00\x00peak_out/macs2/lm33_bg3_suhw_R1/lm33_bg3_suhw_R1.bedq6XA\x00\x00\x00peak_out/macs2/lm33_bg3_suhw_R1/lm33_bg3_suhw_R1_peaks.narrowPeakq7e}q8(X\x03\x00\x00\x00bedq9h6X\n\x00\x00\x00narrowPeakq:h7h\x0b}q;(h9K\x00N\x86q<h:K\x01N\x86q=uubub.')
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
