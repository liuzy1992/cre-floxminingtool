#!/usr/bin/env python3

import os
import sys
import spacy

def sentSegmentAndTokenize(inFileID, inFile):
    with open(inFile, 'r') as inF:
        text = inF.read().strip().replace('\n', ' ')
    nlp = spacy.load('en_core_web_sm', disable=['ner'])
    parsed = nlp(text)
    print(inFileID)
    for sent in parsed.sents:
#        print(inFileID, end='\t')
        print(sent.text.replace('\t', ' '), end='\t')
        words = [t.text.replace('\t', ' ') for t in sent]
        print('; '.join(words), end='\n')

sentSegmentAndTokenize(sys.argv[1], sys.argv[2])
