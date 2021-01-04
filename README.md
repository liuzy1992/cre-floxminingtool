# Cre-FloxMiningTool

**Cre-FloxMiningTool** is a text-mining based tool to find genes, cell types, drugs or other type of entities related to cre-flox in academic papers. Use following command to run the test case of this tool.

```shell
./main.sh
```

---

## Usage

### pdfConvertAndClean

**pdfConvertAndClean** helps to convert pdf files to text files based on **Xpdf's pdftotext** and **Linux's iconv**. So **Xpdf** and **iconv** should be installed first and added to your environment. The converted text files will be stored in **textConverted** directory. This can be run using following command.

```shell
./pdfConvertAndClean.sh <inputDir> <numThread>
```

More information can be found in **pdfConvertAndClean/pdfConvertAndClean.md**

### sentSegmentAndTokenize

**sentSegmentAndTokenize** helps to process text file based on sentence segmentation and tokenization. This can be run using following command.

```shell
./sentSegmentAndTokenize.py <inFileID> <inFile> > <outFile> 
```

More information can be found in **sentSegmentAndTokenize/sentSegmentAndTokenize.md**

### findEntitiesInSentences

**findEntitiesInSentences** helps to search entities in sentences and can be run using following command:

```shell
./findEntitiesInSentences.py <entity1Name:entity1Reference.tsv;entity2Name:entity2Reference.tsv> <inFile> > <outFile> 
```

More information can be found in **findEntitiesInSentences/findEntitiesInSentences.md**

