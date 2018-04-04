
######## Snakemake header ########
import sys; sys.path.insert(0, "/data/Lei_student/Hussain/miniconda/envs/peakerror/lib/python3.6/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x11\x00\x00\x00bam/SRR567586.bamq\x06X\x11\x00\x00\x00bam/SRR567585.bamq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x02\x00\x00\x00ipq\x0bK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x06\x00\x00\x00outputq\x0fcsnakemake.io\nOutputFiles\nq\x10)\x81q\x11Xz\x00\x00\x00peak_out/macs2/SRR567586/q_value_0.06/llocal_10000/slocal_1000/lowmfold_3/highmfold_50/no-nl/ds/SRR567586_peaks.narrowPeakq\x12a}q\x13(h\t}q\x14X\n\x00\x00\x00narrowPeakq\x15K\x00N\x86q\x16sh\x15h\x12ubX\x06\x00\x00\x00paramsq\x17csnakemake.io\nParams\nq\x18)\x81q\x19(X_\x00\x00\x00peak_out/macs2/SRR567586/q_value_0.06/llocal_10000/slocal_1000/lowmfold_3/highmfold_50/no-nl/dsq\x1aX/\x00\x00\x00peak_out/macs2/SRR567586/q_value_0.06/SRR567586q\x1bX\x04\x00\x00\x000.06q\x1cX\x05\x00\x00\x0010000q\x1dX\x04\x00\x00\x001000q\x1eX\x01\x00\x00\x003q\x1fX\x02\x00\x00\x0050q X\x02\x00\x00\x00dsq!X\x05\x00\x00\x00no-nlq"e}q#(h\t}q$(X\r\x00\x00\x00outdir_prefixq%K\x00N\x86q&X\r\x00\x00\x00sample_prefixq\'K\x01N\x86q(X\x05\x00\x00\x00q_valq)K\x02N\x86q*X\x06\x00\x00\x00llocalq+K\x03N\x86q,X\x06\x00\x00\x00slocalq-K\x04N\x86q.X\x08\x00\x00\x00lowmfoldq/K\x05N\x86q0X\t\x00\x00\x00highmfoldq1K\x06N\x86q2X\n\x00\x00\x00downsampleq3K\x07N\x86q4X\x08\x00\x00\x00nolambdaq5K\x08N\x86q6uh%h\x1ah\'h\x1bh)h\x1ch+h\x1dh-h\x1eh/h\x1fh1h h3h!h5h"ubX\t\x00\x00\x00wildcardsq7csnakemake.io\nWildcards\nq8)\x81q9(X\t\x00\x00\x00SRR567586q:h\x1ch\x1dh\x1eh\x1fh h"h!e}q;(h\t}q<(X\x06\x00\x00\x00sampleq=K\x00N\x86q>X\x07\x00\x00\x00q_valueq?K\x01N\x86q@X\x06\x00\x00\x00llocalqAK\x02N\x86qBX\x06\x00\x00\x00slocalqCK\x03N\x86qDX\x08\x00\x00\x00lowmfoldqEK\x04N\x86qFX\t\x00\x00\x00highmfoldqGK\x05N\x86qHX\x08\x00\x00\x00nolambdaqIK\x06N\x86qJX\n\x00\x00\x00downsampleqKK\x07N\x86qLuX\x06\x00\x00\x00sampleqMh:X\x07\x00\x00\x00q_valueqNh\x1ch+h\x1dh-h\x1eh/h\x1fh1h h5h"h3h!ubX\x07\x00\x00\x00threadsqOK\x01X\t\x00\x00\x00resourcesqPcsnakemake.io\nResources\nqQ)\x81qR(K\x01K\x01e}qS(h\t}qT(X\x06\x00\x00\x00_coresqUK\x00N\x86qVX\x06\x00\x00\x00_nodesqWK\x01N\x86qXuhUK\x01hWK\x01ubX\x03\x00\x00\x00logqYcsnakemake.io\nLog\nqZ)\x81q[}q\\h\t}q]sbX\x06\x00\x00\x00configq^}q_X\x04\x00\x00\x00ruleq`X\x05\x00\x00\x00macs2qaub.'); from snakemake.logging import logger; logger.printshellcmds = True
######## Original script #########
from snakemake.shell import shell

downsample = {"ds" : "--down-sample", "no-ds" : ""}

if snakemake.params.downsample == "ds":
    downsample_value = "--down-sample"
elif snakemake.params.downsample == "no-ds":
    downsample_value = ""
else:
    raise ValueError("downsample error")

if snakemake.params.nolambda == "nl":
    nolambda_value = "--down-sample"
elif snakemake.params.nolambda == "no-nl":
    nolambda_value = ""
else:
    raise ValueError("nolambda error")

shell(
    'macs2 '
    'callpeak '
    '-c {snakemake.input.inp} '
    '-t {snakemake.input.ip} '
    '-q {snakemake.params.q_val} '
    '--llocal {snakemake.params.llocal} '
    '--slocal {snakemake.params.slocal} '
    '-m {snakemake.params.lowmfold} {snakemake.params.highmfold} '
    '{downsample_value} '
    '{nolambda_value} '
    '-n {snakemake.wildcards.sample} '
    '--outdir {snakemake.params.outdir_prefix}'
)
#shell('Rscript {snakemake.params.sample_prefix}_model.r')
#shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
#shell("cd {snakemake.params.qval_prefix} && ln -sf $(basename {snakemake.output.narrowPeak}) $(basename {snakemake.output.bed})")

