
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00logq\x03csnakemake.io\nLog\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\t\x00\x00\x00wildcardsq\tcsnakemake.io\nWildcards\nq\n)\x81q\x0bX\x0f\x00\x00\x00sjl_kc_cp190_R1q\x0ca}q\r(h\x07}q\x0eX\x06\x00\x00\x00sampleq\x0fK\x00N\x86q\x10sX\x06\x00\x00\x00sampleq\x11h\x0cubX\x06\x00\x00\x00paramsq\x12csnakemake.io\nParams\nq\x13)\x81q\x14X\x1e\x00\x00\x00peak_out/macs2/sjl_kc_cp190_R1q\x15a}q\x16(h\x07}q\x17X\x06\x00\x00\x00prefixq\x18K\x00N\x86q\x19sh\x18h\x15ubX\t\x00\x00\x00resourcesq\x1acsnakemake.io\nResources\nq\x1b)\x81q\x1c(K\x01K\x01e}q\x1d(h\x07}q\x1e(X\x06\x00\x00\x00_coresq\x1fK\x00N\x86q X\x06\x00\x00\x00_nodesq!K\x01N\x86q"uh!K\x01h\x1fK\x01ubX\x06\x00\x00\x00configq#}q$X\x05\x00\x00\x00inputq%csnakemake.io\nInputFiles\nq&)\x81q\'(X\x19\x00\x00\x00dedup/sjl_kc_cp190_R1.bamq(X\x19\x00\x00\x00dedup/sjl_kc_input_R1.bamq)e}q*(h\x07}q+(X\x02\x00\x00\x00ipq,K\x00N\x86q-X\x03\x00\x00\x00inpq.K\x01N\x86q/uh,h(h.h)ubX\x07\x00\x00\x00threadsq0K\x01X\x06\x00\x00\x00outputq1csnakemake.io\nOutputFiles\nq2)\x81q3(X?\x00\x00\x00peak_out/macs2/sjl_kc_cp190_R1/sjl_kc_cp190_R1_peaks.narrowPeakq4X2\x00\x00\x00peak_out/macs2/sjl_kc_cp190_R1/sjl_kc_cp190_R1.bedq5e}q6(h\x07}q7(X\n\x00\x00\x00narrowPeakq8K\x00N\x86q9X\x03\x00\x00\x00bedq:K\x01N\x86q;uh8h4h:h5ubX\x04\x00\x00\x00ruleq<X\x05\x00\x00\x00macs2q=ub.')
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
shell('touch {snakemake.output.bed}')
shell('Rscript peak_out/macs2/{snakemake.params.prefix}_model.r')
