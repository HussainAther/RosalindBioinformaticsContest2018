
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x06X\x1a\x00\x00\x00dedup/sjl_mbn2_shep_R1.bamq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x03\x00\x00\x00inpq\x0bK\x00N\x86q\x0cX\x02\x00\x00\x00ipq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1q\x12a}q\x13(h\t}q\x14X\x06\x00\x00\x00prefixq\x15K\x00N\x86q\x16sh\x15h\x12ubX\x04\x00\x00\x00ruleq\x17X\x05\x00\x00\x00macs2q\x18X\t\x00\x00\x00wildcardsq\x19csnakemake.io\nWildcards\nq\x1a)\x81q\x1bX\x10\x00\x00\x00sjl_mbn2_shep_R1q\x1ca}q\x1d(h\t}q\x1eX\x06\x00\x00\x00sampleq\x1fK\x00N\x86q sX\x06\x00\x00\x00sampleq!h\x1cubX\t\x00\x00\x00resourcesq"csnakemake.io\nResources\nq#)\x81q$(K\x01K\x01e}q%(h\t}q&(X\x06\x00\x00\x00_nodesq\'K\x00N\x86q(X\x06\x00\x00\x00_coresq)K\x01N\x86q*uh\'K\x01h)K\x01ubX\x03\x00\x00\x00logq+csnakemake.io\nLog\nq,)\x81q-}q.h\t}q/sbX\x07\x00\x00\x00threadsq0K\x01X\x06\x00\x00\x00outputq1csnakemake.io\nOutputFiles\nq2)\x81q3(XA\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1_peaks.narrowPeakq4X4\x00\x00\x00peak_out/macs2/sjl_mbn2_shep_R1/sjl_mbn2_shep_R1.bedq5e}q6(h\t}q7(X\n\x00\x00\x00narrowPeakq8K\x00N\x86q9X\x03\x00\x00\x00bedq:K\x01N\x86q;uh8h4h:h5ubX\x06\x00\x00\x00configq<}q=ub.')
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
shell('Rscript {snakemake.params.prefix}_model.r')
