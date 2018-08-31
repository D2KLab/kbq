# KBQ
An intelligent agent that performs quality assessment and validation of knowledge bases

## Architecture

The package `kbq` is composed of the following modules:

- `metrics`, which contains the abstract class *metrics* and the concrete classess *completeness*, *consistency*,*hpersistency*, and *persistency*;
- `sparql`, which ontains the script *queries* that extract summary statistics based on SPARQL queries;
- `scheduler`, which contains the script *apiScheduler* that perform periodic scheduling tasks;
- `rest`, which contains the scripts for quality assessment and validation rest apis;


## Instruction

If you want to run the webapp locally, you need to first clone the repository and then install the requirements:

```bash
$ pip install -r requirements.txt
```

## Team

- Mohammad Rashid <diego.monti@polito.it>
- Giuseppe Rizzo <giuseppe.rizzo@ismb.it>
- Marco Torchiano <marco.torchiano@polito.it>
- Nandana Mihindukulasooriya <nmihindu@fi.upm.es>
- Oscar Corcho <ocorcho@fi.upm.es> 

## Publications

- Mohammad Rashid, Giuseppe Rizzo, Marco Torchiano, Nandana Mihindukulasooriya, and Oscar Corcho, "A Quality Assessment Approach for EvolvingKnowledge Bases." Accepted for publication in Special issue on Benchmarking Linked Data , Semantic Web Journal (2018).
- Mohammad Rashid, Giuseppe Rizzo, Nandana Mihindukulasooriya, Marco Torchiano, and Oscar Corcho, "KBQ - A Tool for Knowledge Base Quality Assessment Using Temporal Analysis", In Proceedings of Workshops and Tutorials of the 9th International Conference on Knowledge Capture (K-CAP2017), Austin, Texas,2017 , Volume 2065 of CEUR Workshop Proceedings. CEUR-WS. org.
- Mohammad Rashid, Giuseppe Rizzo, Nandana Mihindukulasooriya, Marco Torchiano, and Oscar Corcho, "Knowledge Base Evolution Analysis: A Case Study in the Tourism Domain", In Proceedings of Workshops on Knowledge Graphs on Travel and Tourism co-located with 18th International Conferenceon Web Engineering (ICWE), Caceres,Spain, 2018.

## Licence

These scripts are free software; you can redistribute it and/or modify it under the terms of the Apache License (Version 2.0)  published by the Apache Foundation, either version 2 of the License, or (at your option) any later version. See the file [Apache License 2](http://www.apache.org/licenses/LICENSE-2.0) in the original distribution for details. There is ABSOLUTELY NO warranty.

