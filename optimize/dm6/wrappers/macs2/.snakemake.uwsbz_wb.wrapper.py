
######## Snakemake header ########
import sys; sys.path.insert(0, "/data/Lei_student/Hussain/miniconda/envs/peakerror/lib/python3.6/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x18\x00\x00\x00bam/dc94_bg3_ctcf-59.bamq\x06X\x16\x00\x00\x00bam/dc93_bg3_input.bamq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x02\x00\x00\x00ipq\x0bK\x00N\x86q\x0cX\x03\x00\x00\x00inpq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x06\x00\x00\x00outputq\x0fcsnakemake.io\nOutputFiles\nq\x10)\x81q\x11X\x9c\x00\x00\x00peak_out/macs2/dc94_bg3_ctcf-59/q_value_2.1530571391796592e-07/llocal_10000/slocal_800/lowmfold_8/highmfold_50/nl/no-ds/tl/dc94_bg3_ctcf-59_peaks.narrowPeakq\x12a}q\x13(h\t}q\x14X\n\x00\x00\x00narrowPeakq\x15K\x00N\x86q\x16sh\x15h\x12ubX\x06\x00\x00\x00paramsq\x17csnakemake.io\nParams\nq\x18)\x81q\x19(Xz\x00\x00\x00peak_out/macs2/dc94_bg3_ctcf-59/q_value_2.1530571391796592e-07/llocal_10000/slocal_800/lowmfold_8/highmfold_50/nl/no-ds/tlq\x1aXO\x00\x00\x00peak_out/macs2/dc94_bg3_ctcf-59/q_value_2.1530571391796592e-07/dc94_bg3_ctcf-59q\x1bX\x16\x00\x00\x002.1530571391796592e-07q\x1cX\x05\x00\x00\x0010000q\x1dX\x03\x00\x00\x00800q\x1eX\x01\x00\x00\x008q\x1fX\x02\x00\x00\x0050q X\x05\x00\x00\x00no-dsq!X\x02\x00\x00\x00nlq"X\x02\x00\x00\x00tlq#e}q$(h\t}q%(X\r\x00\x00\x00outdir_prefixq&K\x00N\x86q\'X\r\x00\x00\x00sample_prefixq(K\x01N\x86q)X\x05\x00\x00\x00q_valq*K\x02N\x86q+X\x06\x00\x00\x00llocalq,K\x03N\x86q-X\x06\x00\x00\x00slocalq.K\x04N\x86q/X\x08\x00\x00\x00lowmfoldq0K\x05N\x86q1X\t\x00\x00\x00highmfoldq2K\x06N\x86q3X\n\x00\x00\x00downsampleq4K\x07N\x86q5X\x08\x00\x00\x00nolambdaq6K\x08N\x86q7X\x07\x00\x00\x00tolargeq8K\tN\x86q9uh&h\x1ah(h\x1bh*h\x1ch,h\x1dh.h\x1eh0h\x1fh2h h4h!h6h"h8h#ubX\t\x00\x00\x00wildcardsq:csnakemake.io\nWildcards\nq;)\x81q<(X\x10\x00\x00\x00dc94_bg3_ctcf-59q=h\x1ch\x1dh\x1eh\x1fh h"h!h#e}q>(h\t}q?(X\x06\x00\x00\x00sampleq@K\x00N\x86qAX\x07\x00\x00\x00q_valueqBK\x01N\x86qCX\x06\x00\x00\x00llocalqDK\x02N\x86qEX\x06\x00\x00\x00slocalqFK\x03N\x86qGX\x08\x00\x00\x00lowmfoldqHK\x04N\x86qIX\t\x00\x00\x00highmfoldqJK\x05N\x86qKX\x08\x00\x00\x00nolambdaqLK\x06N\x86qMX\n\x00\x00\x00downsampleqNK\x07N\x86qOX\x07\x00\x00\x00tolargeqPK\x08N\x86qQuX\x06\x00\x00\x00sampleqRh=X\x07\x00\x00\x00q_valueqSh\x1ch,h\x1dh.h\x1eh0h\x1fh2h h6h"h4h!h8h#ubX\x07\x00\x00\x00threadsqTK\x01X\t\x00\x00\x00resourcesqUcsnakemake.io\nResources\nqV)\x81qW(K\x01K\x01e}qX(h\t}qY(X\x06\x00\x00\x00_coresqZK\x00N\x86q[X\x06\x00\x00\x00_nodesq\\K\x01N\x86q]uhZK\x01h\\K\x01ubX\x03\x00\x00\x00logq^csnakemake.io\nLog\nq_)\x81q`}qah\t}qbsbX\x06\x00\x00\x00configqc}qdX\x04\x00\x00\x00ruleqeX\x05\x00\x00\x00macs2qfub.'); from snakemake.logging import logger; logger.printshellcmds = True
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

if snakemake.params.tolarge == "tl":
    tolarge_value = "--to-large"
elif snakemake.params.tolarge == "no-tl":
    tolarge_value = ""
else:
    raise ValueError("tolarge error")

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
    '{tolarge_value} '
    '-n {snakemake.wildcards.sample} '
    '--outdir {snakemake.params.outdir_prefix}'
)
#shell('Rscript {snakemake.params.sample_prefix}_model.r')
#shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
#shell("cd {snakemake.params.qval_prefix} && ln -sf $(basename {snakemake.output.narrowPeak}) $(basename {snakemake.output.bed})")

