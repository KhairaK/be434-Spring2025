#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-04-05
Purpose: Compute GC content
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("FILE", nargs="?", help='Input sequence file')
   
    return parser.parse_args()

def read_fasta(file):
    sequences = {} 
    current_id = None 
    for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:]
                sequences[current_id] = ''
            else:
                sequences[current_id] += line
    return sequences
def gc_content(sequence): 
    gc = sum(1 for base in sequence if base.upper() in "GC") 
    return (gc / len(sequence)) * 100 if sequence else 0.0
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.FILE:
        if not os.path.isfile(args.FILE):
            print('usage: cgc.py [-h] FILE')
            print(f"cgc.py: error: No such file or directory: '{args.FILE}'")
            sys.exit(1)
        with open(args.FILE) as file:
            sequences = read_fasta(file)
    else:
        sequences = read_fasta(sys.stdin)
    max_id = None 
    max_gc = 0.0
    
    for seq_id, sequence in sequences.items(): 
        gc = gc_content(sequence) 
        if gc > max_gc:
            max_gc = gc
            max_id = seq_id
    print(f'{max_id} {max_gc:.6f}')
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
