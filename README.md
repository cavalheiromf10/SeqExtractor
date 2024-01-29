SeqExtractor is a script for extracting sequences from a FASTA file based on a list of sequence IDs provided in a separate file.

## Prerequisites

- Python 3
- Biopython library (`pip install biopython`)

## Installation

1. Clone the repository:

 ```bash
 git clone https://github.com/cavalheiromf/SeqExtractor.git
 cd SeqExtractor
```
2. Make the script executable

  ```console
  foo@bar: ~$ chmod +x SeqExtractor.py
  ```
## Usage
```bash
./SeqExtractor.py -i input_file -s sequence_file -o output_file
```
## Arguments
`input_file`: File with one sequence ID per line.
`sequence_file`: FASTA file containing sequences to extract.
`output_file`: Name of the output file to save the extracted sequences.

## Example
```bash
./SeqExtractor.py -i IDs_DUFs.txt -s Esalsugineum_173_v1.0.protein.fa -o output.fasta
```
This example will extract sequences from `Esalsugineum_173_v1.0.protein.fa` based on the sequence IDs listed in `IDs_DUFs.txt` and save the results to `output.fasta`.

## Troubleshooting

If you encounter any issues with file permissions or missing files, check the error messages provided by the script.
Ensure that Biopython is installed (pip install biopython).
