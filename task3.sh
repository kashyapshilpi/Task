# We have to remove some data in the chromosome column that are ambiguous and look like this: 10|19|3.Assign into a .txt file.
zcat Homo_sapiens.gene_info.gz |cut -f3,7|grep -v "|"| grep -v "-" > task3.txt
#Run the Rscript to generate the plot
Rscript plot.R
