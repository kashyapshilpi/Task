# Load required library
library(ggplot2)

# Read the data from the provided input file
gene_data <- read.delim("task3.txt", stringsAsFactors = FALSE, fill = TRUE)

# Convert "chromosome" column to factor
gene_data$chromosome <- as.factor(gene_data$chromosome)

# Create the plot using ggplot2 
ggplot(gene_data, aes(x = chromosome)) +
  geom_bar(color = "black", fill = "darkgrey") +
  labs(title = "Number of Genes per Chromosome",
       x = "Chromosome",
       y = "Number of Genes") +
  theme_minimal()

# Save the plot to a PDF file
ggsave("genes_per_chromosome_plot.pdf", device = "pdf")

