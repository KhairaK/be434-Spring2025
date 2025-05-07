#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-05-07
Purpose: Annotate BLAST output
"""

import argparse
import csv 
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
                            description='Annotate BLAST output',
                            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-b', '--blasthits',
                        metavar='str', type=argparse.FileType('rt'), required=True,
                        help='BLAST -outfmt 6')

    parser.add_argument('-a', '--annotations', metavar='str',
                        help='Annotations file',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-o', '--outfile',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        default='out.csv', metavar='str')

    parser.add_argument('-d', '--delimiter',
                        help='Output field delimiter',
                        default=',',
                        metavar='str')

    parser.add_argument('-p', '--pctid',
                        help='Minimum percent identity',
                        type=float, metavar='float',
                        default=0.0)
    return parser.parse_args() 


# --------------------------------------------------
def guess_delimiter(filename):
    with open(filename, 'rt', newline='') as f:
        sample = f.read(1024)
        sniffer = csv.Sniffer()
        return sniffer.sniff(sample).delimiter


# --------------------------------------------------
def main():
    args = get_args()

    try:
        ann_delim = guess_delimiter(args.annotations.name)
        print(f'Guessed delimiter for annotations file: {ann_delim}')
        reader = csv.DictReader(args.annotations, delimiter=ann_delim)

        annotations = {}
        for row in reader:
            qseqid = row.get('qseqid')
            if qseqid:
                annotations[qseqid] = row
        print(f'Annotations (first 3 rows): {list(annotations.items())[:3]}')
        out_fields = ['qseqid', 'pident', 'depth', 'lat_lon']
        writer = csv.DictWriter(args.outfile, fieldnames=out_fields, delimiter=args.delimiter)
        writer.writeheader()

        reader = csv.reader(args.blasthits, delimiter='\t')
        count = 0
        for row in reader:
            if len(row) < 3:
                continue

            qseqid = row[0]
            try:
                pident = float(row[2])
            except ValueError:
                continue
            print(f'Processing BLAST hit: {qseqid}, pident: {pident}')
            if qseqid not in annotations: 
                print(f'DEBUG: {qseqid} not found in annotations')
            elif pident >= args.pctid: 
                ann = annotations[qseqid]
                writer.writerow({
                    'qseqid': qseqid,
                    'pident': f'{pident:.3f}',
                    'depth': ann.get('depth', ''),
                    'lat_lon': ann.get('lat_lon', '')
                })
                count += 1

        print(f'Exported {count} hits to "{args.outfile.name}".')

    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)



# --------------------------------------------------
if __name__ == '__main__':
    main()