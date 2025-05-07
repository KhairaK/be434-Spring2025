#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-05-07
Purpose: Run Length Encoding
"""
#doooone
import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression')
    parser.add_argument('text',
                        metavar='str',
                        help='DNA text or file')
    return parser.parse_args()


def rle(seq):
    """Return run-length encoded string"""
    if not seq:
        return ''

    result = []
    count = 1
    prev = seq[0]

    for base in seq[1:]:
        if base == prev:
            count += 1
        else:
            result.append(prev + (str(count) if count > 1 else ''))
            prev = base
            count = 1
    result.append(prev + (str(count) if count > 1 else ''))
    return ''.join(result)


def main():
    args = get_args()

    if os.path.isfile(args.text):
        with open(args.text) as fh:
            for line in fh:
                line = line.strip()
                if line:
                    print(rle(line))
    else:
        print(rle(args.text))


def test_rle():
    """Test rle"""
    assert rle('') == ''
    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


if __name__ == '__main__':
    main() 