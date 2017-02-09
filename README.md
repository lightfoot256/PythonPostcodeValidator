# Digital Tech Task

## Running the files

The solutions are written for Python 3.6

From the root; they can be run from the command line as follows:

### Part 1

>     $ python -m tests.postcode_validator_test

### Part 2

The specification:

* Validate postcodes in the data file
* Report on the row_id where validation fails
* Untar the file if required (using gzip)
* At end of running import; produce file named 'failed_validation.csv' with same columns as above

Given the import csv; taken from: [Google drive](https://drive.google.com/file/d/0BwxZ38NLOGvoTFE4X19VVGJ5NEk/view?usp=sharing) and placed in the data directory; you could run the import:

>     $ python -m src.postcode_importer data\import_data.csv.gz

Summary

* Creates validator with compiled regular expression
* Opens output immediately to avoid keeping large data set in memory while processing
* Uses GZip to read file
* Skips first line to avoid header
* Prints (reports) rowId and postcode when failed validation to the console


### Part 3

Specification:

* Modifyto produce success file
* Order the output

Using the same import data from Part 2 -- you could run the import:

>     $ python -m src.postcode_importer_part3 data\import_data.csv.gz

Summary

* In memory dictionary is used to process the data; this uses more memory but allows us to sort the entire list at the end before we write it out -- to avoid use of memory we could read and write a single line at a line and insert the line into the output at the appropriate location - however this would be extremely slow so wasn't even attempted since a memory constraint wasn't given
* Dictionary keys are sorted during iteration and items are looked up based on sorted Key; An OrderedDictionary wasn't used since we don't care about insertion order here

----
## changelog
* 08-Feb-2017 Moved analysis to seperate ANALYSIS.md file
* 07-Feb-2017 Initial implementation
