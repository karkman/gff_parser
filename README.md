# gff_parser
Python parser to add external gene calls and functional annotation from Prokka
or IMG to Anvi'o.
Uses Python3 and gffutils package (https://github.com/daler/gffutils)

Annotate your genome/metagenome with Prokka or download annotations from the IMG
database.
Use the script to get two files needed for external gene calls and annotations for Anvi'o 

```
gff_parser.py GFF3_file --gene-calls gene_calls.txt --annotation gene_annot.txt
--source Prokka
```

This might or might not work for your files. But I hope it works for you too.
