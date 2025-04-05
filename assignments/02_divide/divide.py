#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-04-03
Purpose: Add Your Purpose
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
    description='Divide two numbers',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('INT', metavar= 'INT', nargs= 2, type=valid_int, help= 'Numbers to divide')
    return parser

def valid_int(value):
    try: 
        ivalue= int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f'invalid int value: {value}') 
    
    return ivalue
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    parser = get_args()
    args = parser.parse_args()
    numerator, denominator = args.INT
    result = numerator // denominator
    print(f'{numerator} / {denominator} = {result}')
    if args.INT[1] == 0:
            parser.error('Cannot divide by zero, dum-dum!')


# --------------------------------------------------
if __name__ == '__main__':
    main()