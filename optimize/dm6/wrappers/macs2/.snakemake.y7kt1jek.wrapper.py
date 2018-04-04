
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X4\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1.bedq\x06XA\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1/sjl_cl8_cp190_R1_peaks.narrowPeakq\x07e}q\x08(X\x03\x00\x00\x00bedq\th\x06X\n\x00\x00\x00narrowPeakq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\t\x00\x00\x00resourcesq\x0fcsnakemake.io\nResources\nq\x10)\x81q\x11(K\x01K\x01e}q\x12(X\x06\x00\x00\x00_coresq\x13K\x01h\x0b}q\x14(h\x13K\x00N\x86q\x15X\x06\x00\x00\x00_nodesq\x16K\x01N\x86q\x17uh\x16K\x01ubX\x07\x00\x00\x00threadsq\x18K\x01X\t\x00\x00\x00wildcardsq\x19csnakemake.io\nWildcards\nq\x1a)\x81q\x1bX\x10\x00\x00\x00sjl_cl8_cp190_R1q\x1ca}q\x1d(X\x06\x00\x00\x00sampleq\x1eh\x1ch\x0b}q\x1fX\x06\x00\x00\x00sampleq K\x00N\x86q!subX\x06\x00\x00\x00paramsq"csnakemake.io\nParams\nq#)\x81q$X\x1f\x00\x00\x00peak_out/macs2/sjl_cl8_cp190_R1q%a}q&(h\x0b}q\'X\x06\x00\x00\x00prefixq(K\x00N\x86q)sh(h%ubX\x04\x00\x00\x00ruleq*X\x05\x00\x00\x00macs2q+X\x06\x00\x00\x00configq,}q-X\x05\x00\x00\x00inputq.csnakemake.io\nInputFiles\nq/)\x81q0(X\x1a\x00\x00\x00dedup/sjl_cl8_cp190_R1.bamq1X\x1a\x00\x00\x00dedup/sjl_cl8_input_R1.bamq2e}q3(X\x02\x00\x00\x00ipq4h1h\x0b}q5(h4K\x00N\x86q6X\x03\x00\x00\x00inpq7K\x01N\x86q8uh7h2ubX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x0b}q=sbub.')
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
shell('Rscript {snakemake.params.prefix}/{snakemake.input.ip}_model.r')
