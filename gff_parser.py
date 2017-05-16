#!/usr/bin/env python

## Antti Karkman
## University of Gothenburg
## 2017

import gffutils
import argparse

#parse the arguments
parser = argparse.ArgumentParser(description="""Parse Prokka annotated genome/metagenome to add external gene calls and functions to anvi'o. 
					Input annotation in GFF3 format, outputs are tab-delimited text files, one for gene calls and one for annotations""")
parser.add_argument('gff_file', metavar='GFF3', help='Annotation file from Prokka in GFF3 format')
parser.add_argument('--gene_calls', default='gene_calls.txt', help='Output: External gene calls (Default: gene_calls.txt)')
parser.add_argument('--annotation', default='gene_annot.txt', help='Output: Functional annotation for external gene calls (Default: gene_annot.txt)')

args = parser.parse_args()

#Input file and output files
GFF = args.gff_file
OUT_CDS = open(args.gene_calls, 'w')
OUT_ANNO = open(args.annotation, 'w')

#load in the GFF3 file
db = gffutils.create_db(GFF, ':memory:')

#Print headers for anvi'o
print >>OUT_CDS, "gene_callers_id\tcontig\tstart\tstop\tdirection\tpartial\tsource\tversion"
print >>OUT_ANNO, "gene_callers_id\tsource\taccession\tfunction\te_value"

#running gene ID and a trumped-up e-value for the gene calls.
gene_id=1
e_value = "0"

#parse the GFF3 file and write results to output files
for feature in db.all_features():
	start = feature.start-1
	stop = feature.stop
	if (float(start-stop)/float(3)).is_integer()==True:
		partial = str(0)
	else:
		partial = str(1)
	try:
		gene_acc = feature.attributes['gene'][0]
	except KeyError:
		gene_acc = ""
	try:
		product = feature.attributes['product'][0]
	except KeyError:
		product = feature.attributes['note'][0]
	if feature.featuretype=='repeat_region':
		direction='f'
		source, version = feature.source.split(':')
		print >>OUT_CDS, str(gene_id)+"\t"+feature.seqid+"\t"+str(start)+"\t"+str(stop)+"\t"+direction+"\t"+partial+"\t"+source+"\t"+version
		print >>OUT_ANNO, str(gene_id)+"\t"+source+"\t"+gene_acc+"\t"+product+"\t"+e_value
	else:
		if feature.strand=='+':
			direction='f'
		else:
			direction='r'
		source, version = feature.source.split(':')
		print >>OUT_CDS, str(gene_id)+"\t"+feature.seqid+"\t"+str(start)+"\t"+str(stop)+"\t"+direction+"\t"+partial+"\t"+source+"\t"+version
		print >>OUT_ANNO, str(gene_id)+"\t"+source+"\t"+gene_acc+"\t"+product+"\t"+e_value
	gene_id = gene_id+1
