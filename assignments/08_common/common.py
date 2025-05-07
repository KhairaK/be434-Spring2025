#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-05-06
Purpose: Find common words between two files
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1', type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file (default: stdout)',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()
def get_words(filehandle): 
                    words = set()
                    for line in filehandle:
                        for word in line.split():
                            words.add(word)
                    return words 

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    words1 = get_words(args.file1) 
    words2 = get_words(args.file2)

    common = sorted(words1 & words2)

    for word in common:
                        print(word, file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
