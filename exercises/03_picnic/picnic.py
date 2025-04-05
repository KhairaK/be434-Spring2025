#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-03
Purpose: Add Your Purpose
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('Item', metavar= 'str', nargs='+', help='Item(s) to bring')
    parser.add_argument('-s', '--sorted', action='store_true', help='Sort the items')

   

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    items = args.Item
    print(f'You are bringing {items}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
