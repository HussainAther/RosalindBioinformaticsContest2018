
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X\x1b\x00\x00\x00dedup/el37_bg3_input_R1.bamq\x06X\x1e\x00\x00\x00dedup/el39_bg3_rump-5g4_R1.bamq\x07e}q\x08(X\x03\x00\x00\x00inpq\th\x06X\x02\x00\x00\x00ipq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x07\x00\x00\x00threadsq\x0fK\x01X\x04\x00\x00\x00ruleq\x10X\x05\x00\x00\x00macs2q\x11X\t\x00\x00\x00wildcardsq\x12csnakemake.io\nWildcards\nq\x13)\x81q\x14X\x14\x00\x00\x00el39_bg3_rump-5g4_R1q\x15a}q\x16(h\x0b}q\x17X\x06\x00\x00\x00sampleq\x18K\x00N\x86q\x19sX\x06\x00\x00\x00sampleq\x1ah\x15ubX\x06\x00\x00\x00paramsq\x1bcsnakemake.io\nParams\nq\x1c)\x81q\x1dX#\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1q\x1ea}q\x1f(h\x0b}q X\x06\x00\x00\x00prefixq!K\x00N\x86q"sh!h\x1eubX\x06\x00\x00\x00configq#}q$X\x06\x00\x00\x00outputq%csnakemake.io\nOutputFiles\nq&)\x81q\'(X<\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1/el39_bg3_rump-5g4_R1.bedq(XI\x00\x00\x00peak_out/macs2/el39_bg3_rump-5g4_R1/el39_bg3_rump-5g4_R1_peaks.narrowPeakq)e}q*(X\x03\x00\x00\x00bedq+h(h\x0b}q,(h+K\x00N\x86q-X\n\x00\x00\x00narrowPeakq.K\x01N\x86q/uh.h)ubX\x03\x00\x00\x00logq0csnakemake.io\nLog\nq1)\x81q2}q3h\x0b}q4sbX\t\x00\x00\x00resourcesq5csnakemake.io\nResources\nq6)\x81q7(K\x01K\x01e}q8(X\x06\x00\x00\x00_coresq9K\x01h\x0b}q:(h9K\x00N\x86q;X\x06\x00\x00\x00_nodesq<K\x01N\x86q=uh<K\x01ubub.')
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
