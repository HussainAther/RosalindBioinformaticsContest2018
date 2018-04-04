
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\t\x00\x00\x00wildcardsq\x03csnakemake.io\nWildcards\nq\x04)\x81q\x05X\x10\x00\x00\x00sjl_mbn2_suhw_R1q\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x06\x00\x00\x00sampleq\nK\x00N\x86q\x0bsX\x06\x00\x00\x00sampleq\x0ch\x06ubX\x05\x00\x00\x00inputq\rcsnakemake.io\nInputFiles\nq\x0e)\x81q\x0f(X\x1b\x00\x00\x00dedup/sjl_mbn2_input_R1.bamq\x10X\x1a\x00\x00\x00dedup/sjl_mbn2_suhw_R1.bamq\x11e}q\x12(h\x08}q\x13(X\x03\x00\x00\x00inpq\x14K\x00N\x86q\x15X\x02\x00\x00\x00ipq\x16K\x01N\x86q\x17uh\x14h\x10h\x16h\x11ubX\x06\x00\x00\x00outputq\x18csnakemake.io\nOutputFiles\nq\x19)\x81q\x1a(XA\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1_peaks.narrowPeakq\x1bX4\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1/sjl_mbn2_suhw_R1.bedq\x1ce}q\x1d(h\x08}q\x1e(X\n\x00\x00\x00narrowPeakq\x1fK\x00N\x86q X\x03\x00\x00\x00bedq!K\x01N\x86q"uh\x1fh\x1bh!h\x1cubX\t\x00\x00\x00resourcesq#csnakemake.io\nResources\nq$)\x81q%(K\x01K\x01e}q&(h\x08}q\'(X\x06\x00\x00\x00_nodesq(K\x00N\x86q)X\x06\x00\x00\x00_coresq*K\x01N\x86q+uh(K\x01h*K\x01ubX\x06\x00\x00\x00paramsq,csnakemake.io\nParams\nq-)\x81q.X\x1f\x00\x00\x00peak_out/macs2/sjl_mbn2_suhw_R1q/a}q0(h\x08}q1X\x06\x00\x00\x00prefixq2K\x00N\x86q3sh2h/ubX\x06\x00\x00\x00configq4}q5X\x07\x00\x00\x00threadsq6K\x01X\x04\x00\x00\x00ruleq7X\x05\x00\x00\x00macs2q8X\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x08}q=sbub.')
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
