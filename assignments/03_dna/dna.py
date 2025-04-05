#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-04-05
Purpose: 
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(description="Tetranucleotide frequency")
    parser.add_argument("DNA", help="Input DNA sequence")
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sequence = args.DNA.upper()
    a_count = sequence.count('A')
    c_count = sequence.count('C')
    g_count = sequence.count('G')
    t_count = sequence.count('T')

    print(f'{a_count} {c_count} {g_count} {t_count}')
    

   


# --------------------------------------------------
if __name__ == '__main__':
    main()
