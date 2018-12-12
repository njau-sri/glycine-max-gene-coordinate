import gzip


INFILE = "Gmax_189_gene.gff3.gz"
OUTFILE = "JGI_Wm82.a1.v1_gene_coordinate.txt"

INFILE = "Gmax_275_Wm82.a2.v1.gene.gff3.gz"
OUTFILE = "JGI_Wm82.a2.v1_gene_coordinate.txt"

INFILE = "Gmax_508_Wm82.a4.v1.gene.gff3.gz"
OUTFILE = "JGI_Wm82.a4.v1_gene_coordinate.txt"


with gzip.open(INFILE) as f1, open(OUTFILE,"w") as f2:
    for line in f1:
        if line.startswith("##"):
            continue
        v = line.split()
        if v[2] != "gene":
            continue
        name = v[8].split(";")[1].split("=")[1]
        f2.write("{0}\t{1}\t{2}\t{3}\n".format(name, v[0], v[3], v[4]))
