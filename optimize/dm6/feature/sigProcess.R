function (x, inpName = "SRR015350_copa")
{
    library(signal)
    Fs = 1000
    step = trunc(5 * Fs/1000)
    window <- trunc(40 * Fs/1000)
    fftn <- 2^ceiling(log2(abs(window)))
    x1 = x
    x2 = sample(x, replace = F)
    sx1 = specgram(x1, n = fftn, Fs, window, overlap = window - step)
    sx1
    S1 <- abs(sx1$S[2:(fftn * 500/Fs), ])
    S1
    S1 <- S1/max(S1)
    S1
    S1[S1 < 10^(-40/10)] <- 10^(-40/10)
    S1[S1 > 10^(-3/10)] <- 10^(-3/10)
    sx2 = specgram(x2, n = fftn, Fs, window, overlap = window - step)
    sx2
    S2 <- abs(sx2$S[2:(fftn * 500/Fs), ])
    S2
    S2 <- S2/max(S2)
    S2
    S2[S2 < 10^(-40/10)] <- 10^(-40/10)
    S2[S2 > 10^(-3/10)] <- 10^(-3/10)
    library(fields)
    tiff(file = paste(inpName, ".Spectrum.tiff", sep = ""))
    image.plot(t(20 * log10(S1)), axes = T, legend.shrink = 1,
    legend.width = 0.5, col = rainbow(100, alpha = 1), main = "Spectrum Distribution",
    xlab = "Frequency (0-500 Hz)", ylab = "Time (1-111 ms)",
    legend.only = F)
    dev.off()
    tiff(file = paste(inpName, ".Spectrum_Rand.tiff", sep = ""))
    image.plot(t(20 * log10(S2)), axes = T, legend.shrink = 1,
    legend.width = 0.5, col = rainbow(100, alpha = 1), main = "Spectrum Distribution (Random)",
    xlab = "Frequency (0-500 Hz)", ylab = "Time (1-111 ms)",
    legend.only = F)
    dev.off()
}
