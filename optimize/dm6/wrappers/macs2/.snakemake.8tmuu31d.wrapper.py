
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X:\x00\x00\x00peak_out/macs2/lm47_bg3_rump5g4_R1/lm47_bg3_rump5g4_R1.bedq\x06XG\x00\x00\x00peak_out/macs2/lm47_bg3_rump5g4_R1/lm47_bg3_rump5g4_R1_peaks.narrowPeakq\x07e}q\x08(X\x03\x00\x00\x00bedq\th\x06X\n\x00\x00\x00narrowPeakq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x06\x00\x00\x00paramsq\x0fcsnakemake.io\nParams\nq\x10)\x81q\x11X"\x00\x00\x00peak_out/macs2/lm47_bg3_rump5g4_R1q\x12a}q\x13(h\x0b}q\x14X\x06\x00\x00\x00prefixq\x15K\x00N\x86q\x16sh\x15h\x12ubX\t\x00\x00\x00resourcesq\x17csnakemake.io\nResources\nq\x18)\x81q\x19(K\x01K\x01e}q\x1a(X\x06\x00\x00\x00_coresq\x1bK\x01h\x0b}q\x1c(h\x1bK\x00N\x86q\x1dX\x06\x00\x00\x00_nodesq\x1eK\x01N\x86q\x1fuh\x1eK\x01ubX\t\x00\x00\x00wildcardsq csnakemake.io\nWildcards\nq!)\x81q"X\x13\x00\x00\x00lm47_bg3_rump5g4_R1q#a}q$(h\x0b}q%X\x06\x00\x00\x00sampleq&K\x00N\x86q\'sX\x06\x00\x00\x00sampleq(h#ubX\x06\x00\x00\x00configq)}q*X\x07\x00\x00\x00threadsq+K\x01X\x04\x00\x00\x00ruleq,X\x05\x00\x00\x00macs2q-X\x05\x00\x00\x00inputq.csnakemake.io\nInputFiles\nq/)\x81q0(X\x1d\x00\x00\x00dedup/lm47_bg3_rump5g4_R1.bamq1X\x1b\x00\x00\x00dedup/lm31_bg3_input_R1.bamq2e}q3(X\x02\x00\x00\x00ipq4h1X\x03\x00\x00\x00inpq5h2h\x0b}q6(h4K\x00N\x86q7h5K\x01N\x86q8uubX\x03\x00\x00\x00logq9csnakemake.io\nLog\nq:)\x81q;}q<h\x0b}q=sbub.')
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
