from snakemake import shell

# ComputeMatrix calculates the scores of the genomic
# regions that is used to make heatmap and profile. 
# These scores are made from the regions bed file (-R) 
# and the score bigwig file (-S)

# The two methods for ComputeMatrix, reference-point 
# and scale-regions give different results. The 
# reference-point method looks only around a certain 
# reference point to compute score while scale-regions 
# looks at all the regions that are scaled down to a certain size.
shell('computeMatrix {snakemake.params.sub} -R {snakemake.input.spp_region} \
        -S {snakemake.input.ip} {snakemake.input.inp}  \
        --outFileNameMatrix heatmaps/{snakemake.params.sub}/{snakemake.params.sample}_spp_heatmapvalues.txt \
        -out matrices/{snakemake.params.sub}/spp_{snakemake.params.sample}')

shell('computeMatrix {snakemake.params.sub} -R {snakemake.input.spp_only} \
        -S {snakemake.input.ip} {snakemake.input.inp}  \
        --outFileNameMatrix heatmaps/{snakemake.params.sub}/{snakemake.params.sample}_spp_only_heatmapvalues.txt \
        -out matrices/{snakemake.params.sub}/spp_only_{snakemake.params.sample}')

shell('computeMatrix {snakemake.params.sub} -R {snakemake.input.spp2_region} \
        -S {snakemake.input.ip} {snakemake.input.inp}  \
        --outFileNameMatrix heatmaps/{snakemake.params.sub}/{snakemake.params.sample}_spp2_heatmapvalues.txt \
        -out matrices/{snakemake.params.sub}/spp2_{snakemake.params.sample}')

shell('computeMatrix {snakemake.params.sub} -R {snakemake.input.spp2_only} \
        -S {snakemake.input.ip} {snakemake.input.inp}  \
        --outFileNameMatrix heatmaps/{snakemake.params.sub}/{snakemake.params.sample}_spp2_only_heatmapvalues.txt \
        -out matrices/{snakemake.params.sub}/spp2_only_{snakemake.params.sample}')

shell('computeMatrix {snakemake.params.sub} -R {snakemake.input.macs2_region} \
        -S {snakemake.input.ip} {snakemake.input.inp} \
        --outFileNameMatrix heatmaps/{snakemake.params.sub}/{snakemake.params.sample}_macs2_heatmapvalues.txt \
        -out matrices/{snakemake.params.sub}/macs2_{snakemake.params.sample}')

shell('computeMatrix {snakemake.params.sub} -R {snakemake.input.macs2_only} \
        -S {snakemake.input.ip} {snakemake.input.inp} \
        --outFileNameMatrix heatmaps/{snakemake.params.sub}/{snakemake.params.sample}_macs2_only_heatmapvalues.txt \
        -out matrices/{snakemake.params.sub}/macs2_only_{snakemake.params.sample}')

shell('computeMatrix {snakemake.params.sub} -R {snakemake.input.overlap_spp} \
        -S {snakemake.input.ip} {snakemake.input.inp} \
        --outFileNameMatrix heatmaps/{snakemake.params.sub}/{snakemake.params.sample}_heatmapvalues.txt \
        -out matrices/{snakemake.params.sub}/overlap_spp_{snakemake.params.sample}')

shell('computeMatrix {snakemake.params.sub} -R {snakemake.input.overlap_spp2} \
        -S {snakemake.input.ip} {snakemake.input.inp} \
        --outFileNameMatrix heatmaps/{snakemake.params.sub}/{snakemake.params.sample}_heatmapvalues.txt \
        -out matrices/{snakemake.params.sub}/overlap_spp2_{snakemake.params.sample}')

# The Heatmaps are plotted and the other option 
# (--outFileNameData) gives the values in a .txt 
# file that can be used by other programs for graphing. 
shell('plotHeatmap -m matrices/{snakemake.params.sub}/spp_{snakemake.params.sample} \
        -out heatmaps/{snakemake.params.sub}/spp_{snakemake.params.sample}_heatmap.pdf')

shell('plotHeatmap -m matrices/{snakemake.params.sub}/spp2_{snakemake.params.sample} \
        -out heatmaps/{snakemake.params.sub}/spp2_{snakemake.params.sample}_heatmap.pdf')

shell('plotHeatmap -m matrices/{snakemake.params.sub}/macs2_{snakemake.params.sample} \
        -out heatmaps/{snakemake.params.sub}/macs2_{snakemake.params.sample}_heatmap.pdf')

