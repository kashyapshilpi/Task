# Download the desired file
wget https://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.faa
#count the number of protein sequence
grep -c "^>" NC_000913.faa
#count the number of amino acid
grep -v '^>' NC_000913.faa | tr -d '\n' | wc -c 
#Find the avg. length of protein ## total no. of protein sequence i got 4140, total no of amino acid sequence is 1311795
echo "scale=2; 1311795/4140" | bc
