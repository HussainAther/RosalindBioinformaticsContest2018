
######## Snakemake header ########
import sys; sys.path.insert(0, "/data/Lei_student/Hussain/miniconda/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05(X\x05\x00\x00\x00no-nlq\x06X\x0f\x00\x00\x00lm32_kc_suhw_R1q\x07X\x05\x00\x00\x00no-dsq\x08X\x05\x00\x00\x0010000q\tX\x05\x00\x00\x00chr2Rq\nX\x01\x00\x00\x004q\x0bX\x02\x00\x00\x0030q\x0cX\x04\x00\x00\x002000q\rX\x14\x00\x00\x000.040677966101704405q\x0ee}q\x0f(X\x07\x00\x00\x00q_valueq\x10h\x0eX\t\x00\x00\x00highmfoldq\x11h\x0cX\x08\x00\x00\x00nolambdaq\x12h\x06X\x06\x00\x00\x00sampleq\x13h\x07X\n\x00\x00\x00downsampleq\x14h\x08X\x06\x00\x00\x00_namesq\x15}q\x16(X\x07\x00\x00\x00q_valueq\x17K\x08N\x86q\x18X\t\x00\x00\x00highmfoldq\x19K\x06N\x86q\x1aX\x08\x00\x00\x00nolambdaq\x1bK\x00N\x86q\x1cX\x06\x00\x00\x00sampleq\x1dK\x01N\x86q\x1eX\n\x00\x00\x00downsampleq\x1fK\x02N\x86q X\x03\x00\x00\x00chrq!K\x04N\x86q"X\x06\x00\x00\x00slocalq#K\x07N\x86q$X\x06\x00\x00\x00llocalq%K\x03N\x86q&X\x08\x00\x00\x00lowmfoldq\'K\x05N\x86q(uX\x06\x00\x00\x00llocalq)h\tX\x06\x00\x00\x00slocalq*h\rX\x03\x00\x00\x00chrq+h\nX\x08\x00\x00\x00lowmfoldq,h\x0bubX\x05\x00\x00\x00inputq-csnakemake.io\nInputFiles\nq.)\x81q/X\xab\x00\x00\x00peak_out/macs2/lm32_kc_suhw_R1/q_value_0.040677966101704405/llocal_10000/slocal_2000/lowmfold_4/highmfold_30/no-nl/no-ds/chr2R/lm32_kc_suhw_R1_peaks.broadPeak.threecolumnsq0a}q1h\x15}q2sbX\x06\x00\x00\x00outputq3csnakemake.io\nOutputFiles\nq4)\x81q5X\x9a\x00\x00\x00peakerror/macs2/lm32_kc_suhw_R1/q_value_0.040677966101704405/llocal_10000/slocal_2000/lowmfold_4/highmfold_30/no-nl/no-ds/chr2R/lm32_kc_suhw_R1_errors.tsvq6a}q7h\x15}q8sbX\x04\x00\x00\x00ruleq9X\x11\x00\x00\x00peakerror_computeq:X\x07\x00\x00\x00threadsq;K\x01X\x06\x00\x00\x00paramsq<csnakemake.io\nParams\nq=)\x81q>(X(\x00\x00\x00peakerror/labels/kc_suhw/chr2Rlabels.bedq?X)\x00\x00\x00peakerror/labels/kc_cp190/chr2Rlabels.bedq@e}qA(X\x0e\x00\x00\x00kc_cp190labelsqBh@X\r\x00\x00\x00kc_suhwlabelsqCh?h\x15}qD(hCK\x00N\x86qEhBK\x01N\x86qFuubX\x06\x00\x00\x00configqG}qHX\t\x00\x00\x00resourcesqIcsnakemake.io\nResources\nqJ)\x81qK(K\x01K\x01e}qL(X\x06\x00\x00\x00_nodesqMK\x01X\x06\x00\x00\x00_coresqNK\x01h\x15}qO(hNK\x00N\x86qPhMK\x01N\x86qQuubX\x03\x00\x00\x00logqRcsnakemake.io\nLog\nqS)\x81qT}qUh\x15}qVsbub.'); from snakemake.logging import logger; logger.printshellcmds = True
######## Original script #########
from snakemake import shell

for sample in snakemake.input:
    if "kc_suhw" in sample:
        shell("Rscript peakerror/PeakError_compute.R {sample} {snakemake.params.kc_suhwlabels} > {snakemake.output}")
    elif "kc_cp190" in sample:
        shell("Rscript peakerror/PeakError_compute.R {sample} {snakemake.params.kc_cp190labels} > {snakemake.output}")
