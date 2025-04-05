#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-04-05
Purpose: Print the Reverse complement of DNA
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA', help="Input sequence or file")
   

    return parser.parse_args()

def read_sequence(dna_args): 
   if os.path.isfile(dna_args):
     with open(dna_args) as file:  
        return file.read().strip()
   else: 
                   return dna_args.strip()

def reverse_complement(sequence):
  """Return the reverse complement of a DNA sequence"""
  complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
  return ''.join(complement.get(base, base) for base in reversed(sequence))
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sequence = read_sequence(args.DNA)
    revc = reverse_complement(sequence) 
    print(revc)



# --------------------------------------------------
if __name__ == '__main__':
    main()
