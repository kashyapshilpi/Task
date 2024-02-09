import gzip

def read_gene_info(file_path):
    gene_mapping = {}
    
    with gzip.open(file_path, 'rt') as file:
        for line in file:
            if line.startswith('#'):
                continue  # Skip comments
            fields = line.strip().split('\t')
            gene_id, symbol, synonyms = fields[1], fields[2], fields[4].split('|')
            gene_mapping[symbol] = gene_id
            for synonym in synonyms:
                gene_mapping[synonym] = gene_id
    
    return gene_mapping

def replace_symbols_with_entrez(gmt_path, gene_mapping):
    new_gmt_lines = []
    
    with open(gmt_path, 'r') as gmt_file:
        for line in gmt_file:
            fields = line.strip().split('\t')
            pathway_name, pathway_desc = fields[0], fields[1]
            genes = fields[2:]
            
            # Replace symbols with Entrez IDs
            entrez_genes = [gene_mapping.get(gene, gene) for gene in genes]
            
            new_line = '\t'.join([pathway_name, pathway_desc] + entrez_genes)
            new_gmt_lines.append(new_line)
    
    return new_gmt_lines

def write_new_gmt(output_path, new_gmt_lines):
    with open(output_path, 'w') as output_file:
        for line in new_gmt_lines:
            output_file.write(line + '\n')

if __name__ == "__main__":
    # Provide the file paths
    gene_info_path = "Homo_sapiens.gene_info.gz"
    gmt_path = "h.all.v2023.1.Hs.symbols.gmt"
    output_gmt_path = "output_entrez.gmt"

    # Step 1: Read gene_info file
    gene_mapping = read_gene_info(gene_info_path)

    # Step 2: Replace symbols with Entrez IDs in GMT file
    new_gmt_lines = replace_symbols_with_entrez(gmt_path, gene_mapping)

    # Step 3: Write the new GMT file
    write_new_gmt(output_gmt_path, new_gmt_lines)

    print(f"New GMT file with Entrez IDs has been created: {output_gmt_path}")

