#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-05-07
Purpose: Find Conserved Bases
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description='Find conserved bases')
    parser.add_argument('file', metavar='FILE', type=argparse.FileType('r'),
                        help='Input file with sequences')
    return parser.parse_args()

def read_sequences(file):
    """Read sequences from the file and return them as a list"""
    sequences = []
    for line in file:
        line = line.strip()
        if not line.startswith('>'):  
            sequences.append(line)
    return sequences

def find_conserved_bases(sequences):
    """Find conserved bases in the sequences"""
    
    if len(set(len(seq) for seq in sequences)) > 1:
        raise ValueError("Sequences have different lengths")

    conserved = []
    for i in range(len(sequences[0])):  
        bases = [seq[i] for seq in sequences]
        if len(set(bases)) == 1:  
            conserved.append('|')
        else:
            conserved.append('X')
    return ''.join(conserved)

def main():
    args = get_args()

    try:
        
        sequences = read_sequences(args.file)

        
        for seq in sequences:
            print(seq)

       
        conserved_bases = find_conserved_bases(sequences)
        print(conserved_bases)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()