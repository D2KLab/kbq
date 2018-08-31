# KBQ
An intelligent agent that performs quality assessment and validation of knowledge bases

## Architecture

The package `KBQ` is composed of the following modules:

- `metrics`, which contains the abstract class *metrics* and the concrete classess *completeness*, *consistency*,*hpersistency*, and *persistency*;
- `sparql`, which ontains the script *queries* that extract summary statistics based on SPARQL queries;
- `scheduler`, which contains the script *apiScheduler* that perform periodic scheduling tasks;
- `rest`, which contains the scripts for quality assessment and validation rest apis;


## Instruction

KBQ is hosted on the website: 

If you want to run the webapp locally, you need to first clone the repository and then install the requirements:

```bash
$ pip install -r requirements.txt
$ python run.py
```

## Team

- Mohammad Rashid <diego.monti@polito.it>
- Giuseppe Rizzo <giuseppe.rizzo@ismb.it>
- Marco Torchiano <marco.torchiano@polito.it>
- Nandana Mihindukulasooriya <nmihindu@fi.upm.es>
- Oscar Corcho <ocorcho@fi.upm.es> 

## Licence

These scripts are free software; you can redistribute it and/or modify it under the terms of the Apache License (Version 2.0)  published by the Apache Foundation, either version 2 of the License, or (at your option) any later version. See the file [Apache License 2](http://www.apache.org/licenses/LICENSE-2.0) in the original distribution for details. There is ABSOLUTELY NO warranty.

