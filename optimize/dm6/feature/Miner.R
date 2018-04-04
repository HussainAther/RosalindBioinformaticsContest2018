function (input = "/data/Lei_student/Hussain/ML/dm6/COPAR/data/SRR015350_copar.rda", plotPN = T, plotFDR = T,
              maxPN = T)
{
    load(input)
    inpN = strsplit(input, split = "[.]")[[1]][1]
    inpN
    BS.PN = matrix(BS[, 3], nrow = 9, byrow = T) # BS = read.table on the bam file
    print(BS.PN)
    rownames(BS.PN) = unique(BS[, 1])
    colnames(BS.PN) = unique(BS[, 2])
    BS.PN
    class(BS.PN)
    class(BS.PN[1, 2])
    save(file = paste(inpN, ".PN.rda", sep = ""), BS.PN)
    TT = BS[, 8]
    TT = as.numeric(sub("%", "", TT))
    BS.FDR = matrix(TT, nrow = 9, byrow = T)
    rm(TT)
    rownames(BS.FDR) = unique(BS[, 1])
    colnames(BS.FDR) = unique(BS[, 2])
    BS.FDR
    class(BS.FDR)
    class(BS.FDR[1, 1])
    save(file = paste(inpN, ".FDR.rda", sep = ""), BS.FDR)
     if (plotPN == T) {
         library(pheatmap)
         library(RColorBrewer)
    pheatmap(BS.PN, border_color = "white", cluster_rows = F,
    cluster_cols = F, color = colorRampPalette(rev(brewer.pal(n = 11,
    name = "RdBu")))(100), display_numbers = F, number_format = "%.1f",
    fontsize = 5, fontsize_row = 5, fontsize_col = 5,
    main = "Peak Number", cellwidth = 15, cellheight = 15,
    filename = paste(inpN, ".PN.tiff", sep = ""))
     }
     if (plotFDR == T) {
        library(pheatmap)
        library(RColorBrewer)
     pheatmap(BS.FDR, border_color = "white", cluster_rows = F,
     cluster_cols = F, color = colorRampPalette(c("grey",
     "navy", "red"))(50), display_numbers = F, number_format = "%.1f",
     fontsize = 5, fontsize_row = 5, fontsize_col = 5,
     main = "False Discovery Rate (%)", cellwidth = 15,
             cellheight = 15, filename = paste(inpN, ".FDR.tiff",
                                     sep = ""))
    }
}