shell('plotHeatmap -m matrices/{snakemake.params.sub}/spp_only_{snakemake.params.sample} \
        -out heatmaps/{snakemake.params.sub}/spp_only_{snakemake.params.sample}_heatmap.pdf')

shell('plotHeatmap -m matrices/{snakemake.params.sub}/spp2_only_{snakemake.params.sample} \
        -out heatmaps/{snakemake.params.sub}/spp2_only_{snakemake.params.sample}_heatmap.pdf')

shell('plotHeatmap -m matrices/{snakemake.params.sub}/macs2_only_{snakemake.params.sample} \
        -out heatmaps/{snakemake.params.sub}/macs2_only_{snakemake.params.sample}_heatmap.pdf')

shell('plotHeatmap -m matrices/{snakemake.params.sub}/overlap_spp_{snakemake.params.sample} \
        -out heatmaps/snakemake.params.sub}/overlap_spp_{snakemake.params.sample}_heatmap.pdf')

shell('plotHeatmap -m matrices/{snakemake.params.sub}/overlap_spp2_{snakemake.params.sample} \
        -out heatmaps/{snakemake.params.sub}/overlap_spp2_{snakemake.params.sample}_heatmap.pdf')

# The Profiles plot the scores over genomic regions.
shell('plotProfile -m matrices/{snakemake.params.sub}/spp_{snakemake.params.sample} \
        --outFileNameData profiles/{snakemake.params.sub}/spp_{snakemake.params.sample}_profilevalues.txt \
        -out profiles/{snakemake.params.sub}/spp_{snakemake.params.sample}_profile.pdf')

shell('plotProfile -m matrices/{snakemake.params.sub}/spp2_{snakemake.params.sample} \
        --outFileNameData profiles/{snakemake.params.sub}/spp2_{snakemake.params.sample}_profilevalues.txt \
        -out profiles/{snakemake.params.sub}/spp2_{snakemake.params.sample}_profile.pdf')

shell('plotProfile -m matrices/{snakemake.params.sub}/macs2_{snakemake.params.sample} \
        --outFileNameData profiles/{snakemake.params.sub}/macs2_{snakemake.params.sample}_profilevalues.txt \
        -out profiles/{snakemake.params.sub}/macs2_{snakemake.params.sample}_profile.pdf')

shell('plotProfile -m matrices/{snakemake.params.sub}/spp_only_{snakemake.params.sample} \
        --outFileNameData profiles/{snakemake.params.sub}/spp_only_{snakemake.params.sample}_profilevalues.txt \
        -out profiles/{snakemake.params.sub}/spp_only_{snakemake.params.sample}_profile.pdf')

shell('plotProfile -m matrices/{snakemake.params.sub}/spp2_only_{snakemake.params.sample} \
        --outFileNameData profiles/{snakemake.params.sub}/spp2_only_{snakemake.params.sample}_profilevalues.txt \
        -out profiles/{snakemake.params.sub}/spp2_only_{snakemake.params.sample}_profile.pdf')

shell('plotProfile -m matrices/{snakemake.params.sub}/macs2_only_{snakemake.params.sample} \
        --outFileNameData profiles/{snakemake.params.sub}/macs2_only_{snakemake.params.sample}_profilevalues.txt \
        -out profiles/{snakemake.params.sub}/macs2_only_{snakemake.params.sample}_profile.pdf')

shell('plotProfile -m matrices/{snakemake.params.sub}/overlap_spp_{snakemake.params.sample} \
        --outFileNameData profiles/{snakemake.params.sub}/overlap_spp_{snakemake.params.sample}_profilevalues.txt \
        -out profiles/{snakemake.params.sub}/overlap_spp_{snakemake.params.sample}_profile.pdf')

shell('plotProfile -m matrices/{snakemake.params.sub}/overlap_spp2_{snakemake.params.sample} \
        --outFileNameData profiles/{snakemake.params.sub}/overlap_spp2_{snakemake.params.sample}_profilevalues.txt \
        -out profiles/{snakemake.params.sub}/overlap_spp2_{snakemake.params.sample}_profile.pdf')

# the fingerprint gives an idea of how well the 
# immunoprecipitation worked. the larger the difference 
# between the input and the ip, the better. 
shell('plotFingerprint -b {snakemake.input.ip_bam} {snakemake.input.inp_bam} -plot {snakemake.output.fingerprints}')

