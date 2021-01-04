#!/usr/bin/env bash

# Use pdftotext to convert PDF file to text

cd pdftotext/
./pdftotext.sh test_data/28855730.pdf
cd ../

# Remove non-utf8 characters in text

cd iconv/
./iconv.sh test_data/test.txt
cd ../

# Handle a single text file with sentence segmentation and tokenization

cd sentSegmentAndTokenize/
./sentSegmentAndTokenize.py 123123 testPapers/123123.txt > 123123_processed.tsv
cd ../

# Search entities in processed TSV file

cd findEntitiesInSentences/
./findEntitiesInSentences.py 'cre-flox:testEntityReference/mini_term_cre-flox.tsv;gene:testEntityReference/mini_term_genes.tsv' ../sentSegmentAndTokenize/123123_processed.tsv > 123123_entitiesFound.tsv
cd ../
