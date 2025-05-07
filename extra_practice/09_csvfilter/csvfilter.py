#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-05-07
Purpose: Add Your Purpose
"""

import argparse
import csv
import re
import sys
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(description='Filter delimited records')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), required=True, help='Input file')
    parser.add_argument('-v', '--val', required=True, help='Value for filter')
    parser.add_argument('-c', '--col', help='Column name for filter')
    parser.add_argument('-o', '--outfile', type=str, default='out.csv', help='Output file name')
    parser.add_argument('-d', '--delimiter', default=',', help='Input file delimiter (default: ",")')
    return parser.parse_args()
                    
def main():
    args = get_args()
   
    reader = csv.DictReader(args.file, delimiter=args.delimiter)
    fieldnames = reader.fieldnames
   
    if args.col and args.col not in fieldnames:
       print(f'Error: --col "{args.col}" not a valid column!', file=sys.stderr)
       sys.exit(1)
    else: 
     writer = csv.DictWriter(open(args.outfile, 'w', newline=''), fieldnames=fieldnames, delimiter=args.delimiter)
    writer.writeheader()
    
    count = 0
   
    for row in reader:
        if args.col:  
            text = row[args.col]
        else:  
            text = " ".join(row.values())
        if re.search(args.val, text, re.IGNORECASE):
            writer.writerow(row)
            count += 1
    print(f'Done, wrote {count} to "{args.outfile}".')
if __name__ == '__main__':
    main()