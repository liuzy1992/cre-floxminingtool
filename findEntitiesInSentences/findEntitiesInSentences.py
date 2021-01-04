#!/usr/bin/env python3

import os
import sys
from collections import defaultdict
import re

def loadEntityReference(entityList):
    lookup = defaultdict(dict)
    ID2name = {}
    entityTypes = []
    for entitytype, filename in entityList:
#        lookup.update({entityType: defaultdict()})
#        assert os.path.isfile(filename), "s% does not exitsts!" %filename
        entityTypes.append(entitytype)
        with open(filename, 'r') as f:
            tempLookup = defaultdict(set)
            for line in f.readlines():
                split = line.strip().split('\t')
                termid, terms = split[0], split[2]
                ID2name.update({split[0]: split[1].strip()})
                for term in terms.split('|'):
                    tempLookup[term.lower().strip()].add(termid)
                    
        for term, idlist in tempLookup.items():
            lookup[term].update({entitytype: ";".join(sorted(list(idlist)))})
    
    return lookup, ID2name, entityTypes

def searchEntities(inFile, lookup, typeNum):
    KOsymbols = ['-/-', '\+/-', '-/\+', 'f/f', 'flox/flox', 'lox/lox', 'f/wt', 'wt/f']    
    entitiesInSentences = {}
    with open(inFile, 'r') as inF:
        lines = inF.readlines()
        inFileID = lines[0].strip()
        for line in lines[1:]:
            sent = line.strip().split('\t')[0]
            words = line.strip().split('\t')[1].split('; ')

            termsFound, typeLookup = [], []
            wordsFiltered = []
            for w in words:
                for s in KOsymbols:
                    w = re.sub(s, '', w)
                wordsFiltered.append(w)
#        print(wordsFiltered)

            for startPos in range(len(wordsFiltered)):
                for endPos in range(startPos+1, len(wordsFiltered)+1):
                    c1 = ' '.join(wordsFiltered[startPos:endPos])
                    c2 = ''.join(wordsFiltered[startPos:endPos])
                    if c1 in lookup and c1 not in termsFound:
#                    termtypesAndids.append(lookup[s])
                        termsFound.append(c1)
                    if c2 in lookup and c2 not in termsFound:
                        termsFound.append(c2)
            if len(termsFound) >= 2:
                for t in termsFound:
                    for typeAndID in lookup[t]:
                        if typeAndID[0] not in typeLookup:
                            typeLookup.append(typeAndID[0])
#                    typeLookup[typeAndID[0]] = True
#            for k, v in typeLookup:
#                if not v:
#                    break
                if len(typeLookup) == typeNum:
                    entitiesInSentences.update({sent: termsFound})
    return inFileID, entitiesInSentences

def findEntitiesInSentences(inFile, entityReference):
    assert len(entityReference.split(';')) >= 2, "Two or more pairs of entity type names and entity reference files are needed!"
    entityList = [tuple(e.split(':')) for e in entityReference.split(';')]
#    print("%s: Loading %d types of entity information from reference files..." %(now(), len(entityList)))
    termLookup, termID2name, entityTypes = loadEntityReference(entityList)
    
    inFileID, entitiesInSentences = searchEntities(inFile, termLookup, len(entityTypes))
    
    if entitiesInSentences:
        for sent, terms in entitiesInSentences.items():
            print(inFileID, end='')
            for e in sorted(entityTypes):
                outIDs, outNames, outTerms = [], [], []
                for t in terms:
                    if e in termLookup[t]:
                        outIDs.append(termLookup[t][e])
                        tempNames = ';'.join([ termID2name[ID] for ID in termLookup[t][e].split(';') ])
                        outNames.append(tempNames)
                        outTerms.append(t)
                print('\t'+'|'.join(outIDs)+'\t'+'|'.join(outNames)+'\t'+'|'.join(outTerms), end='')
            print('\t'+sent, end='\n')

findEntitiesInSentences(sys.argv[2], sys.argv[1])
