#!/usr/bin/env python3

import argparse
import os
from Bio import SeqIO

def check_file(file_path, file_type):
    """Check if the file exists and is accessible."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_type} file '{file_path}' not found.")
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Permission denied for {file_type} file '{file_path}'.")

# Get the current directory
current_directory = os.getcwd()

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='A simple script to extract IDs of interest from your fasta file')

# Add positional arguments
parser.add_argument('-i','--input', help='file with one ID per line')
parser.add_argument('-s', '--seq', help='fasta file to extract')
parser.add_argument('-o','--output', help='name of the output to save your results')

# Parse the command-line arguments
args = parser.parse_args()

# Construct full paths using os.path.join
input_file = os.path.join(current_directory, args.input)
seq_file = os.path.join(current_directory, args.seq)
output_file = os.path.join(current_directory, args.output)

try:
    check_file(input_file, 'input')
    check_file(seq_file, 'sequence')
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
    exit(1)

selected_seqs = []

try:
    with open(input_file, 'r') as file:
        ids = file.read().splitlines()

    with open(seq_file, 'r') as f:
        for s_record in SeqIO.parse(f, 'fasta'):
            name = s_record.id
            seq = s_record.seq
            if name in ids:
                selected_seqs.append(s_record)

    with open(output_file, 'w') as output_file_handle:
        SeqIO.write(selected_seqs, output_file_handle, 'fasta')

except Exception as e:
    print(f"Error: {e}")
    exit(1)

print(f"Extraction completed. Results saved to {output_file}")