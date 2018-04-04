
######## Snakemake header ########
import sys; sys.path.insert(0, "/data/Lei_student/Hussain/miniconda/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00configq\x03}q\x04X\x05\x00\x00\x00inputq\x05csnakemake.io\nInputFiles\nq\x06)\x81q\x07X\xac\x00\x00\x00peak_out/macs2/lm32_kc_suhw_R1/q_value_0.040677966101704405/llocal_20000/slocal_1000/lowmfold_12/highmfold_30/no-nl/no-ds/chr2R/lm32_kc_suhw_R1_peaks.broadPeak.threecolumnsq\x08a}q\tX\x06\x00\x00\x00_namesq\n}q\x0bsbX\x07\x00\x00\x00threadsq\x0cK\x01X\x06\x00\x00\x00outputq\rcsnakemake.io\nOutputFiles\nq\x0e)\x81q\x0fX\x9b\x00\x00\x00peakerror/macs2/lm32_kc_suhw_R1/q_value_0.040677966101704405/llocal_20000/slocal_1000/lowmfold_12/highmfold_30/no-nl/no-ds/chr2R/lm32_kc_suhw_R1_errors.tsvq\x10a}q\x11h\n}q\x12sbX\x06\x00\x00\x00paramsq\x13csnakemake.io\nParams\nq\x14)\x81q\x15(X(\x00\x00\x00peakerror/labels/kc_suhw/chr2Rlabels.bedq\x16X)\x00\x00\x00peakerror/labels/kc_cp190/chr2Rlabels.bedq\x17e}q\x18(X\r\x00\x00\x00kc_suhwlabelsq\x19h\x16h\n}q\x1a(h\x19K\x00N\x86q\x1bX\x0e\x00\x00\x00kc_cp190labelsq\x1cK\x01N\x86q\x1duh\x1ch\x17ubX\x03\x00\x00\x00logq\x1ecsnakemake.io\nLog\nq\x1f)\x81q }q!h\n}q"sbX\x04\x00\x00\x00ruleq#X\x11\x00\x00\x00peakerror_computeq$X\t\x00\x00\x00resourcesq%csnakemake.io\nResources\nq&)\x81q\'(K\x01K\x01e}q((X\x06\x00\x00\x00_nodesq)K\x01h\n}q*(h)K\x00N\x86q+X\x06\x00\x00\x00_coresq,K\x01N\x86q-uh,K\x01ubX\t\x00\x00\x00wildcardsq.csnakemake.io\nWildcards\nq/)\x81q0(X\x02\x00\x00\x0030q1X\x14\x00\x00\x000.040677966101704405q2X\x05\x00\x00\x00no-nlq3X\x05\x00\x00\x00no-dsq4X\x02\x00\x00\x0012q5X\x04\x00\x00\x001000q6X\x0f\x00\x00\x00lm32_kc_suhw_R1q7X\x05\x00\x00\x00chr2Rq8X\x05\x00\x00\x0020000q9e}q:(X\t\x00\x00\x00highmfoldq;h1X\x07\x00\x00\x00q_valueq<h2X\x06\x00\x00\x00llocalq=h9X\x08\x00\x00\x00nolambdaq>h3X\n\x00\x00\x00downsampleq?h4X\x08\x00\x00\x00lowmfoldq@h5X\x06\x00\x00\x00slocalqAh6h\n}qB(X\t\x00\x00\x00highmfoldqCK\x00N\x86qDX\x07\x00\x00\x00q_valueqEK\x01N\x86qFX\x08\x00\x00\x00nolambdaqGK\x02N\x86qHX\n\x00\x00\x00downsampleqIK\x03N\x86qJX\x08\x00\x00\x00lowmfoldqKK\x04N\x86qLX\x06\x00\x00\x00slocalqMK\x05N\x86qNX\x06\x00\x00\x00sampleqOK\x06N\x86qPX\x03\x00\x00\x00chrqQK\x07N\x86qRX\x06\x00\x00\x00llocalqSK\x08N\x86qTuX\x03\x00\x00\x00chrqUh8X\x06\x00\x00\x00sampleqVh7ubub.'); from snakemake.logging import logger; logger.printshellcmds = True
######## Original script #########
from snakemake import shell

for sample in snakemake.input:
    if "kc_suhw" in sample:
        shell("Rscript peakerror/PeakError_compute.R {sample} {snakemake.params.kc_suhwlabels} > {snakemake.output}")
    elif "kc_cp190" in sample:
        shell("Rscript peakerror/PeakError_compute.R {sample} {snakemake.params.kc_cp190labels} > {snakemake.output}")