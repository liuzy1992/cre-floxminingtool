### sentSegmentAndTokenize

**sentSegmentAndTokenize** helps to process text file based on sentence segmentation and tokenization. This can be run using following command.

```shell
./sentSegmentAndTokenize.py <inFileID> <inFile> > <outFile> 
```

* **inFileID**: The ID of input text file.

* **inFile**: Input text file.

* **outFile**: TSV format output file and its content is as following:

  *inFileID*

  *Sentence1	Word1; Word2; Word3 ...*

  *Sentence2	Word4; Word5; Word6 ...*

  *...*

* A test case is provided in **testPapers** directory. Use following command to run this test case:

```shell
./sentSegmentAndTokenize.py 123123 testPapers/123123.txt > 123123_processed.tsv
```

