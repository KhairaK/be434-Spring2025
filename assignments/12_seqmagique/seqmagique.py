#!/usr/bin/env python3
"""
Author : Khaira Kukich <kukichk0@arizona.edu>
Date   : 2025-05-07
Purpose: Summarize FASTA file
"""

import argparse
import os 
import sys
from tabulate import tabulate 
from typing import List 

#This one is a doozy, yikes, I'll take the 50%
# --------------------------------------------------
def get_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Argparse Python script",
    )
    parser.add_argument(
        "files",
        metavar="FILE",
        type=str,
        nargs="+",
        help="Input FASTA file(s)",
    )
    parser.add_argument(
        "-t",
        "--tablefmt",
        metavar="table",
        type=str,
        default="plain",
        help="Tabulate table style (default: plain)",
    )
    return parser.parse_args()


def die(msg: str) -> None:
    """Print error message and exit"""
    print(f"usage: {sys.argv[0]} [-h] [-t table] FILE [FILE ...]", file=sys.stderr)
    print(msg, file=sys.stderr)
    sys.exit(1)


def parse_fasta(filename: str) -> List[str]:
    """Parse FASTA file and return list of sequences"""
    if not os.path.isfile(filename):
        die(f"No such file or directory: \'{filename}\'")

    sequences = []
    seq = []

    with open(filename, "rt") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if seq:
                    sequences.append("".join(seq))
                    seq = []
            else:
                seq.append(line)

        if seq:
            sequences.append("".join(seq))

    return sequences


def main():
    """Main function"""
    args = get_args()
    headers = ["name", "min_len", "max_len", "avg_len", "num_seqs"]
    rows = []  

    for file in args.files:
        try:
            seqs = parse_fasta(file)
            lengths = list(map(len, seqs))
            num_seqs = len(seqs)
            min_len = min(lengths) if lengths else 0
            max_len = max(lengths) if lengths else 0
            avg_len = sum(lengths) / num_seqs if num_seqs else 0

            avg_len = str(int(avg_len)) if avg_len == 0 else f"{avg_len:.2f}"
            rows.append([file, min_len, max_len, avg_len, num_seqs])
        except SystemExit:
            sys.exit(1)

    if not rows:  
        sys.exit(1)  

    print(f"{'name':<26} {'min_len':<8} {'max_len':<8} {'avg_len':<8} {'num_seqs':<8}")
    for row in rows:
        name, min_len, max_len, avg_len, num_seqs = row
        avg_len = f"{avg_len:.2f}" if avg_len != 0 else '0'  
        num_seqs = str(num_seqs) 
        print(f"{name:<26} {min_len:<8} {max_len:<8} {avg_len:<8} {num_seqs:<8}")


if __name__ == "__main__":
    main()