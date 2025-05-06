#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-04-05
Purpose: Transcribe DNA into RNA
"""

import argparse
import os
import sys
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA into RNA')
    parser.add_argument('files', metavar= 'FILE', nargs='+', help='Input DNA file', type=str)
    parser.add_argument('-o', '--out_dir', help='Output directory (default: out', metavar='DIR', default='out') 

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.out_dir
    files = args.files
    
    if not os.path.isdir(out_dir): 
        os.makedirs(out_dir)
    
    total_sequences = 0
    for file in files: 
        try:      
            basename = os.path.basename(file)
            out_path = os.path.join(out_dir, basename) 
            with open(file) as fh_in, open(out_path, 'wt') as fh_out: 
                for line in fh_in: 
                    rna = line.strip().replace("T", "U")
                    fh_out.write(rna + '\n') 
                    total_sequences += 1
        except FileNotFoundError: 
            print(f"usage: {os.path.basename(sys.argv[0])} [-h]", file=sys.stderr) 
            print(f"No such file or directory: '{file}'", file=sys.stderr) 
            sys.exit(1)

    num_files = len(files) 
    seq_str = 'sequence' if total_sequences == 1 else 'sequences' 
    file_str = 'file' if num_files == 1 else 'files'
    print(f'Done, wrote {total_sequences} {seq_str} in {num_files} {file_str} to directory "{out_dir}".')
        


# --------------------------------------------------
if __name__ == '__main__':
    main()
