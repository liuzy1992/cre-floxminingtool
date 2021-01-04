### findEntitiesInSentences

**findEntitiesInSentences** module helps to search entities in sentences and can be run using following command:

```shell
./findEntitiesInSentences.py <entity1Name:entity1Reference.tsv;entity2Name:entity2Reference.tsv> <inFile> > <outFile> 
```

* **entityReference.tsv** should be in following format with 3 colomns and no headers (more than one terms should be sapatated by '|') : 

   *EntityID	EntityOfficialName	EntityAlias*

   e.g.

   *84515	MCM8	MCM8|Minichromosome maintenance complex component 8|C20ORF154|POF10|DJ967N21.5*

* **outFile** is in TSV format and the content is as follows:

   *FileID	Entity1ID	Entity1OfficialName	Entity1TermInSentence	Entity2ID	Entity2OfficialName	Entity2TermInSentence	SentenceText*

* An example of entity reference is provided in **testEntityReference** directory. Use following command to process **../sentSegmentAndTokenize/123123_processed.tsv** as a test case:

```shell
./findEntitiesInSentences.py 'cre-flox:testEntityReference/mini_term_cre-flox.tsv;gene:testEntityReference/mini_term_genes.tsv' ../sentSegmentAndTokenize/123123_processed.tsv > 123123_entitiesFound.tsv
```

