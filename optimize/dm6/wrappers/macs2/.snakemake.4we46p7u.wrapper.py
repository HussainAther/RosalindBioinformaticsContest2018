
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00resourcesq\x03csnakemake.io\nResources\nq\x04)\x81q\x05(K\x01K\x01e}q\x06(X\x06\x00\x00\x00_namesq\x07}q\x08(X\x06\x00\x00\x00_nodesq\tK\x00N\x86q\nX\x06\x00\x00\x00_coresq\x0bK\x01N\x86q\x0cuh\tK\x01h\x0bK\x01ubX\t\x00\x00\x00wildcardsq\rcsnakemake.io\nWildcards\nq\x0e)\x81q\x0fX\x10\x00\x00\x00sjl_cl8_cp190_R1q\x10a}q\x11(h\x07}q\x12X\x06\x00\x00\x00sampleq\x13K\x00N\x86q\x14sX\x06\x00\x00\x00sampleq\x15h\x10ubX\x06\x00\x00\x00paramsq\x16csnakemake.io\nParams\nq\x17)\x81q\x18(X\x1f\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1q\x19h\x10e}q\x1a(h\x07}q\x1b(X\x06\x00\x00\x00prefixq\x1cK\x00N\x86q\x1dX\x0e\x00\x00\x00wrapper_sampleq\x1eK\x01N\x86q\x1fuh\x1ch\x19h\x1eh\x10ubX\x04\x00\x00\x00ruleq X\x05\x00\x00\x00macs2q!X\x07\x00\x00\x00threadsq"K\x01X\x05\x00\x00\x00inputq#csnakemake.io\nInputFiles\nq$)\x81q%(X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq&X\x1a\x00\x00\x00dedup/sjl_cl8_cp190_R1.bamq\'e}q((h\x07}q)(X\x03\x00\x00\x00inpq*K\x00N\x86q+X\x02\x00\x00\x00ipq,K\x01N\x86q-uh*h&h,h\'ubX\x06\x00\x00\x00outputq.csnakemake.io\nOutputFiles\nq/)\x81q0(XA\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1_peaks.narrowPeakq1X4\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1.bedq2e}q3(h\x07}q4(X\n\x00\x00\x00narrowPeakq5K\x00N\x86q6X\x03\x00\x00\x00bedq7K\x01N\x86q8uh5h1h7h2ubX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x07}q=sbX\x06\x00\x00\x00configq>}q?ub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.r > {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.pdf')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
