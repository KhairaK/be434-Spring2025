#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-05-07
Purpose: Implement Caesar Shift
"""

import argparse
import sys
import os

def build_substitution_table(shift, decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted = alpha[shift:] + alpha[:shift]
    if decode:
        return dict(zip(shifted, alpha))
    else:
        return dict(zip(alpha, shifted))

def caesar_shift(text, table):
    result = []
    for char in text:
        upper_char = char.upper()
        if upper_char in table:
            result.append(table[upper_char])
        else:
            result.append(char)
    return ''.join(result)

def valid_file(filename):
    if not os.path.isfile(filename):
        raise argparse.ArgumentTypeError(
            f"No such file or directory: '{filename}'")
    return filename

def get_args():
    parser = argparse.ArgumentParser(
        description="caesar shift",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input file',
                        type=valid_file)

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        type=int,
                        default=3)

    parser.add_argument('-d',
                        '--decode',
                        help='Decode the message',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file (default: stdout)',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()

def main():
    args = get_args()
    shift = args.number % 26
    sub_table = build_substitution_table(shift, args.decode)

    with open(args.FILE, 'r') as infile:
        for line in infile:
            transformed = caesar_shift(line.rstrip(), sub_table)
            print(transformed.upper(), file=args.outfile)

if __name__ == '__main__':
    main()