
######## Snakemake header ########
import sys; sys.path.insert(0, "/data/Lei_student/Hussain/miniconda/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05(X\x14\x00\x00\x000.027118644067806272q\x06X\x04\x00\x00\x001000q\x07X\x01\x00\x00\x008q\x08X\x0f\x00\x00\x00lm32_kc_suhw_R1q\tX\x02\x00\x00\x0050q\nX\x05\x00\x00\x00no-nlq\x0bX\x02\x00\x00\x00dsq\x0cX\x05\x00\x00\x00chr2Rq\rX\x05\x00\x00\x0020000q\x0ee}q\x0f(X\x06\x00\x00\x00_namesq\x10}q\x11(X\x07\x00\x00\x00q_valueq\x12K\x00N\x86q\x13X\x06\x00\x00\x00llocalq\x14K\x08N\x86q\x15X\x08\x00\x00\x00nolambdaq\x16K\x05N\x86q\x17X\x06\x00\x00\x00sampleq\x18K\x03N\x86q\x19X\t\x00\x00\x00highmfoldq\x1aK\x04N\x86q\x1bX\x08\x00\x00\x00lowmfoldq\x1cK\x02N\x86q\x1dX\n\x00\x00\x00downsampleq\x1eK\x06N\x86q\x1fX\x03\x00\x00\x00chrq K\x07N\x86q!X\x06\x00\x00\x00slocalq"K\x01N\x86q#uX\x07\x00\x00\x00q_valueq$h\x06X\x06\x00\x00\x00llocalq%h\x0eX\x08\x00\x00\x00nolambdaq&h\x0bX\x06\x00\x00\x00sampleq\'h\tX\t\x00\x00\x00highmfoldq(h\nX\x08\x00\x00\x00lowmfoldq)h\x08X\n\x00\x00\x00downsampleq*h\x0cX\x03\x00\x00\x00chrq+h\rX\x06\x00\x00\x00slocalq,h\x07ubX\x06\x00\x00\x00outputq-csnakemake.io\nOutputFiles\nq.)\x81q/X\x97\x00\x00\x00peakerror/macs2/lm32_kc_suhw_R1/q_value_0.027118644067806272/llocal_20000/slocal_1000/lowmfold_8/highmfold_50/no-nl/ds/chr2R/lm32_kc_suhw_R1_errors.tsvq0a}q1h\x10}q2sbX\x04\x00\x00\x00ruleq3X\x11\x00\x00\x00peakerror_computeq4X\x06\x00\x00\x00paramsq5csnakemake.io\nParams\nq6)\x81q7(X)\x00\x00\x00peakerror/labels/kc_cp190/chr2Rlabels.bedq8X(\x00\x00\x00peakerror/labels/kc_suhw/chr2Rlabels.bedq9e}q:(h\x10}q;(X\x0e\x00\x00\x00kc_cp190labelsq<K\x00N\x86q=X\r\x00\x00\x00kc_suhwlabelsq>K\x01N\x86q?uh<h8h>h9ubX\x05\x00\x00\x00inputq@csnakemake.io\nInputFiles\nqA)\x81qBX\xa8\x00\x00\x00peak_out/macs2/lm32_kc_suhw_R1/q_value_0.027118644067806272/llocal_20000/slocal_1000/lowmfold_8/highmfold_50/no-nl/ds/chr2R/lm32_kc_suhw_R1_peaks.broadPeak.threecolumnsqCa}qDh\x10}qEsbX\t\x00\x00\x00resourcesqFcsnakemake.io\nResources\nqG)\x81qH(K\x01K\x01e}qI(X\x06\x00\x00\x00_nodesqJK\x01X\x06\x00\x00\x00_coresqKK\x01h\x10}qL(hJK\x00N\x86qMhKK\x01N\x86qNuubX\x06\x00\x00\x00configqO}qPX\x03\x00\x00\x00logqQcsnakemake.io\nLog\nqR)\x81qS}qTh\x10}qUsbX\x07\x00\x00\x00threadsqVK\x01ub.'); from snakemake.logging import logger; logger.printshellcmds = True
######## Original script #########
from snakemake import shell

for sample in snakemake.input:
    if "kc_suhw" in sample:
        shell("Rscript peakerror/PeakError_compute.R {sample} {snakemake.params.kc_suhwlabels} > {snakemake.output}")
    elif "kc_cp190" in sample:
        shell("Rscript peakerror/PeakError_compute.R {sample} {snakemake.params.kc_cp190labels} > {snakemake.output}")