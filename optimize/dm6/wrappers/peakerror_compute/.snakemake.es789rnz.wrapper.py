
######## Snakemake header ########
import sys; sys.path.insert(0, "/data/Lei_student/Hussain/miniconda/envs/peakerror/lib/python3.6/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05X\x99\x00\x00\x00peak_out/macs2/sjl_kc_cp190_R1/q_value_0.05/llocal_5000/slocal_500/lowmfold_7/highmfold_60/no-nl/no-ds/chr3R/sjl_kc_cp190_R1_peaks.broadPeak.threecolumnsq\x06a}q\x07X\x06\x00\x00\x00_namesq\x08}q\tsbX\x06\x00\x00\x00outputq\ncsnakemake.io\nOutputFiles\nq\x0b)\x81q\x0cX\x8b\x00\x00\x00peakerror/macs2/sjl_kc_cp190_R1/q_value_0.05/llocal_5000/slocal_500/lowmfold_7/highmfold_60/no-nl/no-ds/chr3R_10/sjl_kc_cp190_R1_errors.tsvq\ra}q\x0eh\x08}q\x0fsbX\x06\x00\x00\x00paramsq\x10csnakemake.io\nParams\nq\x11)\x81q\x12X,\x00\x00\x00peakerror/labels/kc_cp190/chr3Rlabels_10.bedq\x13a}q\x14(h\x08}q\x15X\x0e\x00\x00\x00kc_cp190labelsq\x16K\x00N\x86q\x17sh\x16h\x13ubX\t\x00\x00\x00wildcardsq\x18csnakemake.io\nWildcards\nq\x19)\x81q\x1a(X\x0f\x00\x00\x00sjl_kc_cp190_R1q\x1bX\x04\x00\x00\x000.05q\x1cX\x04\x00\x00\x005000q\x1dX\x03\x00\x00\x00500q\x1eX\x01\x00\x00\x007q\x1fX\x02\x00\x00\x0060q X\x05\x00\x00\x00no-nlq!X\x05\x00\x00\x00no-dsq"X\x05\x00\x00\x00chr3Rq#X\x02\x00\x00\x0010q$e}q%(h\x08}q&(X\x06\x00\x00\x00sampleq\'K\x00N\x86q(X\x07\x00\x00\x00q_valueq)K\x01N\x86q*X\x06\x00\x00\x00llocalq+K\x02N\x86q,X\x06\x00\x00\x00slocalq-K\x03N\x86q.X\x08\x00\x00\x00lowmfoldq/K\x04N\x86q0X\t\x00\x00\x00highmfoldq1K\x05N\x86q2X\x08\x00\x00\x00nolambdaq3K\x06N\x86q4X\n\x00\x00\x00downsampleq5K\x07N\x86q6X\x03\x00\x00\x00chrq7K\x08N\x86q8X\t\x00\x00\x00chrom_cutq9K\tN\x86q:uX\x06\x00\x00\x00sampleq;h\x1bX\x07\x00\x00\x00q_valueq<h\x1cX\x06\x00\x00\x00llocalq=h\x1dX\x06\x00\x00\x00slocalq>h\x1eX\x08\x00\x00\x00lowmfoldq?h\x1fX\t\x00\x00\x00highmfoldq@h X\x08\x00\x00\x00nolambdaqAh!X\n\x00\x00\x00downsampleqBh"X\x03\x00\x00\x00chrqCh#X\t\x00\x00\x00chrom_cutqDh$ubX\x07\x00\x00\x00threadsqEK\x01X\t\x00\x00\x00resourcesqFcsnakemake.io\nResources\nqG)\x81qH(K\x01K\x01e}qI(h\x08}qJ(X\x06\x00\x00\x00_coresqKK\x00N\x86qLX\x06\x00\x00\x00_nodesqMK\x01N\x86qNuhKK\x01hMK\x01ubX\x03\x00\x00\x00logqOcsnakemake.io\nLog\nqP)\x81qQ}qRh\x08}qSsbX\x06\x00\x00\x00configqT}qUX\x04\x00\x00\x00ruleqVX\x11\x00\x00\x00peakerror_computeqWub.'); from snakemake.logging import logger; logger.printshellcmds = False
######## Original script #########
from snakemake import shell

for sample in snakemake.input:
#    if "kc_suhw" in sample:
#        shell("Rscript peakerror/PeakError_compute.R {sample} {snakemake.params.kc_suhwlabels} > {snakemake.output}")
    if "kc_cp190" in sample:
        shell("Rscript peakerror/PeakError_compute.R {sample} {snakemake.params.kc_cp190labels} > {snakemake.output}")