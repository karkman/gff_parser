# gff_parser
Python parser to add external gene calls and functional annotation from Prokka
or IMG to Anvi'o.
Uses Python3 and gffutils package (https://github.com/daler/gffutils)

Annotate your genome/metagenome with Prokka or download annotations from the IMG
database.
Use the script to get two files needed for external gene calls and annotations for Anvi'o.   
With the `--source` flag you can specify where the annotations are coming from.

```
gff_parser.py GFF3_file --gene-calls gene_calls.txt --annotation gene_annot.txt
--source Prokka
```

This might or might not work for your files. But I hope it works for you too.

But at least you can try it out with the test files provided in the `test` folder (Thanks to [Andrew Morris](https://github.com/amorris28)).

__PROKKA__ annotations:
```
python gff_parser.py test/PROKKA.gff --gene-calls Prokka_gene_calls.txt --annotation Prokka_annotation.txt --process-all --source Prokka
```
__IMG__ annotations:
```
python gff_parser.py test/IMG.gff --gene-calls IMG_gene_calls.txt --annotation IMG_annotation.txt --process-all --source IMG
```
