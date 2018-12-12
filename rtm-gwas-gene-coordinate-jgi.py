import gzip


INFILE = "Gmax_189_gene.gff3.gz"
OUTFILE = "RTM_GWAS_Wm82.a1.v1_gene_coordinate_JGI.txt"

INFILE = "Gmax_275_Wm82.a2.v1.gene.gff3.gz"
OUTFILE = "RTM_GWAS_Wm82.a2.v1_gene_coordinate_JGI.txt"

INFILE = "Gmax_508_Wm82.a4.v1.gene.gff3.gz"
OUTFILE = "RTM_GWAS_Wm82.a4.v1_gene_coordinate_JGI.txt"


d = dict()
with gzip.open(INFILE) as f:
    for line in f:
        if line.startswith("##"):
            continue
        v = line.split()
        if v[2] != "gene":
            continue
        try:
            chr = int(v[0].lower().replace("gm","").replace("chr",""))
        except:
            continue
        if chr < 1 or chr > 20:
            continue
        name = v[8].split(";")[1].split("=")[1]
        start = int(v[3])
        stop = int(v[4])
        if start >= stop:
            continue
        if chr not in d:
            d[chr] = []
        d[chr].append( (stop - start, start, stop, name) )

g = []
for chr in d.keys():
    v = d[chr]
    v.sort()
    w = []
    for x in v:
        start, stop, name = x[1], x[2], x[3]
        overlap = False
        for y in w:
            if y[1] >= start and y[1] <= stop:
                overlap = True
                break
            if y[2] >= start and y[2] <= stop:
                overlap = True
                break
        if not overlap:
            w.append( (chr, start, stop, name) )
    g += w
g.sort()

with open(OUTFILE,"w") as f:
    for e in g:
        f.write("{0}\t{1}\t{2}\t{3}\n".format(e[3], e[0], e[1], e[2]))
